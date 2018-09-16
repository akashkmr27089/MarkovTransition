#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 10:40:16 2018

@author: mycore
"""

import numpy as np

a = np.zeros((26,26), dtype=float)
b = np.zeros((1,26), dtype=int)
g = []
count = 0

#data preprocessing ###########################################################
def char_preproc(data): #data processing to be done befor char_count ->type::string
    c=[]
    for i in data:
        if(i.isalpha()):
            c.append(i)
        if(i==" "):
            c.append(" ")
    for i in range(c.__len__()):
        if(c[i].isupper()):
            c[i]=c[i].lower()
    return c

def two_char(data): #returns two character as an element ->type::string
    c = char_preproc(data)
    print(data)
    e = []
    for i in range(c.__len__()-1):
        e.append(c[i]+c[i+1])
    return e

def word_preproc():
    j=0
    opn = open("words.txt", "r")
    for line in opn:
        if(line.__len__()>=2 and line[0].isalpha() and line[1].isalpha() and line[0]=='b'):
            g.append(line)
            j = j+1
        if(j==10000):
            break
    opn.close()
    for i in g:
        print(i)
        

    
###############################################################################
def char_count(data): #keep counting characters -> requires char_preproc before ->type::list of character
    d = 0 
    for i in data:
        d = ord(i)-97
        b[0][d] = b[0][d] + 1
        
def markov(data): #send only 2 char at a time and increase the number  ->type::string
    global count
    if(data.__len__()==2):
        x = ord(data[0])-97
        y = ord(data[1])-97
        if(x>=0 and y>=0 and x<=25 and y<=25):
            #print(data +" "+ str(x) + " " +str(y))
            count = count + 1
            a[x][y] = a[x][y] + 1
            
#main_file######################################################################
def test_file():
    a = "nation /sd"
    a = two_char(a)
    print(a)
    for i in a:
        markov(i)

def main_file():
    opn = open("words.txt", "r")
    for line in opn:
        if(line.__len__()>=2 and line[0].isalpha() and line[1].isalpha()):
            a = line
            a = two_char(a)
            for i in a:
                markov(i)
    opn.close()
    
def chal1():
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if(a[i][j] == 0):
                print(chr(i+97)+" "+chr(j+97))

def prob1():
    global g
    g = (a/count)*10
            
                
