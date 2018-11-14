# -*- coding: utf-8 -*-
"""
NU FP Skeleton

Created on Tue Nov 13 07:37:42 2018

@author: annaa
"""

# import required packages
import csv
import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
import matplotlib as plt

root = tk.Tk()
root.withdraw()

#lists the types of files one can select
my_filetypes = [('all files', '.*'), ('text files', '.txt'), ('csv files', '.csv')]

# Ask the user to select a one or more file names.
openfile = filedialog.askopenfilenames(initialdir=os.getcwd(),
                                       title="Please select one or more files:",
                                       filetypes=my_filetypes)

with open(%s openfile, newline='') as csvfile:
  selectedfile = csv.reader(csvfile, delimiter=',')
for row in selectedfile:
  print(', '.join(row))