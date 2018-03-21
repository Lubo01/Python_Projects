# -*- coding: utf-8 -*-
"""	Project Safedocs
	Backup automatic tool
	Documentation check
	Author:LL, Done: 01/2018"""

import os, shutil, time, sys

# 1 set source and backup folder

#take current date for backup folder name suffix
def backup_date():
	today = time.localtime()[0:3]
	today2 = [0,0,0]
	print today

	for i in range (0,3):
		if (today[i])<10:
			today2[i] = "0%s" % (today[i])
		else:
			today2[i] = "%s" % (today[i])
	suffix = today2[0]+today2[1]+today2[2]
	print suffix
	return suffix

#set source folder for backup
back_this = "e:\\try\\fold1"	#"e:\\7_AbsoluteAccount"
suffix = backup_date()
#set destination folder
backup_here = os.path.join("f:\\backup_" + suffix)
print "The value of backup_here is %s" % backup_here

#list files for selecting backup
#os.chdir(path)

#shutil.copytree(src,dst,symlinks=False,ignore=None)
""""
folder=os.getcwd()
print folder
print os.getcwd()

#list folder content
#print os.listdir(folder)
for i in os.listdir(folder):
	print i
	"""

# 2 Backup copy

#copy file
#shutil.copy2(back_this,backup_here)
#copy directory tree including files
#shutil.copytree(back_this,backup_here)

#alternative for more speed in Windows with windows xcopy 
#have to make different calls for Linux and Windows..

if sys.platform == 'win32':
	os.system('xcopy /S /I /E /Y "%s" "%s"' % (back_this, backup_here))
	#add /S subdirectories, /I include copy to directory, 
	#add /E copy also empty directories, /Y Yes to overwrite existing files 
	
else:
	shutil.copy(back_this, backup_here)

#alternative for more speed by increasing buffer size from 16kb to 16MB
"""
import shutil

def _copyfileobj_patched(fsrc, fdst, length=16*1024*1024):
    #Patches shutil method to hugely improve copy speed
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break
        fdst.write(buf)
shutil.copyfileobj = _copyfileobj_patched
"""
