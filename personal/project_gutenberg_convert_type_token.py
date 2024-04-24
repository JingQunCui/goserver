import time
import sys
import nltk

#take in a file filename, send to outfile, ignore text up until start token

filename = sys.argv[1]
outfile = sys.argv[2]
start = sys.argv[3]


found_start = False
s = ''

fileList = ["10039-0.txt", "23108-0.txt", '23727-0.txt',"10000-0.txt", "10140-0.txt", '31111-0.txt', 
            '30-0.txt', '29247-0.txt', '29261-0.txt']

count = 0
for f in fileList:
    file = open(f, 'r', errors='ignore')
    
    for line in file:
        count += 1
        if found_start:
            s += line.replace('\n',' ').replace('\"', "").replace('\\', ' ')
        else:
            if start in line:
                found_start = True
    file.close()
nltk.download('punkt')


# Tokenize the paragraph into sentences

sentences = nltk.sent_tokenize(s)

sorted_sentences = sorted(sentences, key=len)

sparse = open(outfile + '_sparse.txt', 'w')
dense = open(outfile + '_dense.txt', 'w')

sparse_vals = []
dense_vals = []

for s in sorted_sentences:
    
    if len(s) < 50:
        continue

    a = s.split()
    words = []

    for x in a:
        if x not in words:
            words.append(x)

    type_token = float(len(words))/float(len(s.split()))
    #print(type_token)
    '''
    print(len(words[0]))
    print(len(s.split()))
    print(words)
    print(a)

    print('\n\n\n\n')
    '''
    #print(words)
    #time.sleep(5)
    if s[0] == '[' or len(s) < 50 or type_token > 0.8:
        continue
    else:
        
        sparse_vals.append(type_token)
        sparse.write(s + '\n')

for s in sorted_sentences:
    if len(s) < 50:
        continue

    a = s.split()
    words = []
    for x in a:
        if x not in words:
            words.append(x)


    type_token = float(len(words))/float(len(s.split()))
    
    if s[0] == '[' or len(s) < 50 or type_token < 0.95:
        continue
    else:
        dense_vals.append(type_token)
        dense.write(s + '\n')


print(f'num sparse: {len(sparse_vals)}\nsparse avg: {sum(sparse_vals)/len(sparse_vals)}')
print(f'num dense: {len(dense_vals)}\ndense avg: {sum(dense_vals)/len(dense_vals)}')


#print(next(iter(ds)))