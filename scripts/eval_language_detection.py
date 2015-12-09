#!/usr/bin/env python

# -*- coding: utf-8 -*-
#usage python eval_language_detectuib.py folder_with_sets
import codecs
import os
import re
import sys


setnr=10
inputfolder= sys.argv[1]
acc=[]
baseline_acc_l=[]
baseline_acc_e=[]

dist_ic_l=[]
dist_ic_n=[]
dist_ic_a=[]
for i in range(setnr):
    corr=0
    corr_bl=0
    corr_be=0
    incorrect=0
    ic_l=0
    ic_n=0
    ic_a=0
    crf_test = codecs.open(inputfolder+'/set'+str(i)+'/test.crf','r','utf8').readlines()
    for l in crf_test:
        ls=l.strip().split()
        if ls[-2].strip()==ls[-1].strip():
            corr+=1
        else:
            incorrect+=1
            if ls[-2].strip() in ['e','l']:
                ic_l+=1
            if ls[-2].strip() =='n':
                ic_n+=1
            if ls[-2].strip() =='a':
                ic_a+=1
        if ls[-2].strip() == 'l':
            corr_bl+=1
        if ls[-2].strip() == 'e':
            corr_be+=1
    print corr
    print len(crf_test)
    dist_ic_l.append(float(ic_l)/incorrect)
    dist_ic_a.append(float(ic_a)/incorrect)
    dist_ic_n.append(float(ic_n)/incorrect)
    acc.append(float(corr)/len(crf_test))
    baseline_acc_l.append(float(corr_bl)/len(crf_test))
    baseline_acc_e.append(float(corr_be)/len(crf_test))
print acc
print baseline_acc_l
print  baseline_acc_e
print 'average acc'
print sum(acc)/setnr
print 'average acc_l'
print sum(baseline_acc_l)/setnr
print 'average acc_e'
print sum(baseline_acc_e)/setnr
print 'average nr incorrect lang'
print sum(dist_ic_l)/setnr
print 'average nr incorrect n'
print sum(dist_ic_n)/setnr
print 'average nr incorrect a'
print sum(dist_ic_a)/setnr
    
