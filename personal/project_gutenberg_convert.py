from datasets import load_dataset
import time
ds = load_dataset("manu/project_gutenberg", split="fr", streaming=True)

d = list(iter(ds))
#print(d)

f = open('hello_bro.txt', 'w')

for i in d:
    #print(i)
    print(i.keys())
    print(len(i.values()))
    time.sleep(100)
    f.write(i)

f.close()

#print(next(iter(ds)))