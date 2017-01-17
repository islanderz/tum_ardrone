#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import os, os.path
import csv
from operator import add

print "Processing ",

imuFile = open("logPTAM.txt", 'rt');
#kfFile = open("logFilter.txt", 'rt');
#kfData = [];
imuData = [];
imuDataVel = [];

#Reading the IMU and KF files
imuReader = csv.reader(imuFile, delimiter=" ");
#kfReader = csv.reader(kfFile, delimiter=" ");
 
imuCount = 0;
#kfCount = 0;

#Extracting first 1899 for nav and 1800 for vid
for row in imuReader: 
   roundedtime = str(row[1])[:5];
   imuData.append(int(roundedtime));
   #imuData.append(row[1]);
   imuDataVel.append(row[2]);
   #print(row[0]);
   imuCount+=1;
   if(imuCount >= 5000):
     break;
#for row in kfReader:
   #if (row[14] != -1):
   #kfData.append(row[14]);
#   kfData.append(row[14]);
   #print(row[5]);
#   kfCount+=1;
#   if(kfCount >= 800):
#     break;
imuFile.close();
#kfFIle.close();

idx = 0;

plt.figure(1);
#plt.subplot(211)
plt.ylabel('Pose x(metric)')
plt.xlabel('Time (ms)')
axes = plt.gca()
#axes.set_ylim([0.34,0.38])
 	
plt.plot(imuData,imuDataVel)

#plt.figure(1)
#plt.subplot(211)
#plt.plot(imuData, kfData)

plt.show()
