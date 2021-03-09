#Layer Project V2 
#setup parameters 

import os
import winsound
import datetime
from app_version import get_versions
# input the setup parameters below
software_title = 'Layer Performance Calculator'


excel_file_name = 'layers_dta.xlsx'
excel_col_import = 'A:N'  # coluns to import from the excel file
working_directory = os.getcwd() # get current working path


# define automatically the csv filename basef on excel filename
csv_file_name = excel_file_name.split('.', -1)[0]
csv_file_name = (f'{csv_file_name}.csv')


# get the SHA repository version - software version
def soft_version():
	#__version__ = get_versions('software_title')
	#soft_version = __version__
	#print(soft_version)
	# take the version from GIT (SHA) - 7 first characters
	soft_version= 'to be implemented'
	return soft_version


soft_version = soft_version()

dec = 3 # n decimals - used in function round_np

""" define the percentil of the reports %"""
low = int(25)
med = int(50)
high = int(75)

def sound_error():
	sd1 = [1500,300]  # frequency, time mseg.
	sd2 = [2500, 300]
	winsound.Beep(sd1[0],sd1[1])
	winsound.Beep(sd2[0],sd2[1])
	return 

def error_exit():
	print('\n\n****** Error ******\n')
	print('********Aborting script ******\n\n')
	exit


def intro_text(module):
	print('\n############################################################################')
	print(f' {software_title}   -   Module : {module} ')
	print(f' Git Version (SHA)  -    {soft_version} ')
	print('##############################################################################\n')

# takes the date and time 
def datetime_now():
	return datetime.datetime.now()

