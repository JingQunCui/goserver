import time
import sys
import nltk

#take in a file filename, send to outfile, ignore text up until start token

filename = sys.argv[1]
outfile = sys.argv[2]
start = sys.argv[3]


found_start = False
s = ''

fileList = ["10039-0.txt", "23108-0.txt", '23727-0.txt',"10000-0.txt", "10140-0.txt", '31111-0.txt']

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

short = open(outfile + '_short.txt', 'w')
long = open(outfile + '_long.txt', 'w')

count1 = 0
count2 = 0
for s in sorted_sentences:

    if s[0] == '[' or len(s) < 50 or len(s) > 150:
        continue
    short.write(s + '\n')
    count1+=1

for s in sorted_sentences:
    if s[0] == '[' or len(s) < 150:
        continue
    long.write(s + '\n')
    count2+=1

print(f'num short: {count1}')
print(f'num long: {count2}')

