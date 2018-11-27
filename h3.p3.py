#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 11:26:53 2018

@author: VyTran
"""

def get_csv_data(f, string_pos_list, sep= ","):
    data_lst = []
    columns = f.readline()
    columns = columns.strip()
    columns = columns.split(sep)
    #data_lst.append(columns)
    lines = f.readlines()

    lines = lines[:-4]
    for i in range(len(lines)):
        line = lines[i]
        line = line.strip()
        line = line.split(sep)

    for x in range(len(line)):
        if x in string_pos_list:
            line[x] = str(line[x])
        else:
            line[x] = float(line[x])
    print line
    #print columns
    #print lines
    #print data_lst

bb_file = open("lb-james.csv", "r")
james_lst = get_csv_data(bb_file, [0, 2, 3, 4])    # columns at indeces 0,2,3,4


"""import pylab 

def get_csv_data(f, string_pos_list, sep):
    data_list = []
    column_heading = []
    hold = []
    
    h = f.readline()
    try:
        for tok in h.split(sep):
            column_heading.append(tok)
        data_list.append(column_heading)
        
        for line in f:
            for tok in line.split(sep):
                hold.append(tok)
            data_list.append(hold)
            hold = []
        for x in range(len(data_list)):
            for y in range(len(data_list[x])):
                for z in range(len(string_pos_list)):
                    if y == string_pos_list[z]:
                        break
                    if z == len(string_pos_list) - 1 and x!=0:
                        data_list[x][y] = float(data_list[x][y])
    except ValueError as v:
        print("There was a value error: ", v)
    except Exception as e:
        print("Sorry there was an error ", e)
    return data_list

def get_column(data_lst, cols_lst):
    l = []
    selected_columns_lst = []
    s = data_lst[0][len(data_lst[0])-1].replace('\n','')
    data_lst[0][len(data_lst[0])-1] = s
    
    for x in range(len(cols_lst)):
        if cols_lst[x] in data_lst[0]:
            for i in range(len(data_lst[0])):
                if cols_lst[x] == data_lst[0][i]:
                    print(cols_lst[x], "is in column", i)
                    for t in range (len(data_lst)):
                        if t != 0:
                            l.append(data_lst[t][i])
                    selected_columns_lst.append(l)
                    l = []
    return selected_columns_lst

file = open("lb-james.csv", "r")
pos_list = [0,2,3,4]

m = get_csv_data(file, pos_list, ',')
find = ['Season', '3P%', '2P%', 'FT%']
p = get_column(m, find)

x = [d for d in range(len(p[0]))]
xT = [p[0][i] for i in range(len(p[0]))]
y = [p[1][n] for n in range (len(p[0]))]
y1 = [p[2][n] for n in range (len(p[0]))]
y2 = [p[3][n] for n in range (len(p[0]))]

pylab.xticks(x, xT)
pylab.xticks(range(len(p[0])), xT, rotation = 45)
pylab.plot(x,y, 'ro-', label = '3P%')
pylab.plot(x,y, 'yo-', label = '2P%')
pylab.plot(x,y, 'bo-', label = 'FT%')
pylab.legend()
pylab.xlabel("Year")
pylab.ylabel("Percentage")
pylab.title("Lebron's Shooting Percentage")
pylab.show()
"""