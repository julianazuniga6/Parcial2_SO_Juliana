from subprocess import Popen, PIPE
 
def get_all_files():
	lista = Popen(["ls","/home/filesystem_user/files/"], stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,lista)

def create_file(filename, content):
	create= Popen(["touch", "/home/filesystem_user/files",filename])
	a=open("/home/filesystem_user/files/"+filename,"w")
	a.write(content)
	a.close()
	return "Se creo el archivo"

  
def eliminar_a(file):
	r=Popen(["rm", '-f', "/home/filesystem_user/files/"+file], stdout=PIPE, stderr=PIPE)
	
	return "se han eliminado todos los archivos de filesystem_user"


def get_recientes():
	lista= Popen(["find", "/home/filesystem_user/files/", '-type', 'f', '-mtime', '-1'], stdout=PIPE, stderr=PIPE)
	#recientes= Popen(["grep", "filesystem_user/files/"], stdin=lista.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	listo= Popen(["awk", '-F', '/', '{print $5}'], stdin=lista.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
	return filter(None,listo)




