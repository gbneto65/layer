######################################################################################33
# Setup of charts
cost_color_1 =['r','b','r'] # line color of cost charts 1 
earn_color_1 =['r','b','r'] # line color of earnings charts 1
delta_color_1 =['r','b','r'] # line color of delta charts 1


fontsize_label_1 =10
fontsize_title_1 =11
fontsize_x_axis_1 =10
fontsize_y_axis_1 =10
fontsize_legend_1 =8
fontsize_annot_1 =6
fontsize_copyright =8

fontstyle_label_1 ='normal'  # normal italic oblique
fontstyle_title_1 ='normal'
fontstyle_x_axis_1 ='normal'
fontstyle_y_axis_1 ='normal'
fontstyle_legend_1 ='normal'
fontstyle_annot_1 ='normal'
fontstyle_copyright ='normal'

dpi_charts = 200 # resolution of the graph files


###########################################################################################
# Stackplot parameters -  # colors of the stackplots (1 - pullet, 2 - feed, 3 - feed aditiv)
stackplot_colors = [\
             "#a6b2d7",\
		     "#b6c2d7",\
 		     "#006de1",\
             '#c6d2d7',\
             '#d6e2d7',
             '#e6f2d7'\
              ]

stackplot_labels =[\
                   'Pullet',\
                   'Feed',\
                   'Aditiv',\
                   'Vet',\
                   'Labor',\
                   'other'\
                   ] # labels of the stackplots

stack_title_1 = 'Main cumulative variable costs / layer / age'
stack_ylabel_1 = "Cum. cost / layer / age (LC)"
stack_xlabel_1 = "weeks of age"

stack_title2_1 = 'Operating result / layer / age (LC)'
stack_ylabel2_1 = "costs & earnings / layer / age (LC)"
stack_xlabel2_1 = "weeks of age"