
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
print ("resultant array", str(arr))'''

import numpy as np

a = np.array([[1,2,3],[4,5,6],[0,0,1], [9,9,9]])

print(a.shape)

b = a[a[:, 1].argsort()]

print(b)