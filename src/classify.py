#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import commands
import lcs

# Extract disassembled machine instruction sequence
# Input: file name to fetch machine instruction sequence (string)
# Output: machine instruction sequence (list of string)
def fetch_machine_instruction_sequence(file_name):
  machine_instruction_sequence = []
  ret = commands.getoutput('beelzebub ' + file_name)

  flag = 0
  for line in ret.split('\n'):
    if flag == 0:
      if line == 'Start disassembling...':
        flag = 1
      else:
        next
    else:
      machine_instruction_sequence.append(line.split(' ')[0].lstrip('\t'))
  return machine_instruction_sequence

# S (Jaccard coefficient) = |L|/(|A| + |B| - |L|)
# Where
# A, B: Set
# L: Longest Common Subsequence of A, B
# Input: 
# Output: similarity (float)
def calculate_jaccard_coefficient(L, A, B):
  S = float(L) / float(len(A) + len(B) - L)
  return S

# Input: two file names to calculate similarity
# Output: similarity
def calculate_similarity(file_name_1, file_name_2):
    seq1 = fetch_machine_instruction_sequence(file_name_1)
    seq2 = fetch_machine_instruction_sequence(file_name_2)
    lcs_len_seq1_seq2 = lcs.find_lcs_len(seq1, seq2)
    similarity = calculate_jaccard_coefficient(lcs_len_seq1_seq2, seq1, seq2)
    return similarity

# Input: similarity
# Output: distance
def calculate_distance(file_name_1, file_name_2):
    distance = 1 - calculate_similarity(file_name_1, file_name_2)
    return distance

if __name__ == '__main__':
  argv = sys.argv
  argc = len(argv)

  file_name_1 = argv[1]
  file_name_2 = argv[2]
#  for i in fetch_machine_instruction_sequence(file_name):
#    print i
