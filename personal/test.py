
import os


#print(x)

#from datasets import load_dataset

#dataset = load_dataset("iamgroot42/mimir", 'c4')
#dataset = load_dataset('iamgroot42/mimir', 'arxiv')
#dataset = load_dataset("iamgroot42/mimir", "pile_cc", split="ngram_7_0.2")


#print(dataset)

#print(os.environ.get('MIMIR_CACHE_PATH', None))
#print(os.environ)

'''
import numpy as np
 
ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])
 
# Array to be added as column
column_to_be_added = np.array([[1], [2], [3]])
 
# Adding column to array using append() method
arr = np.concatenate([ini_array, column_to_be_added], axis=1)
 
print(arr.shape)
# printing result
print ("resultant array", str(arr))

import numpy as np

a = np.array([[1,2,3],[4,5,6],[0,0,1], [9,9,9]])

print(a.shape)

b = a[a[:, 1].argsort()]

print(b)'''




'''

s = 'a a a a a a a a a a a a a a'
a = s.split()
words = []

# traverse for all elements
for x in a:
    # check if exists in words or not
    if x not in words:
        words.append(x)
# print list
for x in words:
    print(x)
 
type_token = float(len(words[0]))/float(len(s.split()))
print(s)
print(words[0])
print(a)
print(type_token)

'''


# importing required modules
import argparse
 
# create a parser object
parser = argparse.ArgumentParser(description = "An addition program")
 
# add argument
parser.add_argument("add", nargs = '*', metavar = "num", type = int, 
                     help = "All the numbers separated by spaces will be added.")
 
# parse the arguments from standard input
args = parser.parse_args()
 
# check if add argument has any input data.
# If it has, then print sum of the given numbers
if len(args.add) != 0:
    print(sum(args.add))

