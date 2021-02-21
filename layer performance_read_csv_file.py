# # Layers performance project - branch V2
# module: read CSV file - performance database from genetics 
# 
import pandas as pd
from setup_parameters_v2 import intro_text, csv_file_name, working_directory, sound_error, working_directory

intro_text('Main')
print(f'\nworking Path : {working_directory}')

# read database - CSV file
try:
	dta_df = pd.read_csv(csv_file_name)
	print('CSV File read sucessfully\n')
except:
	print(f'Error - Verify if .CSV file exist at {working_directory}\n')
	sound_error()




print(dta_df.head(5))



