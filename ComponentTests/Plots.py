'''
Created on Sep 10, 2015

@author: ammarbahman

Note: you need to have all the test results CSV files executed before run this file.
It will update all the plots based on the latest results from the CSV file.

'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec

#Experimental Results
T_env = np.array([125,115,105,95,85,75])
m_dot_exp = np.array([0.0447,0.0366,0.0349,0.0379,0.0315,0.0335])
capacity_exp = np.array([5578,5014,5150,5814,5133,5649])
total_power_exp = np.array([4296,3857,3530,3329,2852,2654])
compressor_power_exp = np.array([3049,2591,2252,2030,1779,1582])
COPS_exp = np.array([1.298,1.300,1.459,1.746,1.800,2.129])
#Import data from CSV file
data1 = csv2rec('results/Cycle_Test#1.csv',delimiter=',')
data2 = csv2rec('results/Cycle_Test#2.csv',delimiter=',')
data3 = csv2rec('results/Cycle_Test#3.csv',delimiter=',')
data4 = csv2rec('results/Cycle_Test#4.csv',delimiter=',')
data5 = csv2rec('results/Cycle_Test#5.csv',delimiter=',')
data6 = csv2rec('results/Cycle_Test#6.csv',delimiter=',')
#Arrange data in Numpy array for the 6 different tests
m_dot = np.array([data1[2][14],data2[2][14],data3[2][14],data4[2][14],data5[2][14],data6[2][14]])
capacity = np.array([data1[2][11],data2[2][11],data3[2][11],data4[2][11],data5[2][11],data6[2][11]])
total_power = np.array([data1[2][12],data2[2][12],data3[2][12],data4[2][12],data5[2][12],data6[2][12]])
compressor_power = np.array([data1[2][13],data2[2][13],data3[2][13],data4[2][13],data5[2][13],data6[2][13]])
COPS =np.array([data1[2][10],data2[2][10],data3[2][10],data4[2][10],data5[2][10],data6[2][10]])
#to convert string array to integer array
m_dot = m_dot.astype(np.float)
capacity = capacity.astype(np.float)
total_power = total_power.astype(np.float)
compressor_power = compressor_power.astype(np.float)
COPS = COPS.astype(np.float)
#plots
#Plot mass flow rate comparison
plt.plot(T_env,m_dot_exp,'-ob',label='Experimental')
plt.plot(T_env,m_dot,'--or',label='Model')
plt.ylim(0.02,0.05)
plt.xlim(70,130)
plt.legend(loc='best',fancybox=False)
plt.xlabel('$T_{env}$ $(\degree F)$')
plt.ylabel('$\dot m$ $(kg/s)$')
plt.title('Mass flowrate Comparison')
plt.savefig('images/comparison_massflow.pdf')
plt.show()
#Plot Capacity comparison
plt.plot(T_env,capacity_exp,'-ob',label='Experimental')
plt.plot(T_env,capacity,'--or',label='Model')
plt.ylim(4000,7000)
plt.xlim(70,130)
plt.legend(loc='best',fancybox=False)
plt.xlabel('$T_{env}$ $(\degree F)$')
plt.ylabel('$\dot Q$ $(W)$')
plt.title('Capacity Comparison')
plt.savefig('images/comparison_capacity.pdf')
plt.show()
#Plot total power comparison
plt.plot(T_env,total_power_exp,'-ob',label='Experimental')
plt.plot(T_env,total_power,'--or',label='Model')
plt.ylim(2000,5000)
plt.xlim(70,130)
plt.legend(loc='best',fancybox=False)
plt.xlabel('$T_{env}$ $(\degree F)$')
plt.ylabel('$\dot E_t$ $(W)$')
plt.title('Total Power Comparison')
plt.savefig('images/comparison_total_power.pdf')
plt.show()
#Plot compressor power comparison
plt.plot(T_env,compressor_power_exp,'-ob',label='Experimental')
plt.plot(T_env,compressor_power,'--or',label='Model')
plt.ylim(1000,3500)
plt.xlim(70,130)
plt.legend(loc='best',fancybox=False)
plt.xlabel('$T_{env}$ $(\degree F)$')
plt.ylabel('$\dot W$ $(W)$')
plt.title('Compressor Power Comparison')
plt.savefig('images/comparison_compressor_power.pdf')
plt.show()
#Plot COPS comparison
plt.plot(T_env,COPS_exp,'-ob',label='Experimental')
plt.plot(T_env,COPS,'--or',label='Model')
plt.ylim(1,2.4)
plt.xlim(70,130)
plt.legend(loc='best',fancybox=False)
plt.xlabel('$T_{env}$ $(\degree F)$')
plt.ylabel('$COP_{sys}$')
plt.title('System COP Comparison')
plt.savefig('images/comparison_COPS.pdf')
plt.show()
#Combine
fig = plt.figure(1, figsize=(10, 10), dpi=100)
for i, gtype in enumerate(['Mass', 'Capacity', 'Power', 'Compressor', 'COPS']):
    ax = plt.subplot(3, 2, i+1)
    if gtype.startswith('Mass'):
        plt.plot(T_env,m_dot_exp,'-ob',label='Experimental')
        plt.errorbar(T_env,m_dot_exp, yerr=0.1*m_dot_exp)
        plt.plot(T_env,m_dot,'--or',label='Model')
        plt.ylim(0.02,0.05)
        plt.xlim(70,130)
        plt.legend(loc='best',fancybox=False)
        plt.xlabel('$T_{env}$ $(\degree F)$')
        plt.ylabel('$\dot m$ $(kg/s)$')
        plt.title('Mass flowrate Comparison')
    if gtype.startswith('Capacity'):
        plt.plot(T_env,capacity_exp,'-ob',label='Experimental')
        plt.plot(T_env,capacity,'--or',label='Model')
        plt.ylim(4000,7000)
        plt.xlim(70,130)
        plt.legend(loc='best',fancybox=False)
        plt.xlabel('$T_{env}$ $(\degree F)$')
        plt.ylabel('$\dot Q$ $(W)$')
        plt.title('Capacity Comparison')
    if gtype.startswith('Power'):
        plt.plot(T_env,total_power_exp,'-ob',label='Experimental')
        plt.plot(T_env,total_power,'--or',label='Model')
        plt.ylim(2000,5000)
        plt.xlim(70,130)
        plt.legend(loc='best',fancybox=False)
        plt.xlabel('$T_{env}$ $(\degree F)$')
        plt.ylabel('$\dot E_t$ $(W)$')
        plt.title('Total Power Comparison')
    if gtype.startswith('Compressor'):
        plt.plot(T_env,compressor_power_exp,'-ob',label='Experimental')
        plt.plot(T_env,compressor_power,'--or',label='Model')
        plt.ylim(1000,3500)
        plt.xlim(70,130)
        plt.legend(loc='best',fancybox=False)
        plt.xlabel('$T_{env}$ $(\degree F)$')
        plt.ylabel('$\dot W$ $(W)$')
        plt.title('Compressor Power Comparison')
    if gtype.startswith('COPS'):
        plt.plot(T_env,COPS_exp,'-ob',label='Experimental')
        plt.plot(T_env,COPS,'--or',label='Model')
        plt.ylim(1,2.4)
        plt.xlim(70,130)
        plt.legend(loc='best',fancybox=False)
        plt.xlabel('$T_{env}$ $(\degree F)$')
        plt.ylabel('$COP_{sys}$')
        plt.title('System COP Comparison')
fig.set_tight_layout(True)
plt.savefig('images/comined_comparison.pdf')
plt.show()