import pandas as pd
import pickle
import os
from valentine import valentine_match
from valentine.algorithms import Coma


def read_data(data_path: str):
    mediated_schema = pd.read_csv(data_path + '/mediated_schema.csv')
    anycar_bonbanh = pd.read_csv(data_path + '/anycar_bonbanh.csv')
    bonbanh = pd.read_csv(data_path + '/bonbanh.csv')
    carmudi = pd.read_csv(data_path + '/carmudi.csv')
    chotot = pd.read_csv(data_path + '/chotot.csv')
    oto = pd.read_csv(data_path + '/oto.csv')
    return mediated_schema, anycar_bonbanh, bonbanh, carmudi, chotot, oto


def schema_matching(matcher, config_folder: str):
    anycar_bonbanh_mediated = valentine_match(mediated_schema, anycar_bonbanh, matcher, 'mediated_schema',
                                              'anycar_bonbanh')
    bonbanh_mediated = valentine_match(mediated_schema, bonbanh, matcher, 'mediated_schema', 'bonbanh')
    carmudi_mediated = valentine_match(mediated_schema, carmudi, matcher, 'mediated_schema', 'carmudi')
    chotot_mediated = valentine_match(mediated_schema, chotot, matcher, 'mediated_schema', 'chotot')
    oto_mediated = valentine_match(mediated_schema, oto, matcher, 'mediated_schema', 'oto')

    for result in [anycar_bonbanh_mediated, bonbanh_mediated, carmudi_mediated, chotot_mediated, oto_mediated]:
        file_name = None
        mapping = {}
        for key, value in result.items():
            file_name = key[0][0] + '_' + key[1][0]
            attr1, attr2 = key[0][1], key[1][1]
            mapping[attr1] = attr2
        with open(config_folder + '/' + file_name + '.pkl', 'wb') as file:
            pickle.dump(mapping, file)


if __name__ == '__main__':
    project_path = os.getcwd()
    data_path = project_path + '/WebScrapy/Crawl_Data'
    mediated_schema, anycar_bonbanh, bonbanh, carmudi, chotot, oto = read_data(data_path=data_path)
    matcher = Coma(strategy="COMA_OPT_INST")
    config_mapping = project_path + '/config_mapping'
    schema_matching(matcher=matcher, config_folder=config_mapping)
