# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:54:39 2020
######################################################################################
# layer performance - comparison tool
# stochastick approach
# Python 
# Version - 0.3 beta - improvements - change the performance during prefixed periods (disease outbreak simulation)
# github gbneto65 
# parameters file - input variables

#####################################################################################
"""

genetic1 = 1  # 1 - Hyline W36 - White / 2 - to be defined


n_layers = 50000 # to be used to calculated birds / cost
prod_week_analysis = 100   # usually 100 - define the production week for cost / earnings analysis - usually 100 wks (varies from 18 - 100)
n_repl = 200 # idealy at least 3000

wks_per_month = 4.348 # avg weeks in a month
wks_per_year = 52.1429 # avg weeks per year
egg_std_weight = 62/1000  # std egg weight - used to calculated egg mass price


#############################################################################################


# adjustment on feed consuption if needed - input 1 and 'f' for no adjustment

feed_cons_adj_1 =[.013  , # % of incremet of feed consuption (if below input negative values - Ex: -.1 (-10%)) ,
                  .015 ,     # this value should be multiplied with feed_cons_layer_day,
                  .014 ,     # this value should be multiplied with feed_cons_layer_day,
                  't']

# adjustment on mortality if needed - input 1 and 'f' for no adjustment
mort_adj_week_1 = [.05 ,     # % of increase of mortality rate in relation to std values 
                   .07 ,
                   .06 ,
                   't'] # min, max., mp, distribution  

# laying rate adjustment
laying_rate_adj_1 = [-.1,                  # % above or below the std values defined by genetic co. 
                     -.2,                  # to decrease the standard laying rate by 10% - input -0.1
                     -.15,
                     'f'] # min, max., mp, distribution  

pullet_cost_1  = [5, 7, 6, 't']  # min, max., mp, distribution


# feed costs
feed_cost_ton_1 = [800, 1300, 900, 't'] # min, max., mp, distribution

# aditive cost 
aditiv_cost_ton_1 = [9, 15, 10, 'f']


# consider the cost of vet services + treatments per month - n_layer should be right  inputed
vetcost_layer_week_1 = [1200 /n_layers/wks_per_month,
                        1600 /n_layers/wks_per_month,
                        1300 /n_layers/wks_per_month,
                        't'] # min, max., mp, distribution


labor_cost_layer_week_1 = [2400 / n_layers / wks_per_month,           # input the MONTLY cost of labor / n_layers (IMPORTANT)) 
                           3000 /n_layers / wks_per_month,              # DO NOT consider VET costs (see vet services costs)
                           2600 /n_layers / wks_per_month,
                           't'] # min, max., mp, distribution

other_cost_layer_week_1 = [2000 /n_layers/wks_per_month,           # input the MONTLY other costs / n_layers (IMPORTANT)) 
                           2500 /n_layers/wks_per_month,
                           2200 /n_layers/wks_per_month,
                           'u'] # min, max., mp, distribution

depreci_cost_layer_week_1 = [1000 / n_layers / wks_per_year,           # input the ANUAL amortization and depreciation per N_LAYERS
                             2000 /n_layers / wks_per_year,                
                             1500 /n_layers / wks_per_year,
                             'f'] # min, max., mp, distribution 

losses_cost_layer_week_1 = [1000 / n_layers / wks_per_year,           # input other losses in an ANUAL basis per N_LAYERS
                            2000 /n_layers / wks_per_year,                
                            1500 /n_layers /wks_per_year,
                            'f']  # min, max., mp, distribution 

egg_box_size = 360  # egg price is per XXX units (ex: 360, 100)
 
egg_price_un_std = [70 / (egg_box_size*egg_std_weight), # price / box considering the egg_box_size 
                    100 / (egg_box_size*egg_std_weight),
                    120  / (egg_box_size*egg_std_weight),
                    'f']  # min, max., mp

egg_price_perc_dif_brown = [3/100,   # market price diference for brown eggs % 
                                5/100,   # max 5%
                                4/100,   # most probably
                                'f']     # distribution
other_earn_layer_week_1 = [1000 / n_layers / wks_per_month,           # input the MONTLY earnings of others (manure sales, et) / n_layers (IMPORTANT)) 
                           2000 /n_layers / wks_per_month,            # 
                           1500 /n_layers / wks_per_month,
                           'f'] # min, max., mp, distribution


###############################################################################


if genetic1 == 1 : # Hyline W36 - White
    group1 = ['HY W36', 'white', 'hy_w36'] # define the genetic or group name and egg color (usefull to calculate the egg price)
elif genetic ==2 :
    pass
elif genetic ==3 :
    pass
else:
    print('genetic not defined' * 20)
    error(i)
    sys.exit()
