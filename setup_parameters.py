# setup parameters 
"""
Created on Sat Oct 17 13:54:39 2020
######################################################################################
# layer performance - comparison tool
# stochastick approach
# Python 
# Version - 0.3 beta - improvements - change the performance during prefixed periods (disease outbreak simulation)
# github gbneto65 
##########
"""

# path_excel = r'C:\Users\schwa\Layer-Performance-Project\layers_dta.xlsx' # folder path of the excel layer performance data
dec = 2 # n decimals - used in function round_np

""" define the percentil of the reports %"""
low = int(25)
med = int(50)
high = int(75)

# sound parameters - for alerting
sd1 = [1500,300]  # frequency, time mseg.
sd2 = [2500, 500]



