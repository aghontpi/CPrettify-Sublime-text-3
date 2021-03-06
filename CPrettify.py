import sublime
import sublime_plugin
import subprocess
import os
import shlex
from shutil import copy

# os.system can't be used here since it creates new cmd window

#arguments containing the code

#initiate load settings settings

#so can be access from anywhere

setting = None

flag = 0

user_setting = None

user_config = False

#For restoring purposes.

file_ = None

chkflag = None

def init(view):

	global setting 

	global user_setting

	global file_

	global chkflag

	#custom settings file for package. handling view.settings() in the fuction getSettings().

	setting = sublime.load_settings("CPrettify.sublime-settings")

	user_setting = sublime.load_settings("Preferences.sublime-settings")

	file_ = getSettings(view,'config_file')

	chkflag =  getSettings(view,'user_config_file')

	#checking in view.settings() first

	if file_ is None:

		file_ = setting.get('config_file')


	if chkflag is None:

		chkflag = setting.get('user_config_file')




#function: getSettings()

#Description: Accessing the view's setting object,(project specific settings).

#returns: returns view's setting object.

def getSettings(view,arg):

	return view.settings().get(arg)


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

def restore_config():

	global file_

	file = get_path();

	if file_ is None:

		#error
		#TODO
		#raise error/exception to sublime here
		print("no config file found in that name")

		return

	original_config = os.path.join(file,file_)

	original_config = original_config

	backup_config = os.path.join(file,file_+'.bk')

	copy(backup_config,original_config)

	

def get_path():

	#building file path

	packageDir=sublime.packages_path()

	libDir=os.path.join('CPrettify','lib')

	fDir=os.path.join(packageDir,libDir)

	return fDir


def userFoldercheck():

	packageDir=sublime.packages_path()

	dirFolder=os.path.join(packageDir,'User','CPrettify')

	if not os.path.isdir(dirFolder):

		#TODO
		#change to makedirs
		os.mkdir(dirFolder)

	cfgfile=os.path.join(dirFolder,'user.cfg')

	return os.path.isfile(cfgfile)




def execute_(view,edit,region):

	global flag

	global file_

	global chkflag

	info = None

	file_cfg = None

	if os.name == 'nt':

		info=subprocess.STARTUPINFO()

		info.dwFlags |= subprocess.STARTF_USESHOWWINDOW


	#getting config from default settings

	#"https://www.sublimetext.com/docs/3/api_reference.html#sublime.Settings"



	#check if user has own cfg

	isCustomCfg = eval(chkflag)

	if isCustomCfg:

		packageDir=sublime.packages_path()

		file_cfg=os.path.join(packageDir,'User','CPrettify','user.cfg')

	
	config_ = file_
	
	if config_ is None:

		#error
		sublime.status_message("No config file found.. reinstall plugin")
		
		return

	#for debug only

	if isCustomCfg is False:

		print('using ' + config_ +' file..')

	else:

		print('using ' + file_cfg + ' file')

		if not userFoldercheck():

			sublime.status_message("Not provided user config file")

			flag = 1

			return


	packageDir=sublime.packages_path()

	libDir=os.path.join('CPrettify','lib')

	fDir=os.path.join(packageDir,libDir)

	fileDir=os.path.join(fDir, config_)


	#test file for debug only
	#tfile=os.path.join(fDir,"abc.c")


	#check if config file exists in lib folder:

	if os.path.isfile(fileDir):

		#debug if occurs
		#for dbug only

		print("config file exists!")

	else:

		flag =1

		sublime.status_message("Provided Default config file doesnt exist")

		return 

	cmd = [dirSetup(),"-c",fileDir,"-l","c"]
	
	if user_config and isCustomCfg:

		cmd = [dirSetup(),"-c",file_cfg,"-l","c"]

		print('overriding provided files and using custom file')


	#TO DO 
	#handle errors..which is quite a lot.

	pR=p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,startupinfo = info)

	#view class "sublime.View" "https://www.sublimetext.com/docs/3/api_reference.html#sublime.View"

	#EROR FIX # 'str' does not support the buffer interface


	#reference for ueing stdin as input
	#communicate() returns a tuple (stdoutdata, stderrdata). 
	#docs https://docs.python.org/2/library/subprocess.html

	output , stderr = p.communicate(input = (view.substr(region).encode("utf-8")))


	#Todo 
	#branch out on problems

	#getting error from config file

	braceserror = setting.get('unmatched_braces');
	
	if braceserror in str(stderr):

		#dont replace the intended teest for further infi check logs

		#remove this after debugging

		print(stderr)

		#TODO - change blid assumption

		sublime.status_message("unmatched braces problem")

		#set global flag

		

		flag = 1

		return

	view.replace(edit, region, output.decode("utf-8"))

	




def dirSetup():

	packageDir=sublime.packages_path()

	libDir=os.path.join('CPrettify','lib')

	fDir=os.path.join(packageDir,libDir)

	bPath = os.path.join(fDir,'uncrustify.exe')

	print(bPath)

	return bPath


#etempargs
#debugging and initial version
def tArgs():
	
	#return "-c ben.cfg --no-backup abc.c";
	return  "-l c -o"

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

	def run(self, edit, **args):

		global flag
		
		#process settings, configurations

		init(self.view)

		if not userFoldercheck():

			print('No user File Detected')

			global user_config

			user_config = False

		else:

			user_config = True

		#setup directories and variables
		#generating folder path

		#doc reference future chnages to api

		#"https://www.sublimetext.com/docs/3/api_reference.html#sublime.View"
		
		if(sublime.View.substr is ''):

			sublime.status_message("This is empty!!!")

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
		
		#checking the file name

		exp = self.view.file_name()

		extension = os.path.splitext(exp)[-1].lower()
		
		if extension != ".c":
		
			sublime.status_message("This is not a c program.. save the file in .c extension")
		
			return


		execute_(self.view,edit,sublime.Region(0,self.view.size()))

		if flag is 0:

			sublime.status_message("Done.. Foramting")



class CprettifyOnlySelectionCommand(sublime_plugin.TextCommand):

	def run(self, edit, **args):
		
		exp = self.view.file_name()

		#for settings

		init(self.view)

		if not userFoldercheck():

			print('No user File Detected')


		#pattern = re.compile('c$')

		#print(bool(pattern.match(exp)))
		
		#re takes up unnecessary resources

		#alternative
		extension = os.path.splitext(exp)[-1].lower()
		
		if extension != ".c":
		
			sublime.status_message("This is not a c program.. save the file in .c extension")
		
			return

		for region in self.view.sel():

			#view can be empty
			#some views is and some view are not 

			#Don't run.. Stop execution 
			
			#process non empty views

			if sublime.Region.empty(region):

				sublime.status_message("Nothing Selected")

				return

			execute_(self.view,edit,region)

		#check flag before going further

		if flag is 0:

			sublime.status_message("Done.. Foramting")




class CprettifyRestoreConfigCommand(sublime_plugin.TextCommand):


	def run(self, edit):

		init(self.view)

		restore_config()


