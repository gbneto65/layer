# setup parameters 
"""
######################################################################################
# layer performance - comparison tool
# stochastick approach
# Python 
# Version - 0.3 beta - improvements - change the performance during prefixed periods (disease outbreak simulation)
# github gbneto65 
##########
"""
# excel file name with layers genetics performance data
import os
import winsound
import git


working_directory = os.getcwd()


software_title = 'Layer Performance Calculator'

excel_file = 'layers_dta.xlsx' 
excel_col_import = 'A:N'  # coluns to import from the excel file
csv_file_name = 'layers_dta.csv'
#csv_file_name = ''



dec = 2 # n decimals - used in function round_np

""" define the percentil of the reports %"""
low = int(25)
med = int(50)
high = int(75)

def soft_version():
	repo = git.Repo(search_parent_directories=True)
	soft_version = repo.head.object.hexsha
	return soft_version[:7]

# sound error function - for alerting

def sound_error():
	sd1 = [1500,300]  # frequency, time mseg.
	sd2 = [2500, 300]
	winsound.Beep(sd1[0],sd1[1])
	winsound.Beep(sd2[0],sd2[1])
	return 

def intro_text(module):
	print('#####################################################')
	print(f'# {software_title}   -   Module : {module}  #')
	print(f'# Git Version (SHA)  -    {soft_version()}  #')
	print('#####################################################')

# take the version from GIT (SHA) - 7 first characters


