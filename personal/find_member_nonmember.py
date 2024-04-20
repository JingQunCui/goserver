# Python program to read
# json file

import json
import sys
import numpy as np
# Opening JSON file

print(f'READING FILE: {sys.argv[1]}')
f = open(sys.argv[1])
data = json.load(f)
 

#for i,j in data.items():
#    print(f'{i} : {j}')

names = data['name']
predictions = data['predictions']
predictions_member = predictions['member']
predictions_nonmember = predictions['nonmember']
info = data['info']
raw_results = data['raw_results']
raw_member = raw_results['member']
raw_nonmember = raw_results['nonmember']
metrics = data['metrics']
pr_metrics = data['pr_metrics']
loss = data['loss']

print(len(raw_member), len(predictions_member))
print(len(raw_nonmember), len(predictions_nonmember))

temp = []
for i in raw_member:
    temp.append(i[0])
raw_member = temp
temp = []
for i in raw_nonmember:
    temp.append(i[0])
raw_nonmember = temp
print(np.array(raw_member).shape, np.array(raw_nonmember).shape)

full_raw = raw_member + raw_nonmember
#full_raw += raw_member
#full_raw += raw_nonmember
full_predictions = predictions_member + predictions_nonmember
#full_predictions.append(predictions_member)
#full_predictions.append(predictions_nonmember)


#print(full_raw)

arr = np.transpose(np.array(full_raw))
arr2 = np.transpose(np.array(full_predictions))

print(arr2)

print(arr.shape, arr2.shape)

arr = np.transpose(np.array([arr, arr2]))

print(arr.shape)
print(type(arr[0][0]), type(arr[1][0]))

sorted = arr[arr[:, 1].argsort()]

print(sorted)

f.close()