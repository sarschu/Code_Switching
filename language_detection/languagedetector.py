#!/usr/bin/python
# -*- coding: utf-8 -*-

#usage python languagedetector.py scriptdir infile
import sys
import re
import subprocess
import codecs
import os

class LanguageDetector:

    def __init__(self,scriptdir,inf):
        self.inf=inf
        self.tt_me='/mount/projekte/sfb-732/inf/users/sarah/tools/tree_tagger/cmd/tree-tagger-middleenglish'
        self.tt_lat='/mount/projekte/sfb-732/inf/users/sarah/tools/tree_tagger/cmd/tree-tagger-latin'
        self.crf='/mount/arbeitsdaten13/users/schulzsh/tools/CRF++-0.58/crf_test'
        self.template='/mount/projekte/sfb-732/inf/users/sarah/gits/Code_Switching/language_detection/template_34'
        self.scriptdir=scriptdir
        self.model='/mount/projekte/sfb-732/inf/users/sarah/gits/Code_Switching/language_detection/language_detect_all.model'

    def preprocess(self):
        me_path='.'.join(self.inf.split('.')[:-1])+'.me'
        lat_path='.'.join(self.inf.split('.')[:-1])+'.lat'
        me_out=codecs.open(me_path,'w','utf8')
        o_inf=codecs.open(self.inf,'r','utf8')
        mt= subprocess.Popen([self.tt_me],stdin=o_inf,stdout=me_out)

        out,err = mt.communicate()
        o_inf.close()
        o_inf=codecs.open(self.inf,'r','utf8')
        me_out.close()

        lat_out=codecs.open(lat_path,'w','utf8')
        lt= subprocess.Popen([self.tt_lat],stdin=o_inf,stdout=lat_out)

        out,err = lt.communicate()
        o_inf.close()

        lat_out.close()

        feature_file_path='.'.join(self.inf.split('.')[:-1])+'.features'
        feature_file=codecs.open(feature_file_path,'w','utf8')
        mf= subprocess.Popen(['python',scriptdir+'/make_feature_file.py',self.inf,me_path,lat_path,str(False)],stdout=feature_file)
        mf.communicate()
        feature_file.close()
        return feature_file_path
    
    def lang_detect(self,feature_file_p):
        ff=codecs.open(feature_file_p,'r','utf8')
        print ff
        
        t_path='.'.join(feature_file_p.split('.')[:-1])+'.langtagged'
        tagged=codecs.open(t_path,'w','utf8')
        crf_tag=subprocess.Popen([self.crf,'-m',self.model],stdout=tagged,stdin=ff)
        crf_tag.communicate()
        tagged.close()
        
        return t_path

    def postprocess(self,tagged):
        tf= codecs.open(tagged,'r','utf8')
        lines = tf.readlines()
        print lines
        out = codecs.open('.'.join(tagged.split('.')[:-1])+'.out','w','utf8')
        for line in lines:
            out.write(line.split('\t')[0]+'_'+line.split('\t')[-1].strip()+'\n')
        
    def tag(self):
        ff=self.preprocess()    
        tf=self.lang_detect(ff)
        self.postprocess(tf)
    
        

if __name__ == '__main__':
    scriptdir=sys.argv[1]
    inf=sys.argv[2]
    LanguageDetector(scriptdir,inf).tag()
    
