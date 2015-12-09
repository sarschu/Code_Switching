#!/usr/bin/env python

# -*- coding: utf-8 -*-
import codecs
import sys

output = sys.argv[1]
nr_features= int(sys.argv[2])

outf = codecs.open(output,'w','utf8')

outf.write('# Unigram\n\n')
#U00:%x[

fnr=0
for f in range(nr_features):
	outf.write('U'+str(fnr)+':%x[0,'+str(f)+']\n')
	fnr+=1
	outf.write('U'+str(fnr)+':%x[-1,'+str(f)+']\n')
	fnr+=1
	outf.write('U'+str(fnr)+':%x[-2,'+str(f)+']\n')
	fnr+=1
	fnr+=1
	outf.write('U'+str(fnr)+':%x[1,'+str(f)+']\n')
	fnr+=1	 	
	outf.write('U'+str(fnr)+':%x[2,'+str(f)+']\n')
	fnr+=1

outf.write('\n\n# Bigram\nB\n')
outf.close()

