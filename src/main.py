#!/usr/bin/env python
#-*- coding:utf-8 -*-

from combine import *
from classify import *
from format import *
import sys

if __name__ == '__main__':
    dir_name = 'files'
    distance_list = []
    file_list = make_file_list(dir_name)
    combination = get_all_combination(dir_name)
    list = [[''] * 5] * 5
    for c in combination:
        print c[0], c[1]
        distance = calculate_distance(dir_name + '/' + c[0],
                            		  dir_name + '/' + c[1])
        print distance
        distance_list.append(distance) 

    distance_matrix = make_distance_matrix(file_list, distance_list)
    generate_csv_file('distance.csv', distance_matrix)
    generate_newick_file_with_R('distance.csv', 'newick.txt')
