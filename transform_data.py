import time
import sys
from pandas import DataFrame, read_csv
import pandas as pd #api to read csv files


#convert data in csv file to -1, 0, 1 to be able to find maximum sum contiguous subsequence which will give the highest percentage subsequence
#the encoding is
#A and T to 1
#G and C to -1
#N to 0

encoded = []
with open('Exemple_sequence_t.txt') as seq:
	while True:
		c = seq.read(1)
		if not c:
			print("End of File")
			break
		elif (c == 'A') or (c == 'T') or (c == 'a') or (c == 't'):
			encoded.append(1)
		elif (c == 'G') or (c == 'C') or (c == 'g') or (c == 'c'):
			encoded.append(-1)
		elif (c == 'N') or (c == 'n'):
			encoded.append(0)
		else:
			print("Error: transform_data.py unexpected letter type when encoding", c)

print(encoded[2])

#find starting and ending indices of the largest contiguous sum subsequence

max_ending_here = max_so_far = encoded[0]
begin_max = 0
end_max = 1
i = 0
for x in encoded[1:]:
	i = i + 1
	max_ending_here = max(x, max_ending_here + x)
	if max_ending_here == x:
		begin_max = i
	max_so_far = max(max_so_far, max_ending_here)
	if max_so_far == max_ending_here:
		end_max = i
print("sum", max_so_far, "beginning", begin_max, "ending", end_max)

#current result: sum 75917 beginning 7014 ending 1035718
