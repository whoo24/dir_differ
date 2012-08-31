import os
import hashlib
def md5_for_file(path, block_size=2**20):
	f = open(path)
	md5 = hashlib.md5()
	while True:
		data = f.read(block_size)
		if not data:
			break
        	md5.update(data)
        f.close()
    	return md5.digest()
'''
def list_dir(dir_path):
	for dirname, dirnames, filenames in os.walk(dir_path):
	    for subdirname in dirnames:
	        print os.path.join(dirname, subdirname)
	    for filename in filenames:
	        print os.path.join(dirname, filename)
'''
def get_list_dir(dir_path):
	dir_list = []
	for dirname, dirnames, filenames in os.walk(dir_path):
	    for subdirname in dirnames:
	        filtered_dir_name = os.path.join(dirname[len(dir_path): len(dirname)], subdirname)
	        if( filtered_dir_name.find('\\.svn') != -1):
	        	continue
	        #print filtered_dir_name
	    for filename in filenames:
	    	filtered_file_name = os.path.join(dirname[len(dir_path): len(dirname)], filename)
	        if( filtered_file_name.find('\\.svn') != -1):
	        	continue
	        #print os.path.join(dirname, filename)
	        dir_list.append( filtered_file_name )
	return dir_list



#print (md5_for_file('C:/Git/file_differ/differ.py') == md5_for_file('C:/Git/file_differ/differ.py'))
list1 = get_list_dir('C:/svn/kynapse')
list2 = get_list_dir('C:/Users/Choe Woo-Yeong/Downloads/kynapse_2013.0.4_195561_win64_vc10_src')

print list1 == list2