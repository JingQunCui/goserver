import sys
import time
#Reads in enron files from a particular folder and formats it into jsonl
#also limits line length to 1500 characters

print(f'READING FROM FOLDER: {sys.argv[1]}')
print(f'SENDING TO FILE: {sys.argv[2]}')
out = open(sys.argv[2], "a")

#enron location: "../../cache/enron_mail_20150507/maildir" - add one of the names and subdirectories to parse

count = 0
for i in range(1,3000):

    try:
        s = '\"'
        filepath = f"{sys.argv[1]}/{i}"
        #print(f"{filepath}")
        f = open(f"{sys.argv[1]}/{i}", "r")

        for line in f:
            s += line.replace('\n','').replace('\"', "").replace('\\', ' ') + '\\n'
        
        if len(s) > 1500:
            if s[1499] == '\\':
                s = s[:1499]
            else:
                s = s[:1500]
        s += '\"\n'
        #time.sleep(100)
        out.write(s)
        f.close()
        count += 1
    except IOError as e:
    # print("Couldn't open or write to file (%s)." % e) # python 2
        #print(f'ended on loop {i}')
        continue
print(f'found {count} items')



out.close