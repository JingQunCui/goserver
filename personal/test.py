
import os


#print(x)

#from datasets import load_dataset

#dataset = load_dataset("iamgroot42/mimir", 'c4')
#dataset = load_dataset('iamgroot42/mimir', 'arxiv')
#dataset = load_dataset("iamgroot42/mimir", "pile_cc", split="ngram_7_0.2")


#print(dataset)

print(os.environ.get('MIMIR_CACHE_PATH', None))
print(os.environ)
