import sys


filepath = sys.argv[1]
outfile = sys.argv[2]
#print(f"{filepath}")
f = open(f"{sys.argv[1]}", "r")
out = open(f'{sys.argv[2]}.jsonl', 'w')

s = ''
count = 0
for line in f:
    s = '\"' + line.replace('\n','').replace('\"', "").replace('\\', ' ') + '\\n'

    #limit length
    if len(s) > 1500:
        if s[1499] == '\\':
            s = s[:1499]
        else:
            s = s[:1500]
    s += '\"\n'
    out.write(s)

    count += 1
    if count > 3000:
        break
#time.sleep(100)
print(f'made {count} samples')

f.close()
