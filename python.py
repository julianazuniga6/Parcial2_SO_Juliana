from flask import Flask, abort, request
from comandos import get_all_files, eliminar_a, get_recientes, create_file
import json


app = Flask(__name__)
api_url = '/files'

@app.route(api_url,methods=['POST'])
def crear():
  content = request.get_json(silent=True)
  nombre= content['filename']
  contenido= content['content']
  resp= create_file(nombre, contenido)
  if not nombre:
   return 400
  else:
    return resp, 201

@app.route(api_url,methods=['GET'])
def listado():
  list = {}
  list["files"] = get_all_files()
  #return "hello"
  return json.dumps(list), 200

@app.route(api_url,methods=['PUT'])
def put_files():
  return "NOT FOUND", 404


@app.route(api_url,methods=['DELETE'])
def eliminar_files():
  for file in get_all_files():
    eliminar_a(file)
  return "SE ELIMINARON LOS ARCHIVOS DE filesystem_user", 200


@app.route(api_url+"/recently_created",methods=['POST'])
def post_recent():
  return "NOT FOUND", 404


@app.route(api_url+"/recently_created",methods=['GET'])
def listar_recientes():
  list = {}
  list["files"] = get_recientes()
  return json.dumps(list), 200

@app.route(api_url+"/recently_created",methods=['PUT'])
def put_recent():
  return "NOT FOUND", 404

@app.route(api_url+"/recently_created",methods=['DELETE'])
def delete_recent():
  return "NOT FOUND", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6969,debug='True')
