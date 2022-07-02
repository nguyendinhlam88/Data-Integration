import json
import math
import pandas as pd

from strsimpy.levenshtein import Levenshtein
from strsimpy.cosine import Cosine
from strsimpy.longest_common_subsequence import LongestCommonSubsequence
from strsimpy.jaccard import Jaccard

from fuzzyfinder import fuzzyfinder

class BrandIterator:
  brands = None
  brand = None

  def __init__(self, brands) -> None:
    self.brand = brands.first()
    self.brands = brands

  def __next__(self):
    return next(self.brand)

class Brands:
  brandsDict = dict()
  brands = None
  cars = []
  unknownBrandCars = []
  
  def __init__(self) -> None:
    self.brands = ['alfa romeo', 'aston martin', 'audi', 'bentley', 'bmw', 'cadillac', 'chery', 'chevrolet', 
                   'chrysler', 'citroen', 'dacia', 'daewoo', 'daihatsu', 'dfm', 'dodge', 'ferrari', 'fiat', 
                   'ford', 'geely', 'honda', 'hyundai', 'infiniti', 'isuzu', 'jaguar', 'jeep', 'kia', 'lada', 
                   'lamborghini', 'lancia', 'land rover', 'maserati', 'mazda', 'mercedes', 'mini', 'mitsubishi', 
                   'nissan', 'opel', 'peugeot', 'porsche', 'proton', 'renault', 'rover', 'saab', 'seat', 'skoda', 
                   'smart', 'ssangyong', 'subaru', 'suzuki', 'tata', 'tofaş', 'toyota', 'volkswagen', 'volvo']
    for i, brand in enumerate(self.brands):
      self.cars.append([])
      self.brandsDict[brand] = i

  # return idx in brands
  # return None on nothing
  def Find(self, s: str) -> int:
    s_ = s.lower()
    for i, brand in enumerate(self.brands):
      if brand in s_:
        return i

    return None

  def Insert(self, idx, v):
    if idx is not None:
      self.cars[idx].append(v)
      return

    self.unknownBrandCars.append(v)

  def idx(self, s: str):
    if s in self.brandsDict:
      return self.brandsDict[s]
    return None

  def first(self):
    return iter(self.brandsDict)

  def __getitem__(self, s: str):
    if s in self.brandsDict:
      brand = self.brandsDict[s]
      return self.cars[brand]

    return self.unknownBrandCars

  def __iter__(self):
    return BrandIterator(self)

  #def next(self, current):
  #  return next(current)


class Metric:
  method: None
  threshold: None

  def __init__(self, method, threshold) -> None:
    self.method = method
    self.threshold = threshold
    pass


class DataWareHouse:
    __instance = None

    brands: Brands
    brandMetrics: dict[str, Metric]

    # group by name
    # tuple[str, int] -- (ten, group idx)
    brandGroups: list[tuple[list[pd.DataFrame], list[str], list[int]]]

    def __init__(self) -> None:
      self.brands = Brands()
      self.brandMetrics = dict()
      self.brandGroups = list()

      files = ['anycar_bonbanh.csv', 'bonbanh.csv', 'carmudi.csv', 'chotot.csv', 'oto.csv']
      sources = []

      for f in files:
        sources.append(pd.read_csv(f'./warehouse/sources_data/{f}', encoding='utf-8'))

      for i, s in enumerate(sources):
        sources[i]['ten'] = s['ten'].apply(lambda x: x.replace('\t', ' '))

      for src in sources:
        for i, row in src.iterrows():
          idx = self.brands.Find(row['ten'])
          self.brands.Insert(idx, row)

      for brand in self.brands:
        if brand == 'mercedes':
          self.brandMetrics[brand] = Metric(Levenshtein(), 3)
          continue

        self.brandMetrics[brand] = Metric(Levenshtein(), 8)

      
      for brand in self.brands:
        metric = self.brandMetrics[brand].method
        thres = self.brandMetrics[brand].threshold
        groups = self.Filter(pd.DataFrame(self.brands[brand]), metric, thres)
        names = []
        gId = []

        gIdx = 0
        for group in groups:
          for i, row in group.iterrows():
            names.append(row['ten'])
            gId.append(gIdx)
          gIdx += 1
          
        self.brandGroups.append((groups, names, gId))

      pass


    @staticmethod
    def Initialize():
      if DataWareHouse.__instance is None:
        DataWareHouse.__instance = DataWareHouse()
      return DataWareHouse.__instance

    @staticmethod
    def Instance():
      return DataWareHouse.__instance


    def Filter(self, df, metric, thres) -> list[pd.DataFrame]:
      samples = []

      #count = 0

      while len(df) != 0:
        sample = df.iloc[0]['ten'].lower()
        sames = []
        drops = []

        for i, row in df.iterrows():
          name = row['ten'].lower()
          if metric.distance(sample, name) < thres:
            sames.append(row)
            drops.append(i)

        samples.append(pd.DataFrame(sames))
        df.drop(drops, inplace=True)

        #count += 1
        #if count > 10: break

      return samples


    def SaveListDFAsCSV(self, listDF, path):
      f = open(path, 'w')
      listDF[0]['ten'].to_csv(f, index=False)
      for i in range(1, len(listDF)):
        f.write('\n###########################################################################################\n\n')
        listDF[i]['ten'].to_csv(f, index=False, header=False)


    def Search(self, s: str):
      brandGroup = self.brandGroups[self.brands.Find(s)]
      groups = brandGroup[0]
      names = brandGroup[1]
      gId = brandGroup[2]
      suggestions = fuzzyfinder(s, names)

      retGroups: list[pd.DataFrame] = []
      retGroupsIdxs = []

      for s in suggestions:
        idx = names.index(s)
        gidx = gId[idx]
        g = groups[gidx]
        if gidx not in retGroupsIdxs:
          retGroups.append(g)
          retGroupsIdxs.append(gidx)
      
      retJsons: list[str] = []
      for df in retGroups:
        l = []
        for i in df.index:
          l.append(df.loc[i].to_dict())
        retJsons.append(l)

      return retJsons

    
    def ListSamples(self):
      ret: list[dict[str, ]] = []
      for brand in self.brands:
        idx = self.brands.idx(brand)
        groups = self.brandGroups[idx][0]

        if len(groups) == 0: continue

        t = dict()
        t['brand'] = brand
        l = []

        for group in groups:
          df: pd.DataFrame = group
          l.append(df.iloc[0].to_dict())

        t['samples'] = l
        ret.append(t)

      return ret

def main():
  instance = DataWareHouse.Initialize()
  print(instance.Search('Toyota vios'))
  pass

if __name__ == '__main__':
  main()
else:
  DataWareHouse.Initialize()