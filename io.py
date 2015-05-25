import os, json

#######################################################################################
#								File Operations										#
#######################################################################################

############################# Read Operations #############################
def read_lines(filepath):
	'''
		Reads a file into an array, where every line is an element
	'''
	lines = list()
	with open(filepath, "r") as f:
		lines = f.readlines()
	return lines

def read_string(filepath):
	'''
		Reads a file into one single string
	'''
	line = str()
	with open(filepath, "r") as f:
		line = f.read()
	return line

def read_json(filepath):
	'''
		Reads a json object from file
	'''
	with open(filepath, "r") as f:
		data = json.load(f)
	return data
	
############################# Write Operations #############################
def write_string(string, filepath):
	'''
		Writes a line to the end of a file in *filepath*
	'''
	exists_allready = True if os.path.isfile(filepath) else False
	with open(filepath, "aw") as f:
		f.write(("\n" + string) if exists_allready else string) 
		
def write_json(data, filepath):
	'''
		Write a json object to file
	'''
	with open(filepath, "w") as f:
		json.dump(data, f)
		
#######################################################################################
#							Directory Operations										#
#######################################################################################

############################# Create Operations #############################
def create_dir(dir):
	'''
		Create a new directory if it does not exist
	'''
	if not os.path.exists(dir):
		os.makedirs(dir)