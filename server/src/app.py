from flask import Flask, request, jsonify

from warehouse.data import DataWareHouse

app = Flask(__name__)

@app.route('/api/search', methods=['GET'])
def Search():
  args = request.args
  s = f'{args["brand"]} {args["name"]}'
  return jsonify(DataWareHouse.Instance().Search(s))

@app.route('/api/list', methods=['GET'])
def List():
  return jsonify(DataWareHouse.Instance().ListSamples())

if __name__ == '__main__':
  app.run()