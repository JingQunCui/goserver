# MIMIR -altered

The mimir section of this paper is a modified version of [this repository](https://github.com/iamgroot42/mimir). All credit goes to them for the attacks, model, and training data. 

## Installation

First install the python dependencies in the main root
```
pip install -r requirements.txt
```

Then, install the main package from [here](https://github.com/iamgroot42/mimir).

```
pip install -e .
```

The following environment variables must be set before running the main program
```
MIMIR_CACHE_PATH: Path to cache directory
MIMIR_DATA_SOURCE: Path to data directory
```
The MIMIR_CACHE_PATH directory should be where the datasets are located. To see what the directory should look like inside, pull data from the original code author's repository from [Hugging Face Datasets](https://huggingface.co/datasets/iamgroot42/mimir). In each folder, they have training and testing datasets that will be treated as member/nonmember data. 

## MIA experiments how to run

```
python run.py --config configs/mi.json
```
This will run the attacks with the specified configuration in the mi.json file in configs folder. The data subsets to test attacks for can be chosen by modifying the dataset_member and dataset_nonmember variables. The implemented attacks can be added or removed from the blackbox_attacks variable, and are as follows

- [Likelihood](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8429311) (`loss`). Works by simply using the likelihood of the target datapoint as score.
- [Reference-based](https://arxiv.org/abs/2004.15011) (`ref`). Normalizes likelihood score with score obtained from a reference model.
- [Zlib Entropy](https://www.usenix.org/system/files/sec21-carlini-extracting.pdf) (`zlib`). Uses the zlib compression size of a sample to approximate local difficulty of sample.
- [Neighborhood](https://aclanthology.org/2023.findings-acl.719/) (`ne`). Generates neighbors using auxiliary model and measures change in likelihood.
- [Min-K% Prob](https://swj0419.github.io/detect-pretrain.github.io/) (`min_k`). Uses k% of tokens with minimum likelihood for score computation.
- [Min-K%++](https://zjysteven.github.io/mink-plus-plus/) (`min_k++`). Uses k% of tokens with minimum *normalized* likelihood for score computation.
- [Gradient Norm](https://arxiv.org/abs/2402.17012) (`gradnorm`). Uses gradient norm of the target datapoint as score.

My datasets are located in 'personal/generated datasets'

# Textcomplexity

Textcomplexity is the program used to measure the metrics of text files. Their main repository can be found [here](https://github.com/tsproisl/textcomplexity).

## Installation

Run this line to install all dependencies
```
pip install textcomplexity
```

## Usage
I made a subrepository of Textcomplexity. I modified it to output graphs to show the distribution of some of the metrics. 

The main program that generates the metrics is run_cli.py, located in textcomplexity_mod/textcomplexity

A sample run of the code would look like 
```
python3 run_cli.py --input-format conllu [file] --lang en --preset all
```
These options would lead for all implemented text metrics to be computed using english (as opposed to the other implemented language for textcomplexity, german). Other options can be found in their main repository [here](https://github.com/tsproisl/textcomplexity)

The graphs that resulted from running my modified version of Textcomplexity can be found in textcomplexity_mod/textcomplexity/member_graphs and textcomplexity_mod/textcomplexity/nonmember_graphs

## Conllu formatting

Textcomplexity requires text to be in the connlu format. They use stanza, a conversion program, to do this. To install stanza, run
```
pip install stanza
```

Now, navigate to textcomplexity/utils, where you should see run_stanza.py. Now you can run the following in order to convert a file to connlu format.
```
python3 run_stanza.py [file] -l english -o [output directory]
```

My input and output files can be found in textcomplexity/input and textcomplexity/output. 

# Project Gutenberg
Project Gutenberg is an open repository of book data. I obtained data from it using [this](https://github.com/pgcorpus/gutenberg/tree/96c8c1cef105b321b4d61fef9dc5e0ca66e80ad1)

to obtain a local copy of their data, run

```
python get_data.py
```