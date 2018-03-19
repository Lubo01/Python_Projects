from os import rename, listdir
for filename in listdir("."):
    rename(filename,filename.replace('%20',' '))
	
#listdir   	list files in current directory
#2nd step:  renames files by replacing substring given e.g. %20 with space,
# 			[optional argument number of occurrence]
