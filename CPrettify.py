import sublime
import sublime_plugin
import subprocess
import os
import shlex

# os.system can't be used here since it creates new cmd window

def handleProcess():

	res = subprocess.check_output(['/lib/uncrustify.exe','']) 

	#arguments containing the code

def runSetup():

	dPath = dirSetup() + tArgs()

	print('---generated arguments---')

	print(dPath)

	print('-----------end-----------')

	dpath=shlex.split(dPath)

	return dPath

def execute(args):

	info = None

	if os.name == 'nt':

		info=subprocess.STARTUPINFO()

		info.dwFlags |= subprocess.STARTF_USESHOWWINDOW



	#building file path

	packageDir=sublime.packages_path()

	libDir=os.path.join('CPrettify','lib')

	fDir=os.path.join(packageDir,libDir)

	fileDir=os.path.join(fDir,'ben.cfg')


	#test file for debug only
	tfile=os.path.join(fDir,"abc.c")


	#check if the file exists:

	if os.path.isfile(fileDir):


	#for dbug only

		print("config file exists!")

	cmd = [dirSetup(),"-c",fileDir,"--no-backup",tfile]

	pR=p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,startupinfo = info)

	output , stderr = p.communicate()

	print(output)

	print(stderr)

def extractView():

	print('')

def dirSetup():

	packageDir=sublime.packages_path()

	libDir=os.path.join('CPrettify','lib')

	fDir=os.path.join(packageDir,libDir)

	bPath = os.path.join(fDir,'uncrustify.exe')

	print(bPath)

	return bPath


#etempargs

def tArgs():

	return "-c ben.cfg --no-backup abc.c";

def argsSetup(args):

	return shlex.split(args)

class CprettifyCommand(sublime_plugin.TextCommand):

	def run(self, edit):


		#self.view.insert(edit, 0, "#Prettified by CPrettify")
		genVar=runSetup()

		execute(genVar)



#Menu entry for sublime
#cprettify_file
class CprettifyFileCommand(sublime_plugin.TextCommand):

	def run(self, edit, **kwargs):

		#setup directories and variables
		#generating folder path

		#doc reference future chnages to api

		#"https://www.sublimetext.com/docs/3/api_reference.html#sublime.View"
		
		if(sublime.View.substr is ''):

			sublime.status_message("This is empty!!")

			return

		#failproofing

		#region api reference for sublime text 3
		#https://www.sublimetext.com/docs/3/api_reference.html#sublime.Region

		#check if the region of the file is empty
		#constructor
		if(sublime.Region(0,self.view.size()).empty()):

		#window api ST3
		#https://www.sublimetext.com/docs/3/api_reference.html#sublime.Window

			sublime.status_message("This is empty!!")

			return

		#go ahead and proecessing the file
		
		execute(runSetup())
















#ways that can be run
# $ uncrustify -c mystyle.cfg -f somefile.c -o somefile.c.unc
# $ uncrustify -c mystyle.cfg -f somefile.c > somefile.c.unc
# $ uncrustify -c mystyle.cfg somefile.c
# $ uncrustify -c mystyle.cfg --no-backup somefile.c
# $ uncrustify -c mystyle.cfg *.c
# $ uncrustify -c mystyle.cfg --no-backup *.c

