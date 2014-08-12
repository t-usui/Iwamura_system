#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import lcs

def make_file_list(dir_name):
    file_list = os.listdir(dir_name)
    return file_list

def make_combination(file_list):
    combination = []
    for i in range(len(file_list)):
        for j in range(i):
            combination.append((file_list[i], file_list[j]))
    return combination

def get_all_combination(dir_name):
    file_list = make_file_list(dir_name)
    combination = make_combination(file_list)
    return combination

if __name__ == '__main__':
    dir_name = 'files'
    for c in get_all_combination(dir_name):
        print c
