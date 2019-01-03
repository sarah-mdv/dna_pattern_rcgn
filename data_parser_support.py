'''
    Support functions for data parsing
    Author Sarah Moy de Vitry
'''

from __future__ import division, print_function
import os
import argparse
import math
import numpy as np
import pandas as pd #api to read csv files

from pandas import DataFrame, read_csv

# Reads txt file and returns the content in a numpy array
def readSequence(filename,outdir):

    temp_filename = formatFile(filename, outdir)

    df_seq = pd.read_csv(temp_filename, sep = '\t', names= ['bases'])

    return df_seq

# Formats file so that each base is separated into individual cells
def formatFile(filename, outdir):
    content = ''

    #write entire content to string
    with open(filename, 'r') as f:

        for line in f:

            if not line[0] == '>':

                content += line.rstrip()

    temp_filename = "{}/{}".format(outdir, "temp_formatted.txt")

    # print content in new file with tab separation
    with open(temp_filename, 'w') as out_f:

        for el in content:

            out_f.write(el + '\n')

    return temp_filename
