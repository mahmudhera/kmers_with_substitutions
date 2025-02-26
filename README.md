# kmers_with_substitutions
In this repo, I am trying to do this: given all kmers in a reference, check if a query kmer is 0/1/2/3/more hamming distance away from a known kmer.

To do this, I am now building a trie and a suffix tree, and then see how long of a prefix I can consume using the trie, and how long of a suffix I can consume using the suffix tree.

# Problem
This approach does not work. A subst in the beginning of a kmer will inevitably make some prefix of the mutated kmer match with an existing kmer. Need a different approach.

# Installation
```
conda create --name kws python=3.10 -y
conda activate kws
pip install pytrie suffix-trees
```
