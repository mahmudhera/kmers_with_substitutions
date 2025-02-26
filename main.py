from pytrie import SortedStringTrie as Trie
import random

trie_fwd = Trie()
trie_bckwd = Trie()

def insert_kmer(kmer):
    for i in range(len(kmer)):
        trie_fwd[kmer[:i+1]] = True
    reverse_kmer = kmer[::-1]
    for i in range(len(reverse_kmer)):
        trie_bckwd[reverse_kmer[:i+1]] = True
        
def insert_kmers(kmers):
    for kmer in kmers:
        insert_kmer(kmer)
        
def extract_kmers_and_positions(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append((sequence[i:i+k], i))
    return kmers

def search_kmer(kmer, max_hd = 3):
    longest_prefix_len = len(trie_fwd.longest_prefix(kmer))
    longest_suffix_len = len(trie_bckwd.longest_prefix(kmer[::-1]))
    for i 

alphabet = ['A', 'C', 'G', 'T']
dna_string = 'CCGTTCGCAAAACTGAAACATGGTCGGGCTGTCACAGCAGGCGCGTCAATTGGATTTCGTTCCTTCCAGTCCCTGGACGGTGGGGGCCTCGCACATGGAA'
query_kmer = 'TCGTTCGCAAAACTGAAACAT'
k = 21
kmers = extract_kmers(dna_string, k)
insert_kmers(kmers)
print('Trie built successfully')
print('Searching for kmer:', query_kmer)
result = search_kmer(query_kmer)
print('Result:', result)
print('Done')