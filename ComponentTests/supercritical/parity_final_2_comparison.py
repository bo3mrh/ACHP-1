import matplotlib,os
#matplotlib.use('GTKAgg')
import sys, os
#from FileIO import prep_csv2rec as prep
from matplotlib.mlab import csv2rec

import pylab
import numpy as np
import shutil
from scipy import polyval, polyfit
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('classic')
#mpl.style.use('Elsevier.mplstyle')
#===============================================================================
# Latex render
#===============================================================================
#mpl.use('pgf')

def figsize(scale):
    fig_width_pt = 469.755                          # Get this from LaTeX using \the\textwidth
    inches_per_pt = 1.0/72.27                       # Convert pt to inch
    golden_mean = (np.sqrt(5.0)-1.0)/2.0            # Aesthetic ratio (you could change this)
    fig_width = fig_width_pt*inches_per_pt*scale    # width in inches
    fig_height = fig_width*golden_mean              # height in inches
    fig_size = [fig_width,fig_height]
    return fig_size

pgf_with_latex = {                      # setup matplotlib to use latex for output
"pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
"text.usetex": True,                # use LaTeX to write all text
"font.family": "serif",
"font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
"font.sans-serif": [],
"font.monospace": [],
"axes.labelsize": 12,               # LaTeX default is 10pt font.
"font.size": 12,
"legend.fontsize": 10,               # Make the legend/label fonts a little smaller
"legend.labelspacing":0.2,
"xtick.labelsize": 10,
"ytick.labelsize": 10,
"figure.figsize": figsize(0.9),     # default fig size of 0.9 textwidth
"pgf.preamble": [
r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
        ]
    }
mpl.rcParams.update(pgf_with_latex)
#===============================================================================
# END of Latex render
#===============================================================================


def rmse(predictions, targets):
    '''
    Root Mean Square Error
    '''
    n = len(predictions)
    RMSE = np.linalg.norm(predictions - targets) / np.sqrt(n) / np.mean(targets) * 100
    return RMSE

def mape(y_pred, y_true):  #maps==mean_absolute_percentage_error
    '''
    Mean Absolute Percentage Error
    '''
    MAPE = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return MAPE


    ######RMSE#######
    #rmse_mass = rmse(yuanpei_m_dot_inj_norm,m_dot_inj_norm_exp)
    #print("rmse_mass error is: " + str(rmse_mass) + " %")
    ######MAPE######
    # mape_mass = mape(yuanpei_m_dot_inj_norm,m_dot_inj_norm_exp)
    # print("mape_mass error is: " + str(mape_mass) + " %")
    
    

 
#########################
##### heating load #######
#########################
#import data from excel file
df = pd.read_excel('Table.xlsx',header=0) #file name
#assign axes
y1 = df['Q'][1:]
y2 = df['Q_new_FV'][1:].str[0:-1].str.split(' ', expand=True).astype(float)[0]
x1 = df['Q_siml'][1:]
x2 = df['Q_exp'][1:]
#c2 = df_dar['T_evap[i]'][1:]
s = 40  # size of points

fig, ax = plt.subplots(figsize=(5.5,5.5))
#im = ax.scatter(x2, y1, c='r', s=s, cmap=plt.cm.jet, marker='s',lw=0.2, alpha =1.0,label='predicted vs experimental'+' (MAE = {:0.01f}\%'.format(mape(y1,x2))+', RMSE = {:0.01f}\%)'.format(rmse(y1,x2)))
#im = ax.scatter(x2, x1, c='k', s=s, cmap=plt.cm.jet, marker='o',lw=0.2, alpha =1.0,label='FIM simulation vs experimental'+' (MAE = {:0.01f}\%'.format(mape(x1,x2))+', RMSE = {:0.01f}\%)'.format(rmse(x1,x2)))
im = ax.scatter(x2, y2, c='b', s=s, cmap=plt.cm.jet, marker='^',lw=0.2, alpha =1.0,label='predicted (new) vs experimental'+' (MAE = {:0.01f}\%'.format(mape(y2,x2))+', RMSE = {:0.01f}\%)'.format(rmse(y2,x2)))
# Add a colorbar
#cbar = plt.colorbar(im, ax=ax)
# set the color limits
#im.set_clim(245, 290)
#cbar.ax.set_ylabel('Evaporation temperature [K]')
#ax.text(0.8,0.95,'Markersize (speed) {:0.0f} Hz'.format(s),ha='center',va='center',transform = ax.transAxes,fontsize = 8)
  
#error axes
w=0.1 #Error
ax_min = 4
ax_max = 20 #x and y-axes max scale tick
upp_txt = (ax_min+ax_max) / 2 #location of upper error text on plot -- adjust the number to adjust the location
low_txt = (ax_min+ax_max) / 1.7 #location of lower error text on plot -- adjust the number to adjust the location
ax.plot(np.r_[0,ax_max],np.r_[0,ax_max],'k-',lw=1)
ax.plot(np.r_[0,ax_max],np.r_[0,ax_max*(1-w)],'k-.',lw=1)
ax.plot(np.r_[0,ax_max],np.r_[0,ax_max*(1+w)],'k-.',lw=1)
ax.text(low_txt-0.002,low_txt*(1-w),'$-${:0.0f}\%'.format(w*100),ha='left',va='top')
ax.text(upp_txt-0.002,upp_txt*(1+w),'+{:0.0f}\%'.format(w*100),ha='right',va='bottom')
leg=ax.legend(loc='upper left',scatterpoints=1)
frame  = leg.get_frame()  
frame.set_linewidth(0.5)
ax.set_xlim((ax_min,ax_max))
ax.set_ylim((ax_min,ax_max))
plt.ylabel(r'$\dot Q_{pred}$ [kW]')
plt.xlabel(r'$\dot Q_{exp}$ [kW]')
plt.tight_layout()       
plt.savefig('parity_heating_load_ACFV.pdf')
plt.show()
plt.close()
     
#########################
##### Refrigerant temperature #######
#########################
#import data from excel file
df = pd.read_excel('Table.xlsx',header=0) #file name
#assign axes
y1 = df['Ref out temp'][1:]
y2 = df['Q_new_FV'][1:].str[0:-1].str.split(' ', expand=True).astype(float)[1]
x1 = df['Tested Refrigerant Outlet Temp'][1:]
x2 = df['Simulated Refrigerant Outlet Temp'][1:]
#c2 = df_dar['T_evap[i]'][1:]
s = 40  # size of points
  
fig, ax = plt.subplots(figsize=(5.5,5.5))
#im = ax.scatter(x1, y1, c='r', s=s, cmap=plt.cm.jet, marker='s',lw=0.2, alpha =1.0,label='predicted vs experimental'+' (MAE = {:0.01f}\%'.format(mape(y1,x1))+', RMSE = {:0.01f}\%)'.format(rmse(y1,x1)))
#im = ax.scatter(x1, x2, c='k', s=s, cmap=plt.cm.jet, marker='o',lw=0.2, alpha =1.0,label='FIM simulation vs experimental'+' (MAE = {:0.01f}\%'.format(mape(x2,x1))+', RMSE = {:0.01f}\%)'.format(rmse(x2,x1)))
im = ax.scatter(x1, y2, c='b', s=s, cmap=plt.cm.jet, marker='^',lw=0.2, alpha =1.0,label='predicted (new) vs experimental'+' (MAE = {:0.01f}\%'.format(mape(y2,x1))+', RMSE = {:0.01f}\%)'.format(rmse(y2,x1)))
# Add a colorbar
#cbar = plt.colorbar(im, ax=ax)
# set the color limits
#im.set_clim(245, 290)
#cbar.ax.set_ylabel('Evaporation temperature [K]')
#ax.text(0.8,0.95,'Markersize (speed) {:0.0f} Hz'.format(s),ha='center',va='center',transform = ax.transAxes,fontsize = 8)
  
#error axes
w=3 #Error
ax_min = 20
ax_max = 60 #x and y-axes max scale tick
upp_txt = (ax_min+ax_max) / 2 #location of upper error text on plot -- adjust the number to adjust the location
low_txt = (ax_min+ax_max) / 1.7 #location of lower error text on plot -- adjust the number to adjust the location
ax.plot(np.r_[0,ax_max],np.r_[0,ax_max],'k-',lw=1)
ax.plot(np.r_[0,ax_max],np.r_[-w,ax_max-w],'k--',lw=1)
ax.plot(np.r_[0,ax_max],np.r_[w,ax_max+w],'k--',lw=1)
ax.text(low_txt-0.002,low_txt-w,'$-${:0.0f}K'.format(w),ha='left',va='top')
ax.text(upp_txt-0.002,upp_txt+w,'+{:0.0f}K'.format(w),ha='right',va='bottom')
leg=ax.legend(loc='upper left',scatterpoints=1)
frame  = leg.get_frame()  
frame.set_linewidth(0.5)
ax.set_xlim((ax_min,ax_max))
ax.set_ylim((ax_min,ax_max))
plt.ylabel(r'$T_{r,pred}$ [{\textdegree}C]')
plt.xlabel(r'$T_{r,exp}$ [{\textdegree}C]')
plt.tight_layout()       
plt.savefig('parity_refrigerant_temp_ACFV.pdf')
plt.show()
plt.close()
