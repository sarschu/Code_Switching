#!/usr/bin/python
# -*- coding: utf-8 -*-

#features char n grams
#pos middleenglish tagger
#prob middleenglish tagger
#pos latin tagger
#prob latin tagger

import sys
import re
import codecs

#1a 
def ngr(text,n):
    ng = []
    for w in text:
        w = re.sub('\_[anle]','',w).strip()
        ng.append([w[i:i+n] for i in range(len(w)-n+1)])
    return ng
    


def extract_features(word,pos_m,prob_m,pos_l,prob_l,mode,g2,m2,g3,m3):

    #print all features
    features= word+"\t"+str(pos_l)+"\t"+str(pos_m)+"\t"+str(prob_l)+ \
    "\t"+str(prob_m)+"\t"+'\t'.join(g2)+"\t"+'\t'.join(['None' for x in range(m2-len(g2))])+"\t"+'\t'.join(g3)+'\t'+'\t'.join(['None' for x in range(m3-len(g3))])+'\t'+mode
    return features.strip()+'\n'

def extract_pos_prob_list(tagged):
    t_lines = tagged.readlines()
    pos,prob = [],[]
    for line in t_lines:
        sl=line.strip().split()

        if sl !=[]:
           pos.append(sl[0].strip())
           prob.append(sl[1].strip())
    return pos,prob

def main():

    text= codecs.open(sys.argv[1],'r','utf8').readlines()
    grams2 = ngr(text,2)
    grams3 = ngr(text,3)
    m2=40
    m3=30
    feature_file = codecs.open(sys.argv[1][:-4]+'.features',"w","utf8")
    md = codecs.open(sys.argv[2],'r','utf8')
    lat = codecs.open(sys.argv[3],'r','utf8')
    train=sys.argv[4]
    if train == 'True':
	train = True
    else:
	train = False
    pos_m,prob_m = extract_pos_prob_list(md)
    pos_l,prob_l = extract_pos_prob_list(lat)
    md.close()
    lat.close()
    mode=''


    for i,w in enumerate(text):
        w=unicode(w.strip())

	if train:
		if w[-2:]=='_l':
		    mode='l'
		elif w[-2:]=='_e':
		    mode='e'
		elif w[-2:]=='_a':
		    last_mode=mode
		    mode='a'
		elif w[-2:]=='_n':
		    last_mode=mode
		    mode='n'
		elif w in ['.',',',';','?','!',':']:
		    last_mode=mode
		    mode='p'
	else:
		mode=''

        #word,pos_m,prob_m,pos_l,prob_l,mode,2g,m2,3g,m3
        feature_file.write(extract_features(re.sub('\_[anle]','',w),pos_m[i],prob_m[i],pos_l[i],prob_l[i],mode,grams2[i],m2,grams3[i],m3))    
        
        if mode in ['a','n','p']:
            mode=last_mode

    feature_file.close()
    
if __name__ == "__main__":
    main()
