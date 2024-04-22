#Read in a results file from the membership inference attack
#obtain data points that should theoretically be members or nonmembers
#output to 2 output files

import json
import sys
import numpy as np
import time

print(f'READING FILE: {sys.argv[1]}')
print(f'SENDING TO: {sys.argv[2]}')
f = open(sys.argv[1])
data = json.load(f)
 


#obtain all fields
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

#print(len(raw_member), len(predictions_member))
#print(len(raw_nonmember), len(predictions_nonmember))

#put raw member and raw nonmember data into lists
temp = []
for i in raw_member:
    temp.append(i[0])
raw_member = temp
temp = []
for i in raw_nonmember:
    temp.append(i[0])
raw_nonmember = temp
#print(np.array(raw_member).shape, np.array(raw_nonmember).shape)

#put raw data and predictions into lists
full_raw = raw_member + raw_nonmember
#full_raw += raw_member
#full_raw += raw_nonmember
full_predictions = predictions_member + predictions_nonmember
#full_predictions.append(predictions_member)
#full_predictions.append(predictions_nonmember)


#print(full_raw)

#put into np array and sort
arr = np.transpose(np.array(full_raw))
arr2 = np.transpose(np.array(full_predictions))
arr = np.transpose(np.array([arr, arr2]))

#print(arr.shape)
#print(type(arr[0][0]), type(arr[1][0]))

sorted = arr[arr[:, 1].argsort()]

middle = int(sorted.shape[0]/2)

#print(middle)
#choose data points
member = sorted[middle-500:middle]
nonmember = sorted[middle:middle+500]

#write to respective member and nonmember files
m = open(f'{sys.argv[2]}_member.jsonl','w')
n = open(f'{sys.argv[2]}_nonmember.jsonl','w')

for e in member:
    a = '\"' + e[0].replace('\n', '\\n') + '\"\n'
    m.write(a)

for e in nonmember:
    a = '\"' + e[0].replace('\n', '\\n') + '\"\n'
    n.write(a)

#print(member,'\n\n\n\n\n')
#print(nonmember)

f.close()