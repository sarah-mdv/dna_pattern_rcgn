'''
    Data parser for reading and identifying dna sequences in the genome

    Author Sarah Moy de Vitry
'''
from __future__ import division, print_function
import os
import argparse
import math
import numpy as np
import pandas as pd #api to read csv files
import matplotlib.pyplot as plt #api for intermediary feedback
import data_parser_support as support

from pandas import DataFrame, read_csv

parser = argparse.ArgumentParser(description="identify matching sequences between snippets")

parser.add_argument("--sequence", required=True, help="Full ath to the file containing the sequence to be found")

parser.add_argument("--genome", required=True, help = "Full path to the file containing the genome to be scanned")

parser.add_argument("--accuracy", required=True, help = "Minimum percentage of accuracy between the sequences given and found")

args = parser.parse_args()

genome_seq = args.genome

find_seq = args.sequence

min_percentage = args.accuracy

if (min_percentage < 0 || min_percentage > 100):
    sys.exit(0)

min_percentage = min_percentage / 100


Location = r'/home/moyde/Documents/Projects/dna_pattern_rcgn/MAR-x-29-publication.csv'
df = pd.read_csv(Location)
