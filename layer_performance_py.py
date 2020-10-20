# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:38:16 2020
"""

######################################################################################
# layer performance - comparison tool
# stochastick approach
# Python 
# Version - 0.3 beta - improvements - change the performance during prefixed periods (disease outbreak simulation)
# github gbneto65

#####################################################################################

import pandas as pd
import numpy as np
import locale
import matplotlib.pyplot as plt
import winsound
import sys
from setup_parameters import *  # extra file with setup variables
from setup_charts_parameters import *  # extra file with setup variables
from parameters import *
import os


def rnd_same(min, mp, max, distr) :  # generate random numbers and create a np. array with production_wks (83) , number of replicates (n_repl)

    if distr.lower() == 't' : # triangular distribution
        return np.random.triangular(min, mp, max, (production_wks,n_repl))
    if distr.lower() == 'u' :  # uniform distribution
        return np.random.uniform(min, max, (production_wks,n_repl))
    if distr.lower() == 'f' : # fixed value
        return np.full((production_wks,n_repl),mp, dtype=float )

def transp_and_tile(param) :  # transpose initial array and create a np. array with production_wks (83) , number of replicates (n_repl) with equal values (no randomic)
     transp = np.transpose(param)
     return  np.tile(transp,(1, n_repl))

def curr(var) :                  # change for the local currency
    return locale.currency(var)

def round_np(var) :
    return np.around(var,decimals=dec)

def percent (var, percent) :    # calculation of the percentil 
    return np.percentile(var, percent, axis=1)

def annot(): # annoteted breakeven on the chart
    plt.annotate("Breakeven:\n {} wks".format(zero_crossings_delta_1[0]),
      fontsize = fontsize_annot_1,
      xy=(zero_crossings_delta_1, 0), xycoords='data',
      xytext=((xmax-zero_crossings_delta_1[0])/5 + zero_crossings_delta_1[0],
             (0 - ymin)/3*-1),
      textcoords='data',
      arrowprops=dict(arrowstyle="->",
      connectionstyle="arc3")
      )
def verif_entry (min, max, mp, distrib) :
    if  distrib != 'f' :
        if mp <= min or mp >= max :
            print('*** Verifiy data input ***\n' * 20)
            winsound.Beep(sd1[0],sd1[1])
            winsound.Beep(sd2[0],sd2[1])
            sys.exit()
        elif min >= max :
            print('*** Verifiy data input ***\n' * 20)
            winsound.Beep(sd1[0],sd1[1])
            winsound.Beep(sd2[0],sd2[1])
            sys.exit()
    else :
        pass

def alert_file() :
        print('*** cannot found data file in the working directory ***\n' * 20)
        winsound.Beep(sd1[0],sd1[1])
        winsound.Beep(sd2[0],sd2[1])
        winsound.Beep(sd1[0],sd1[1])
        sys.exit()


# part of the Layers performance project
#


#########################################################################################
""" label according percentis - ideal for confidence intervals plots"""
label_1 = ['Percentil {} %'.format(low),'Percentil {} %'.format(med),'Percentil {} %'.format(high)] 

""" linewidth for line charts - [0] - low conf. limit [1] - median and [2] high conf. limit """ 
line_with_1=[1, 1, 1] 

""" line style  for line charts - [0] - low conf. limit [1] - median and [2] high conf. limit """
line_sty_1 = ['dotted', 'solid', 'dotted']
""" title of the charts """
title1 = 'Operational return until {} weeks of age - {}  {}'.format(prod_week_analysis,group1[0],group1[1])



# output parameters
locale.setlocale(locale.LC_ALL, 'en_US') # define the currency symbol 'en_US'; fr_FR; es_ES; pt_PT; pl_PL;

"""
LANGUAGES = {
    'bg_BG': 'Bulgarian',
    'cs_CZ': 'Czech',
    'da_DK': 'Danish',
    'de_DE': 'German',
    'el_GR': 'Greek',
    'en_US': 'English',
    'es_ES': 'Spanish',
    'et_EE': 'Estonian',
    'fi_FI': 'Finnish',
    'fr_FR': 'French',
    'hr_HR': 'Croatian',
    'hu_HU': 'Hungarian',
    'it_IT': 'Italian',
    'lt_LT': 'Lithuanian',
    'lv_LV': 'Latvian',
    'nl_NL': 'Dutch',
    'no_NO': 'Norwegian',
    'pl_PL': 'Polish',
    'pt_PT': 'Portuguese',
    'ro_RO': 'Romanian',
    'ru_RU': 'Russian',
    'sk_SK': 'Slovak',
    'sl_SI': 'Slovenian',
    'sv_SE': 'Swedish',
    'tr_TR': 'Turkish',
    'zh_CN': 'Chinese',
}
"""

##########################################################################################
"""
if prod_week_analysis < 18 or prod_week_analysis >100 :
    prod_week_alalysis = 100
    print('ERROR')
"""    

# get the current working path
working_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.isfile("layers_dta.xlsx") :
        alert_file()


# import database from excel - see parameters.py file
data_hy_w36 = pd.read_excel(working_path + "/" + 'layers_dta.xlsx' ,sheet_name= group1[2]) # sheet name is defined in parameter.py 
print(data_hy_w36.columns)

# convert to numpy
data_1 = data_hy_w36[['feed_intake_min','feed_intake_max', 'hen_week_mort_cumulative', 'hen_day_egg_cum_min', 'hen_day_egg_cum_max', 'egg_weight_avg' ]].values  # input database and convert to np array
production_wks = data_1.shape[0] # define the number of rows in database

# define the row location in the array (to get results)
row_anal = prod_week_analysis - 18 # 18 is the week of beging the production 

index_error=False

##########################################################################################

############### Zootecnical Parameters ################################################

# adjustment on feed consuption if needed - input 1 and 'f' for no adjustment

verif_entry(feed_cons_adj_1[0],feed_cons_adj_1[1],feed_cons_adj_1[2],feed_cons_adj_1[3]) # verify entry
feed_rnd_adj_1 = rnd_same(feed_cons_adj_1[0],
                          feed_cons_adj_1[2],
                          feed_cons_adj_1[1],
                          feed_cons_adj_1[3])  # generate random numbers 
                         

# adjustment on mortality if needed - input 1 and 'f' for no adjustment

verif_entry(mort_adj_week_1[0],mort_adj_week_1[1],mort_adj_week_1[2],mort_adj_week_1[3]) # verify entry
mort_rnd_adj_week_1 = rnd_same(mort_adj_week_1[0],
                               mort_adj_week_1[2],
                               mort_adj_week_1[1],
                               mort_adj_week_1[3])  # generate random numbers 


# adjust laying rate
verif_entry(laying_rate_adj_1[0],laying_rate_adj_1[1],laying_rate_adj_1[2],laying_rate_adj_1[3]) # verify entry
laying_rnd_adj_1 = rnd_same(laying_rate_adj_1[0],
                            laying_rate_adj_1[2],
                            laying_rate_adj_1[1],
                            laying_rate_adj_1[3])  # generate random numbers 

###############  Operating Expenses #################################################### 
# pullet costs at 18 weeks of age
verif_entry(pullet_cost_1[0],pullet_cost_1[1],pullet_cost_1[2],pullet_cost_1[3]) # verify entry
pullet_rnd_cost_1 = rnd_same(pullet_cost_1[0],
                               pullet_cost_1[2],
                               pullet_cost_1[1],
                               pullet_cost_1[3])  # generate random numbers - per GRAMS od Feed

# feed costs
verif_entry(feed_cost_ton_1[0],feed_cost_ton_1[1],feed_cost_ton_1[2],feed_cost_ton_1[3]) # verify entry
feed_rnd_cost_g_1 = rnd_same(feed_cost_ton_1[0]/1000000,
                               feed_cost_ton_1[2]/1000000,
                               feed_cost_ton_1[1]/1000000,
                               feed_cost_ton_1[3])  # generate random numbers - per GRAMS od Feed

#print(feed_rnd_cost_g_1)


# aditive cost 
verif_entry(aditiv_cost_ton_1[0],aditiv_cost_ton_1[1],aditiv_cost_ton_1[2],aditiv_cost_ton_1[3]) # verify entry
aditiv_rnd_cost_g_1 = rnd_same(aditiv_cost_ton_1[0]/1000000,
                               aditiv_cost_ton_1[2]/1000000,
                               aditiv_cost_ton_1[1]/1000000,
                               aditiv_cost_ton_1[3])  # generate random numbers - adtitive price / per GRAMS of Feed


# consider the cost of vet services + treatments per month - n_layer should be right  inputed
verif_entry(vetcost_layer_week_1[0],vetcost_layer_week_1[1],vetcost_layer_week_1[2],vetcost_layer_week_1[3]) # verify entry
vetcost_rnd_week_1 = rnd_same(vetcost_layer_week_1[0],
                               vetcost_layer_week_1[2],
                               vetcost_layer_week_1[1],
                               vetcost_layer_week_1[3])  # generate random numbers - vet cost / layer / week
vetcost_rnd_cum_week_1 = np.cumsum(vetcost_rnd_week_1, dtype = float, axis=0) # ////  cummulative vet costs

# Labor costs
verif_entry(labor_cost_layer_week_1[0],labor_cost_layer_week_1[1],labor_cost_layer_week_1[2],labor_cost_layer_week_1[3]) # verify
laborcost_rnd_week_1 = rnd_same(labor_cost_layer_week_1[0],
                               labor_cost_layer_week_1[2],
                               labor_cost_layer_week_1[1],
                               labor_cost_layer_week_1[3])
laborcost_rnd_cum_week_1 = np.cumsum(laborcost_rnd_week_1, dtype = float, axis=0) # ///// cumulative labor costs

# consider the other costs  of vet services + treatments per month - n_layer should be right  inputed

verif_entry(other_cost_layer_week_1[0],other_cost_layer_week_1[1],other_cost_layer_week_1[2],other_cost_layer_week_1[3]) # verify
othercost_rnd_week_1 = rnd_same(other_cost_layer_week_1[0],         
                               other_cost_layer_week_1[2],
                               other_cost_layer_week_1[1],
                               other_cost_layer_week_1[3])
othercost_rnd_cum_week_1 = np.cumsum(othercost_rnd_week_1, dtype = float, axis=0)  # ////  cummulative other costs

############ fixed costs ################################################

verif_entry(depreci_cost_layer_week_1[0],depreci_cost_layer_week_1[1],depreci_cost_layer_week_1[2],depreci_cost_layer_week_1[3]) # verify
deprecicost_rnd_layer_week_1 = rnd_same(depreci_cost_layer_week_1[0],         
                               depreci_cost_layer_week_1[2],
                               depreci_cost_layer_week_1[1],
                               depreci_cost_layer_week_1[3])
deprecicost_rnd_cum_layer_week_1 = np.cumsum(deprecicost_rnd_layer_week_1, dtype = float, axis=0) # cumulativo depreciation costs  //////
######################### other losses 

verif_entry(losses_cost_layer_week_1[0],losses_cost_layer_week_1[1],losses_cost_layer_week_1[2],losses_cost_layer_week_1[3]) # verify
losses_rnd_layer_week_1 = rnd_same(losses_cost_layer_week_1[0],         
                                   losses_cost_layer_week_1[2],
                                   losses_cost_layer_week_1[1],
                                   losses_cost_layer_week_1[3])
losses_rnd_cum_layer_week_1 = np.cumsum(losses_rnd_layer_week_1, dtype = float, axis=0)  # cumulative other eventual losses /////

################ EARNINGS  ####################################################################
# earnings - egg sales + others

# Egg_price_std (white egg - L) 
                  # standard egg weight - varies among countries
verif_entry(egg_price_un_std[0],egg_price_un_std[1],egg_price_un_std[2],egg_price_un_std[3]) # verify
egg_mass_rnd_price_kg = rnd_same(  egg_price_un_std[0],         
                                   egg_price_un_std[2],
                                   egg_price_un_std[1],
                                   egg_price_un_std[3])
# price diference for Brown Egg - same size as white
if group1[1].lower() == 'brown' : 
   egg_price_rnd_adj_brown = rnd_same(egg_price_perc_dif_brown[0],         
                                       egg_price_perc_dif_brown[2],
                                       egg_price_perc_dif_brown[1],
                                       egg_price_perc_dif_brown[3])
   egg_mass_rnd_price_kg = egg_mass_rnd_price_kg * (1 + egg_price_rnd_adj_brown)  # adjust egg price if egg = brown



verif_entry(other_earn_layer_week_1[0],other_earn_layer_week_1[1],other_earn_layer_week_1[2],other_earn_layer_week_1[3]) # verify
other_earn_rnd_1 = rnd_same(other_earn_layer_week_1[0],         
                                       other_earn_layer_week_1[2],
                                       other_earn_layer_week_1[1],
                                       other_earn_layer_week_1[3])
other_earn_rnd_cum_1 = np.cumsum(other_earn_rnd_1, dtype = float, axis=0) # cumulative others earnings ////

##########################################################################3

""" implementation of the parcial impact of disease oubreak in the flock
     user should input:
         - the period of the disease (initial to final - weeks of production)
         - the predicted impact (%) on:
                 - Feed consumption / layer
                 - mortality (%) - it will affect the with consuption too
                 - Vet costs 
                 - Laying rate (%)
                 

variables to be affected:
    mort_cum_week_1 --> 
    
    vetcost_rnd_cum_week_1 --> vet costs 
    egg_mass_1 -> consider laying rate

Still not implanted in this version
"""

affect_week_init = 50   # input the initial week of problem
affect_week_final = 80 # input the final week of problem


if affect_week_init < 18 or  affect_week_final > prod_week_analysis  : # ' verify input data '
    affect_week_init = 0
    affect_week_final = 0

mort_affect_week_perc = 0  # excess of mortality - 
cons_affect_week_perc = 0  # reduction of consumption of feed during disease period
vetcost_affect_week_perc = 0 # increase of vet costs / week during disease period 
laying_affect_week_perc = 0 # reduction of laying egg rate during disease period

################################################################################################
# calculation of Costs
# mortality rate / week
mort_cum_rate_week_1 = [data_1[:, 2] / 100]                     # mortaliy 
mort_cum_week_1 = transp_and_tile(mort_cum_rate_week_1)
mort_cum_week_1 = mort_cum_week_1 * (1 + mort_rnd_adj_week_1)
loop = False


############## if affected by correction (diseases, etc)
# mortality


for i in range (affect_week_init - 18,  affect_week_final - 18) :
     loop = True
     
     mort_cum_week_1[i] = mort_cum_week_1[i]*(1-mort_affect_week_perc)

# mortality
     
     


# pullet costs


# pullet_rnd_cost_1 # //////


# Feed costs

feed_cons_layer_week_1 = [(data_1[:,0] + data_1[:,1])/2 * 7]          # avg feed intake / day * 7 days
feed_cons_1 = transp_and_tile(feed_cons_layer_week_1)         # create a array with 83 rows and n replicates colums 
feed_cons_layer_week_1 = feed_cons_1 * (1 + feed_rnd_adj_1)   # adjust the feed consuption according "feed_cons_adj_1" - Extra database
feed_cons_layer_week_1 = feed_cons_layer_week_1 * (1-mort_cum_week_1)


############## if affected by correction (diseases, etc)
#feed consuption
for i in range (affect_week_init - 18,  affect_week_final - 18) :
     feed_cons_layer_week_1[i] = feed_cons_layer_week_1[i]*(1-cons_affect_week_perc)

##########################################

feed_cons_cum_week_1 = np.cumsum(feed_cons_layer_week_1, dtype = float, axis=0)  # cumulative feed intake / layer / week (already adjusted by mortality and adj_factor)


#feed_cum_layer_1 = np.sum(feed_cons_1[:,0])                  # total feed consption / period without adjustments
#feed_cum_layer_adj_1 = np.sum(feed_cons_layer_week_1[:,0])    # total feed consption / period with adjustments

feed_cost_cum_layer_week_1_no_add = feed_cons_cum_week_1 * feed_rnd_cost_g_1  # calculation of cumulative cost of feed / week ($$$) wihtout feed aditive //// feed cost no aditiv

aditiv_cum_cost_layer_week_1 = aditiv_rnd_cost_g_1 * feed_cons_cum_week_1 # calculation of cumulative  cost of feed adtitive / week ($$$)  /////// cum feed adtiv cost


#feed_cost_layer_week_1 = feed_cost_layer_week_1_no_add + aditiv_cum_cost_layer_week_1  # //////////// cum_feed_cost
#print(feed_add_cum_cost_layer_week_1)
#print(aditiv_rnd_cost_g_1)
# egg production / week / cumm


n_egg_cum_prod_week_1 = [(data_1[:,4] + data_1[:,3])/2]       # cummulative egg number / week by average pf min & max (row represent weeks)
n_egg_cum_prod_1 = transp_and_tile(n_egg_cum_prod_week_1)     #  # create a array with 83 rows and n replicates colums 
n_egg_cum_adj_1 = n_egg_cum_prod_1 * (1 + laying_rnd_adj_1)   # adjust the according according laying_rnd_adj

# individual egg weight 
egg_un_weight_kg = transp_and_tile([data_1[:,5]/1000])  # individual egg weight in kg


# egg_mass calculation - considering egg_weight + mortality rate
egg_mass_1 = n_egg_cum_adj_1 * egg_un_weight_kg * (1 - mort_cum_week_1)   # egg mass adjusted my mortality and egg weight



############## if affected by correction (diseases, etc)
# laying rate
for i in range (affect_week_init - 18,  affect_week_final - 18) :
     egg_mass_1[i] = egg_mass_1[i]*(1-laying_affect_week_perc)

##########################################
# earnings with egg sales
egg_earn_cum_week_1 = egg_mass_1 * egg_mass_rnd_price_kg   # ///// earnings from egg sales - correted by mortality and other adj
#print(egg_mass_1)
#print(egg_earn_cum_week_1)
#print(feed_cum_layer_adj_1)
# other earnings 
# other_earn_rnd_1     //// eventual earnings except from eggs 

total_earn_cum_week_1 = egg_earn_cum_week_1 + other_earn_rnd_cum_1 # /// total earnings

############################################ costs ###############################################
########### Cost of Goods Sold #################

#print(pullet_rnd_cost_1) # ok - no cum
#print(feed_cost_cum_layer_week_1_no_add) #ok
#print(aditiv_cum_cost_layer_week_1) #ok
#print(vetcost_rnd_cum_week_1) # ok
#print(laborcost_rnd_cum_week_1) # ok
#print(othercost_rnd_cum_week_1) # ok

total_var_costs_1 = pullet_rnd_cost_1 + \
                    feed_cost_cum_layer_week_1_no_add + \
                    aditiv_cum_cost_layer_week_1 + \
                    vetcost_rnd_cum_week_1 + \
                    laborcost_rnd_cum_week_1 + \
                    othercost_rnd_cum_week_1 # total variable costs 

total_fix_costs_1 = deprecicost_rnd_cum_layer_week_1 + losses_rnd_cum_layer_week_1 # total fixed costs
total_costs_1 = total_var_costs_1 + total_fix_costs_1        # total costs //////

################################ costs participation of each parameter ####################
# variable costs vs total var costs
# pullet costs

pullet_cost_median_1 = percent(pullet_rnd_cost_1, med)  # median
pullet_cost_q1_1 = percent(pullet_rnd_cost_1, low)      # 1 quartil
pullet_cost_q3_1 = percent(pullet_rnd_cost_1, high)      # 3 quratil

pullet_var_cost_rate_1 = pullet_rnd_cost_1 / total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
pullet_tot_cost_rate_1 = pullet_rnd_cost_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

pullet_perc_cost_median_1 = percent(pullet_tot_cost_rate_1, med)
pullet_perc_cost_q1_1 = percent(pullet_tot_cost_rate_1, low)
pullet_perc_cost_q3_1 = percent(pullet_tot_cost_rate_1, high)

##############################
# feed_costs

feed_cost_cum_median_week_1_no_add = percent(feed_cost_cum_layer_week_1_no_add, med)
feed_cost_cum_q1_week_1_no_add = percent(feed_cost_cum_layer_week_1_no_add, low)
feed_cost_cum_q3_week_1_no_add = percent(feed_cost_cum_layer_week_1_no_add, high)

feed_noad_var_cost_rate_1 = feed_cost_cum_layer_week_1_no_add / total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
feed_noad_tot_cost_rate_1 = feed_cost_cum_layer_week_1_no_add / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

feed_perc_cost_cum_median_week_1_no_add = percent(feed_noad_tot_cost_rate_1, med)
feed_perc_cost_cum_q1_week_1_no_add = percent(feed_noad_tot_cost_rate_1, low)
feed_perc_cost_cum_q3_week_1_no_add = percent(feed_noad_tot_cost_rate_1, high)

##############################
# feed_adtitive_costs

aditiv_cum_cost_median_layer_week_1 = percent(aditiv_cum_cost_layer_week_1, med)
aditiv_cum_cost_q1_layer_week_1 = percent(aditiv_cum_cost_layer_week_1, low)
aditiv_cum_cost_q3_layer_week_1 = percent(aditiv_cum_cost_layer_week_1, high)

aditiv_cum_cost_var_rate_1 = aditiv_cum_cost_layer_week_1 / total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
aditiv_cum_cost_tot_rate_1 = aditiv_cum_cost_layer_week_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

aditiv_perc_cost_cum_median_week_1 = percent(aditiv_cum_cost_tot_rate_1, med)
aditiv_perc_cost_cum_q1_week_1 = percent(aditiv_cum_cost_tot_rate_1, low)
aditiv_perc_cost_cum_q3_week_1 = percent(aditiv_cum_cost_tot_rate_1, high)

#############################
# vet costs

vetcost_cum_cost_median_layer_week_1 = percent(vetcost_rnd_cum_week_1, med)
vetcost_cum_cost_q1_layer_week_1 = percent(vetcost_rnd_cum_week_1, low)
vetcost_cum_cost_q3_layer_week_1 = percent(vetcost_rnd_cum_week_1, high)

vetcost_cum_cost_var_rate_1 = vetcost_rnd_cum_week_1 / total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
vetcost_cum_cost_tot_rate_1 = vetcost_rnd_cum_week_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

vetcost_perc_cost_cum_median_week_1 = percent(vetcost_cum_cost_tot_rate_1, med)
vetcost_perc_cost_cum_q1_week_1 = percent(vetcost_cum_cost_tot_rate_1, low)
vetcost_perc_cost_cum_q3_week_1 = percent(vetcost_cum_cost_tot_rate_1, high)

#############################
# labor costs
laborcost_rnd_cum_week_1

labor_cum_cost_median_layer_week_1 = percent(laborcost_rnd_cum_week_1, med)
labor_cum_cost_q1_layer_week_1 = percent(laborcost_rnd_cum_week_1, low)
labor_cum_cost_q3_layer_week_1 = percent(laborcost_rnd_cum_week_1, high)

labor_cum_cost_var_rate_1 = laborcost_rnd_cum_week_1/ total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
labor_cum_cost_tot_rate_1 = laborcost_rnd_cum_week_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

labor_perc_cost_cum_median_week_1 = percent(labor_cum_cost_tot_rate_1, med)
labor_perc_cost_cum_q1_week_1 = percent(labor_cum_cost_tot_rate_1, low)
labor_perc_cost_cum_q3_week_1 = percent(labor_cum_cost_tot_rate_1, high)

############################3
# other costs

other_cum_cost_median_layer_week_1 = percent(othercost_rnd_cum_week_1, med)
other_cum_cost_q1_layer_week_1 = percent(othercost_rnd_cum_week_1, low)
other_cum_cost_q3_layer_week_1 = percent(othercost_rnd_cum_week_1, high)

other_cum_cost_var_rate_1 = othercost_rnd_cum_week_1/ total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
other_cum_cost_tot_rate_1 = othercost_rnd_cum_week_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

other_perc_cost_cum_median_week_1 = percent(labor_cum_cost_tot_rate_1, med)
other_perc_cost_cum_q1_week_1 = percent(labor_cum_cost_tot_rate_1, low)
other_perc_cost_cum_q3_week_1 = percent(labor_cum_cost_tot_rate_1, high)

###############################
deprecicost_rnd_cum_layer_week_1

deprec_cum_cost_median_layer_week_1 = percent(deprecicost_rnd_cum_layer_week_1, med)
deprec_cum_cost_q1_layer_week_1 = percent(deprecicost_rnd_cum_layer_week_1, low)
deprec_cum_cost_q3_layer_week_1 = percent(deprecicost_rnd_cum_layer_week_1, high)

deprec_cum_cost_var_rate_1 = deprecicost_rnd_cum_layer_week_1/ total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
deprec_cum_cost_tot_rate_1 = deprecicost_rnd_cum_layer_week_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

deprec_perc_cost_cum_median_week_1 = percent(deprec_cum_cost_tot_rate_1, med)
deprec_perc_cost_cum_q1_week_1 = percent(deprec_cum_cost_tot_rate_1, low)
deprec_perc_cost_cum_q3_week_1 = percent(deprec_cum_cost_tot_rate_1, high)

###############################
losses_rnd_cum_layer_week_1 

losses_cum_cost_median_layer_week_1 = percent(losses_rnd_cum_layer_week_1, med)
losses_cum_cost_q1_layer_week_1 = percent(losses_rnd_cum_layer_week_1, low)
losses_cum_cost_q3_layer_week_1 = percent(losses_rnd_cum_layer_week_1, high)

losses_cum_cost_var_rate_1 = losses_rnd_cum_layer_week_1/ total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
losses_cum_cost_tot_rate_1 = losses_rnd_cum_layer_week_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

losses_perc_cost_cum_median_week_1 = percent(losses_cum_cost_tot_rate_1, med)
losses_perc_cost_cum_q1_week_1 = percent(losses_cum_cost_tot_rate_1, low)
losses_perc_cost_cum_q3_week_1 = percent(losses_cum_cost_tot_rate_1, high)

################################
# total costs
total_costs_1

total_cum_cost_median_layer_week_1 = percent(total_costs_1, med)
total_cum_cost_q1_layer_week_1 = percent(total_costs_1, low)
total_cum_cost_q3_layer_week_1 = percent(total_costs_1, high)

total_cum_cost_var_rate_1 = total_costs_1/ total_var_costs_1 * 100  # rate of pullet cost on the total variable costs (%)
total_cum_cost_tot_rate_1 = total_costs_1 / total_costs_1 * 100  # rate of pullet cost on the total variable costs (%)

total_perc_cost_cum_median_week_1 = percent(total_cum_cost_tot_rate_1, med)
total_perc_cost_cum_q1_week_1 = percent(total_cum_cost_tot_rate_1, low)
total_perc_cost_cum_q3_week_1 = percent(total_cum_cost_tot_rate_1, high)

##########################################################################################
# earnings

eggearn_cum_median_layer_week_1 = percent(egg_earn_cum_week_1, med)
eggearn_cum_q1_layer_week_1 = percent(egg_earn_cum_week_1, low)
eggearn_cum_q3_layer_week_1 = percent(egg_earn_cum_week_1, high)

eggearn_cum_tot_rate_1 = egg_earn_cum_week_1 / total_earn_cum_week_1 * 100  # rate of pullet cost on the total variable costs (%)

eggearn_perc_cum_median_week_1 = percent(eggearn_cum_tot_rate_1, med)
eggearntotal_perc_cum_q1_week_1 = percent(eggearn_cum_tot_rate_1, low)
eggearn_perc_cum_q3_week_1 = percent(eggearn_cum_tot_rate_1, high)

###################
# other earnings

otherearn_cum_median_layer_week_1 = percent(other_earn_rnd_cum_1, med)
otherearn_cum_q1_layer_week_1 = percent(other_earn_rnd_cum_1, low)
otherearn_cum_q3_layer_week_1 = percent(other_earn_rnd_cum_1, high)

otherearn_cum_tot_rate_1 = other_earn_rnd_cum_1 / total_earn_cum_week_1 * 100  # rate of pullet cost on the total variable costs (%)

otherearn_perc_cum_median_week_1 = percent(otherearn_cum_tot_rate_1, med)
otherearntotal_perc_cum_q1_week_1 = percent(otherearn_cum_tot_rate_1, low)
otherearn_perc_cum_q3_week_1 = percent(otherearn_cum_tot_rate_1, high)

####################
# total earnings
total_earn_cum_week_1

totalearn_cum_median_layer_week_1 = percent(total_earn_cum_week_1, med)
totalearn_cum_q1_layer_week_1 = percent(total_earn_cum_week_1, low)
totalearn_cum_q3_layer_week_1 = percent(total_earn_cum_week_1, high)

totalearn_cum_tot_rate_1 = total_earn_cum_week_1 / total_earn_cum_week_1 * 100  # rate of pullet cost on the total variable costs (%)

totalearn_perc_cum_median_week_1 = percent(totalearn_cum_tot_rate_1, med)
totalearntotal_perc_cum_q1_week_1 = percent(totalearn_cum_tot_rate_1, low)
totalearn_perc_cum_q3_week_1 = percent(totalearn_cum_tot_rate_1, high)

##################################################### Delta #####################
# operational Result:  earnings - total costs

delta_cum_week_1 = total_earn_cum_week_1 - total_costs_1 # operational result ////

delta_cum_median_layer_week_1 = percent(delta_cum_week_1, med)
delta_cum_q1_layer_week_1 = percent(delta_cum_week_1, low)
delta_cum_q3_layer_week_1 = percent(delta_cum_week_1, high)

delta_cum_tot_rate_1 = (total_earn_cum_week_1 - total_costs_1) / total_earn_cum_week_1 * 100  # margin ////

delta_perc_cum_median_week_1 = percent(delta_cum_tot_rate_1, med)
delta_perc_cum_q1_week_1 = percent(delta_cum_tot_rate_1, low)
delta_perc_cum_q3_week_1 = percent(delta_cum_tot_rate_1, high)

######################################################################
""" Breakeven week & max financial return week """
# breakeven - Week  var = zero_crossings_delta_1 

zero_crossings_delta_1 = np.where(np.diff(np.sign(delta_cum_median_layer_week_1)))[0] + 18 # breakeven
""" if error: index_error = true (used in charts / prints of breakeven"""
index_error = zero_crossings_delta_1.size == 0 # verify if there is no crossing of breaklines (always negative return)
    
# max financial return (X, Y) - week (delta_max_x_1) and value delta_max_y_1
delta_max_x_1 = delta_cum_median_layer_week_1.argmax() + 18 # return the week of a max financial return
delta_max_y_1 = delta_cum_median_layer_week_1[delta_cum_median_layer_week_1.argmax()] # take the value of max 

#print(zero_crossings_delta_1) 
##################################################################################
#
###################### Charts #################################

# breakeven - week
""" create the x axis for the plot - var = weeks_axis """

weeks_axis =np.linspace(18, production_wks + 18, production_wks)   # creat axis for charts (production weeks)

#min_pullet = np.amin(pullet_cost_median_1)


####################################### cost charts ################################
# setup parameters for the charts are located in "setup_charts_parameters.py"

"""           
fig, ax = plt.subplots()
ax.stackplot(weeks_axis,
             pullet_cost_median_1,
             feed_cost_cum_median_week_1_no_add,
             aditiv_cum_cost_median_layer_week_1,
             vetcost_cum_cost_median_layer_week_1,
             labor_cum_cost_median_layer_week_1,
             other_cum_cost_median_layer_week_1,
             colors = stackplot_colors,
             labels = stackplot_labels,
             alpha = 1)

ax.legend(loc='upper left',
          fontsize=fontsize_legend_1,
          )
ax.grid(alpha=.3)
ax.set_title('{}\n {} - {}'.format(stack_title_1, group1[0],group1[1]),
             fontsize= fontsize_title_1,
             )
ax.set_ylabel(stack_ylabel_1,
              fontsize=fontsize_y_axis_1,
              )
ax.set_xlabel(stack_xlabel_1,
              fontsize=fontsize_x_axis_1,
              )
# text for % of each cost parameter

ax.text(row_anal+5,
        (feed_cost_cum_median_week_1_no_add[row_anal, ]/2),
        'Feed: {} %'.format(round_np(feed_perc_cost_cum_median_week_1_no_add[row_anal,])),
        fontsize = fontsize_annot_1,
        )
ax.text(row_anal+5,
        (pullet_cost_median_1[row_anal, ]/2),
        'Pullet: {} %'.format(round_np(pullet_perc_cost_median_1[row_anal,])),
        fontsize = fontsize_annot_1,
        )

ax.text(row_anal+5,
        aditiv_cum_cost_median_layer_week_1[row_anal,]/2 +
         feed_cost_cum_median_week_1_no_add[row_anal, ] +
         pullet_cost_median_1[row_anal, ],
        'Adit. {} %'.format(round_np(aditiv_perc_cost_cum_median_week_1[row_anal,])),
        fontsize = fontsize_annot_1,
        )

ax.text(row_anal+5,
        vetcost_cum_cost_q1_layer_week_1[row_anal,]/2 +
        aditiv_cum_cost_median_layer_week_1[row_anal,] +
         feed_cost_cum_median_week_1_no_add[row_anal, ] +
         pullet_cost_median_1[row_anal, ] + 2,
        'Vet. {} %'.format(round_np(vetcost_perc_cost_cum_median_week_1[row_anal,])),
        fontsize = fontsize_annot_1,
        )
ymin, ymax = plt.ylim()
ax.vlines(row_anal+18,
          ymin,
          ymax,
          colors='#5d5d5d',
          linewidth = line_with_1,
          linestyle = line_sty_1)

ax.text(84, (ymax-ymin)*.13*-1,
        'Cost ratios at {} weeks'.format(row_anal+18),
        fontsize = fontsize_annot_1,
        alpha=.5)

plt.savefig('main_costs_by_wk.png',
            dpi=dpi_charts,
            transparent=-True,
            )
plt.show()
"""

           
fig, ax = plt.subplots()
ax.stackplot(weeks_axis,
             pullet_cost_median_1,
             feed_cost_cum_median_week_1_no_add,
             aditiv_cum_cost_median_layer_week_1,
             vetcost_cum_cost_median_layer_week_1,
             labor_cum_cost_median_layer_week_1,
             other_cum_cost_median_layer_week_1,
             colors = stackplot_colors,
             labels = stackplot_labels,
             alpha = .7)

ax.stackplot(weeks_axis,
        totalearn_cum_q1_layer_week_1,
        colors = '	#88d8b0',
        alpha=.4,
        )
"""
ax.legend(loc='upper left',
          fontsize=fontsize_legend_1,
          )
"""
ax.grid(alpha=.3)
ax.set_title('{}\n {} - {}'.format(stack_title2_1, group1[0],group1[1]),
             fontsize= fontsize_title_1,
             )
ax.set_ylabel(stack_ylabel2_1,
              fontsize=fontsize_y_axis_1,
              )
ax.set_xlabel(stack_xlabel2_1,
              fontsize=fontsize_x_axis_1,
              )
# text for % of each cost parameter

ax.text(row_anal-4,
        total_cum_cost_median_layer_week_1[row_anal,] +
        (totalearn_cum_median_layer_week_1[row_anal,] -
         total_cum_cost_median_layer_week_1[row_anal,])/2.1,
        'Operating result*: {} %'.format(round_np(delta_perc_cum_median_week_1[row_anal,])),
        fontsize = fontsize_annot_1,
        )
ax.text(row_anal-10,
        total_cum_cost_median_layer_week_1[row_anal,] +
        (totalearn_cum_median_layer_week_1[row_anal,] -
         total_cum_cost_median_layer_week_1[row_anal,])/5,
        'Earnings',
        fontsize = fontsize_annot_1+1,
        )

ax.text(row_anal-10,
        total_cum_cost_median_layer_week_1[row_anal,] / 3, 
        'Costs',
        fontsize = fontsize_annot_1+1,
        )
ymin, ymax = plt.ylim()
ax.vlines(row_anal+18,
          total_cum_cost_median_layer_week_1[row_anal,],
          totalearn_cum_median_layer_week_1[row_anal,],
          colors='#5d5d5d',
          linewidth = line_with_1,
          linestyle = line_sty_1)

ax.text(90, (ymax-ymin)*.13*-1,
        '*: at {} weeks'.format(row_anal+18),
        fontsize = fontsize_annot_1,
        alpha=.5)

plt.savefig('main_earnings_by_wk.png',
            dpi=dpi_charts,
            transparent=-True,
            )
plt.show()



###################################### operational return chart #####################
plt.plot(weeks_axis,
         delta_cum_q1_layer_week_1,
         label = label_1[0],
         color=delta_color_1[0],
         linestyle=line_sty_1[0],
         linewidth = line_with_1[0],
         alpha=.9,
         )
plt.plot(weeks_axis,
         delta_cum_median_layer_week_1,
         label = label_1[1],
         color=delta_color_1[1],
         linestyle=line_sty_1[1],
         linewidth = line_with_1[1],
         alpha=.9,
         )
plt.plot(weeks_axis,
         delta_cum_q3_layer_week_1,
         label = label_1[2],
         color=delta_color_1[2],
         linestyle=line_sty_1[2],
         linewidth = line_with_1[2],
         alpha=.9,
         )

plt.legend(loc='best',
           fontsize=fontsize_legend_1
           )
plt.xlabel("Weeks of Age",
           fontsize=fontsize_x_axis_1,
           fontstyle = fontstyle_x_axis_1)
plt.ylabel('Operational return / layer (LC)')

xmin, xmax, ymin, ymax = plt.axis()

if delta_max_x_1 >= 75 : # define coordinated for max op return (75 is the production week)
      x_fact = delta_max_x_1 - 12
      y_fact = delta_max_y_1 - ((ymax-ymin)/5)
else :
      x_fact = delta_max_x_1 + 5
      y_fact = delta_max_y_1 + ((ymax-ymin)/5)

plt.annotate("Max. return \n {} wks".format(delta_max_x_1),  # plot the max return rate week
             fontsize = fontsize_annot_1,
            
            xy=(delta_max_x_1, delta_max_y_1), xycoords='data',
            xytext=(x_fact, y_fact), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plt.hlines(0,
           18,
           100,
           linestyle = 'dotted',
           linewidth = 1,
           color = 'r',
           alpha=.5)
plt.grid(alpha=.3)
plt.title(title1,
          fontsize=fontsize_title_1,
          ) 
print(index_error)
#if index_error==False : # indexerror handling
#    annot() # if not error (put breakeven annotated)
    
# plt.annotate("Breakeven:\n {} wks".format(zero_crossings_delta_1[0]),
#      fontsize = fontsize_annot_1[0],
#      xy=(zero_crossings_delta_1, 0), xycoords='data',
#      xytext=((xmax-zero_crossings_delta_1)/5 + zero_crossings_delta_1,
#             (0 - ymin)/4*-1),
#      textcoords='data',
#      arrowprops=dict(arrowstyle="->",
#      connectionstyle="arc3")
#      )

plt.savefig('operational_return.png',
            dpi=dpi_charts,
            transparent=-True,
            )
plt.show()

######################################################################
# pie charts - Operational Costs

pie_labels = ['feed', 'aditiv', 'pullet', 'Vet', 'labor', 'others', 'deprec.', 'losses']
pie_size = [feed_perc_cost_cum_median_week_1_no_add[row_anal, ],\
            aditiv_perc_cost_cum_median_week_1[row_anal, ],\
            pullet_perc_cost_median_1[row_anal, ],\
            vetcost_perc_cost_cum_median_week_1[row_anal ,],\
            labor_perc_cost_cum_median_week_1[row_anal, ],\
            other_perc_cost_cum_median_week_1[row_anal, ],\
            deprec_perc_cost_cum_median_week_1[row_anal, ],\
            losses_perc_cost_cum_median_week_1[row_anal, ]]

pie_explode = (0, 0.2, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Aditiv')    


plt.pie(pie_size, explode=pie_explode, labels=pie_labels, autopct='%1.1f%%',
        shadow=True, startangle=0, textprops={'fontsize': 8})
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Operational expenses - {}-{} -  at {} weeks of age'.format(group1[0],group1[1],prod_week_analysis),
          fontsize=fontsize_title_1-2,
          )
plt.savefig('operational_expenses_pie.png',
            dpi=dpi_charts,
            transparent=-True,
            )
plt.show()

##################################################################################
                      
                      
print ('=' *70)
print('Operating Expenses - {}  - {}                           {} weeks of age'.format(group1[0],group1[1],prod_week_analysis))
print('-' * 70)
print('                    Q1       MD        Q3               of COOGS (MD)')
print('Pullet Cost    : {} , {}  , {}              {} %'.format(curr(pullet_cost_q1_1[row_anal,]),
                                                           curr(pullet_cost_median_1[row_anal,]),
                                                           curr(pullet_cost_q3_1[row_anal,]),
                                                           round_np(pullet_perc_cost_median_1[row_anal,])))

print('Feed costs     : {} , {}  , {}              {} %'.format(curr(feed_cost_cum_q1_week_1_no_add[row_anal,]),
                                                           curr(feed_cost_cum_median_week_1_no_add[row_anal,]),
                                                           curr(feed_cost_cum_q3_week_1_no_add[row_anal,]),
                                                           round_np(feed_perc_cost_cum_median_week_1_no_add[row_anal,])))

print('Aditiv. costs  : {} , {}  , {}                  {} %'.format(curr(aditiv_cum_cost_q1_layer_week_1[row_anal,]),
                                                           curr(aditiv_cum_cost_median_layer_week_1[row_anal,]),
                                                           curr(aditiv_cum_cost_q3_layer_week_1[row_anal,]),
                                                           round_np(aditiv_perc_cost_cum_median_week_1[row_anal,])))

print('Vet costs      : {} , {}  , {}                  {} %'.format(curr(vetcost_cum_cost_q1_layer_week_1[row_anal,]),
                                                           curr(vetcost_cum_cost_median_layer_week_1[row_anal,]),
                                                           curr(vetcost_cum_cost_q3_layer_week_1[row_anal,]),
                                                           round_np(vetcost_perc_cost_cum_median_week_1[row_anal,])))

print('Labor costs    : {} , {}  , {}                  {} %'.format(curr(labor_cum_cost_q1_layer_week_1[row_anal,]),
                                                           curr(labor_cum_cost_median_layer_week_1[row_anal,]),
                                                           curr(labor_cum_cost_q3_layer_week_1[row_anal,]),
                                                           round_np(labor_perc_cost_cum_median_week_1[row_anal,])))

print('Other costs   : {} , {}  , {}                   {} %'.format(curr(other_cum_cost_q1_layer_week_1[row_anal,]),
                                                           curr(other_cum_cost_median_layer_week_1[row_anal,]),
                                                           curr(other_cum_cost_q3_layer_week_1[row_anal,]),
                                                           round_np(other_perc_cost_cum_median_week_1[row_anal,])))

print('-' * 70)
print('Deprec. costs   : {} , {}  , {}                  {} %'.format(curr(deprec_cum_cost_q1_layer_week_1[row_anal,]),
                                                           curr(deprec_cum_cost_median_layer_week_1[row_anal,]),
                                                           curr(deprec_cum_cost_q3_layer_week_1[row_anal,]),
                                                           round_np(deprec_perc_cost_cum_median_week_1[row_anal,])))


print('Other Losses.   : {} , {}  , {}                 {} %'.format(curr(deprec_cum_cost_q1_layer_week_1[row_anal,]),
                                                           curr(deprec_cum_cost_median_layer_week_1[row_anal,]),
                                                           curr(deprec_cum_cost_q3_layer_week_1[row_anal,]),
                                                           round_np(deprec_perc_cost_cum_median_week_1[row_anal,])))
print('-' * 70)

print('Total costs      : {} , {}  , {}         {} %'.format(curr(total_cum_cost_q1_layer_week_1[row_anal,]),
                                                           curr(total_cum_cost_median_layer_week_1[row_anal,]),
                                                           curr(total_cum_cost_q3_layer_week_1[row_anal,]),
                                                           round_np(total_perc_cost_cum_median_week_1[row_anal,])))
print('-' * 70)
print()
print ('=' *70)
print(' Earnings - {}  - {}                           {} weeks of age'.format(group1[0],group1[1],prod_week_analysis))
print('-' * 70)
print('                       Q1       MD        Q3              (MD)')
print('Egg earnings        : {} , {}  , {}         {} %'.format(curr(eggearn_cum_q1_layer_week_1[row_anal,]),
                                                           curr(eggearn_cum_median_layer_week_1[row_anal,]),
                                                           curr(eggearn_cum_q3_layer_week_1[row_anal,]),
                                                           round_np(eggearn_perc_cum_median_week_1[row_anal,])))

print('other earnings      : {} , {}  , {}             {} %'.format(curr(otherearn_cum_q1_layer_week_1[row_anal,]),
                                                           curr(otherearn_cum_median_layer_week_1[row_anal,]),
                                                           curr(otherearn_cum_q3_layer_week_1[row_anal,]),
                                                           round_np(otherearn_perc_cum_median_week_1[row_anal,])))
print('-' * 70)
print('Total earnings      : {} , {}  , {}         {} %'.format(curr(totalearn_cum_q1_layer_week_1[row_anal,]),
                                                           curr(totalearn_cum_median_layer_week_1[row_anal,]),
                                                           curr(totalearn_cum_q3_layer_week_1[row_anal,]),
                                                           round_np(totalearn_perc_cum_median_week_1[row_anal,])))
print()
print('-' * 70)
print('Operational Results : {} , {}  , {}       {} %'.format(curr(delta_cum_q1_layer_week_1[row_anal,]),
                                                           curr(delta_cum_median_layer_week_1[row_anal,]),
                                                           curr(delta_cum_q3_layer_week_1[row_anal,]),
                                                           round_np(delta_perc_cum_median_week_1[row_anal,])))

print()
print('-' * 70)


print(pullet_cost_median_1.shape)
#print(pullet_var_cost_rate_1)
#print(pullet_tot_cost_rate_1)


       
                
####### non operating expenses ################################################################

#print(deprecicost_rnd_cum_layer_week_1) # ok
#print(losses_rnd_cum_layer_week_1) # ok


############### Incomes

#print(egg_earn_cum_week_1) #ok
#print(other_earn_rnd_cum_1) # ok

# total_costs_1 = pullet_rnd_cost_1 + 
#                 feed_cost_layer_week_1_no_add +
#                 aditiv_cum_cost_layer_week_1 +
#                 deprecicost_rnd_cum_layer_week_1 +
#                 losses_rnd_cum_layer_week_1



