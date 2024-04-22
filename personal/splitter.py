import sys

f = open(sys.argv[1], 'r')

l = []

for line in f:
    l.append(line)

l2 = l[:int(len(l)/2)]
#print(l2)
l3 = l[int(len(l)/2):]

s1 = open(f'{sys.argv[2]}_1.jsonl', 'w')
s2 = open(f'{sys.argv[2]}_2.jsonl', 'w')

for a in l2:
    s1.write(a)

for a in l3:
    s2.write(a)