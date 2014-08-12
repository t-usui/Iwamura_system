#!/usr/bin/env python
#-*- coding:utf-8 -*-

import csv
import commands

def make_distance_matrix(file_list, distance_list):
    # Initialization
    distance_matrix = []
    for i in range(len(file_list) + 1):
        list = [None] * (len(file_list) + 1)
        distance_matrix.append(list)

    # Set header and name column
    for i in range(len(file_list) + 1):
        if i == 0:
            continue
        distance_matrix[0][i] = file_list[i-1]
        distance_matrix[i][0] = file_list[i-1]

    # Set distance
    for i in range(2, len(file_list) + 1):
        for j in range(1, i):
            distance_matrix[i][j] = distance_list.pop(0)

#    for list in distance_matrix:
#        print list
    return distance_matrix

def generate_csv_file(file_name, matrix):
    csv_writer = csv.writer(open(file_name, 'wb'),
                            delimiter=',',
                            quotechar=' ',
                            quoting=csv.QUOTE_MINIMAL)
    print matrix
    for line in matrix:
        csv_writer.writerow(line)

def generate_newick_file_with_R(input_file_name, output_file_name):
    commands.getoutput('Rscript hclust.R %s %s' % (input_file_name, output_file_name))
    f = open(output_file_name, 'r')
    str = f.read()
    f.close()
    str = str.replace('"', '', 2)
    f = open(output_file_name, 'w+')
    f.write(str)
    f.close()

if __name__ == '__main__':
    file_list = ['A', 'B', 'C', 'D']
    similarity_list = [1,2,3,4,5,6]
    distance_matrix = make_distance_matrix(file_list, similarity_list)
    print distance_matrix[0]
    print distance_matrix[1]
    print distance_matrix[2]
    print distance_matrix[3]
    print distance_matrix[4]
    generate_csv_file('distance.csv', distance_matrix)
    generate_newick_file_with_R('distance.csv', 'newick.txt')
