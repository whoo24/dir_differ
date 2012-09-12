import os
import hashlib
import glob
from sets import Set

PATH_ROOT1 = 'C:/SVN/kynapse'
PATH_ROOT2 = 'C:/Users/Choe Woo-Yeong/Downloads/kynapse_2013.0.4_195561_win64_vc10_src'

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
	file_list = []

	for d in glob.glob(dir_path + '/*' ):
		if os.path.isdir( d ):
			a = get_list_dir( d )
			dir_list.append( d )
			for _a in a[0]:
				dir_list.append( _a )
			for _b in a[1]:
				file_list.append( _b )
		else:
			file_list.append( d)
		
	dir_list.sort()
	file_list.sort()

	return dir_list, file_list

def comapre_both( a, b ):
	if a == b:
		return 0

	elif a < b:
		return -1

	else:
		return 1


def compare_dir( files1, files2 ):
	idx1 = 0
	idx2 = 0

	added = Set([])
	removed = Set([])

	while (idx1 < len(files1) and idx2 < len(files2) ):
		r = comapre_both( files1[idx1], files2[idx2] )
		if r == 0:
			idx1 += 1
			idx2 += 1

		elif r == -1:
			removed.add( files1[idx1] )
			idx1 += 1

		else:
			added.add( files2[idx2] )
			idx2 += 1

	if idx1 < len(files1):
		for i in range( len(files1) - idx1):
			removed.add( files1[i + idx1] )

	if idx2 < len(files2):
		for i in range( len(files2) - idx2):
			added.add( files2[i + idx2] )

		
	return added, removed



def compare_file( files1, files2 ):
	idx1 = 0
	idx2 = 0

	added = Set([])
	removed = Set([])

	while (idx1 < len(files1) and idx2 < len(files2) ):
		if files1[idx1] == files2[idx2]:
			idx1 += 1
			idx2 += 1

		elif files1[idx1] < files2[idx2]:
			removed.add( files1[idx1] )
			idx1 += 1

		else:
			added.add( files2[idx2] )
			idx2 += 1


	if idx1 < len(files1):
		for i in range( len(files1) - idx1):
			removed.add( files1[i + idx1] )

	if idx2 < len(files2):
		for i in range( len(files2) - idx2):
			added.add( files2[i + idx2] )
		
	return added, removed

#print (md5_for_file('C:/Git/file_differ/differ.py') == md5_for_file('C:/Git/file_differ/differ.py'))
list1 = get_list_dir(PATH_ROOT1)
list2 = get_list_dir(PATH_ROOT2)

def print_compare_result( result ):

	for _r in result[0]:
		print '+ ' + _r

	for _r in result[1]:
		print '- ' + _r

def compare( list1, list2):
	r = []
	if list1 != list2:
		dir1 = []
		dir2 = []

		for d in list1[0]:
			dir1.append(d.replace(PATH_ROOT1, ''))
		for d in list2[0]:
			dir2.append(d.replace(PATH_ROOT2, ''))

		result_d = compare_dir( dir1, dir2 )
		print_compare_result( result_d )

		file1 = []
		file2 = []

		for d in list1[1]:
			file1.append( d.replace(PATH_ROOT1, '') )
		for d in list2[1]:
			file2.append( d.replace(PATH_ROOT2, '') )

		r = compare_file( file1, file2 )
		print_compare_result( r )


compare( list1, list2 )