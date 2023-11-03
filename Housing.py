from turtle import color
import numpy as np1 
# add numpy libraries
fileR = open('housing.csv', 'r')
# read data
lineR = fileR.readlines()
# read lin by line 9 => 10 
Str2 = ""
# keep counter
c1 = 0 
for lineR:
# iterate data line by line
c1 = c1 + 1;
# increment counter
str2 = lineR.split(",");
# split string
  
# list holds data
xdata = []
ydata = []

# read line by line
str1 = ""
i = 0
c = 0

# iterate data line by line
for lineS in lineR:
  c = c + 1 
  # increment counter
  str1 = lineS.split(",")
  # split string
  xdata.apprend(str1[1])
  # append data in x
  ydata.append(str1[0])
  # append data in y
  if c == c1:
    break
  
#display data
print("=====Data Analysis=====\n")
print("Total number of columns", len(str1))
print("Total number of rows", c1)

#imported plot library
import matplotlib.pyplot as plt1 

# x and y labels
x_label = ""
y_label = ""
title = ""
_, ax = plt1.subplots()

# Plot the data
print("====== Line analysis and scatter analysis on housing data ======\n");

ax.plot(xdata, ydata, lw = 2, color = '539caf', alpha = 1);

# labeling with x axis and y axis
ax.set_title(title);
ax.set_xlabel(x_label);
ax.set_ylabel(y_label);

# x and y labels
x_label1 = ""
y_label1 = ""
title1 = ""
color1 = "r"
yscale_log1 = False

_, ax = plt1.subplots()

#scatter plot
ax.scatter(xdata, ydata, s = 15, color = color1, alpha = 0.75);

#plot data
if yscale_log1 == True:
  ax.set_yscale('log')
  
# Label axis
ax.set_title(title1)

ax.set_xlabel(x_label1)

ax.set_ylabel(y_label1)  
 
  
