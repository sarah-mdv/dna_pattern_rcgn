'''
    Data parser for reading and identifying dna sequences in the genome

    Author Sarah Moy de Vitry
'''
from __future__ import division, print_function

import numpy as np
import pandas as pd #api to read csv files
import data_parser_support as support
import os
import argparse
import math

parser = argparse.ArgumentParser(description="identify matching sequences between snippets")

parser.add_argument("--sequence", required=True, help="Full path to the file containing the sequence to be found")
parser.add_argument("--outdir", required=True, help="Full path to the file containing the sequence to be found")

args = parser.parse_args()

find_seq = args.sequence
out_dir = args.outdir

df = support.readSequence(find_seq,out_dir)

print(df)
