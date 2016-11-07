import pytest
import python
import json

@pytest.fixture
def client(request):
    client = python.app.test_client()
    return client



def create_file(client):
	return client.post('/files',data=json.dumps(dict(filename='test_file',content='It is working')),content_type='application/json')

def test_create_file(client):
	result= create_file(client)
	assert result.status == "201 CREATED", "Error creando archivo"



def get_files(client):
	return client.get('/files',follow_redirects=True)

def test_get_files(client):
	result = get_files(client)
	assert result.data != None, "Error obteniendo la lista de archivos"




def put_file(client):
	return client.put('/files',follow_redirects=True)

def test_put_file(client):
	result= put_file(client)
	assert result.status == "404 NOT FOUND", "Error en el servicio"



def delete_files(client):
	return client.delete('/files',follow_redirects=True)

def test_delete_files(client):
	result= delete_files(client)
	assert result.status == "200 OK", "Error eliminando archivos"




def post_recent(client):
	return client.post('/files/recently_created',follow_redirects=True)

def test_post_recent(client):
	result= post_recent(client)
	assert result.status == "404 NOT FOUND", "Error en el servicio"



def get_recent_files(client):
	return client.get('/files/recently_created',follow_redirects=True)

def test_get_recent_files(client):
	result = get_recent_files(client)
	assert result.data != None, "Error obteniendo la lista de archivos"




def put_recent(client):
	return client.put('/files/recently_created',follow_redirects=True)

def test_put_recent(client):
	result= put_recent(client)
	assert result.status == "404 NOT FOUND", "Error en el servicio"



def delete_recent(client):
	return client.put('/files/recently_created',follow_redirects=True)

def test_delete_recent(client):
	result= delete_recent(client)
	assert result.status == "404 NOT FOUND", "Error en el servicio"