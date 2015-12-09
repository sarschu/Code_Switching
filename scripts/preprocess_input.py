#!/usr/bin/python
# -*- coding: utf-8 -*-

#features char n grams
#pos middleenglish tagger
#prob middleenglish tagger
#pos latin tagger
#prob latin tagger

import sys
import re
import subprocess
import codecs

inf=codecs.open(sys.argv[1],'r','utf8')
me_out=codecs.open('.'.join(sys.argv[1].split('.')[:-1])+'.me','w','utf8')
mt= subprocess.Popen(['/mount/projekte/sfb-732/inf/users/sarah/tools/tree_tagger/cmd/tree-tagger-middleenglish'],stdin=inf,stdout=me_out)

out,err = mt.communicate()

#me_out.write(out)

me_out.close()

lat_out=codecs.open('.'.join(sys.argv[1].split('.')[:-1])+'.lat','w','utf8')
lt= subprocess.Popen(['/mount/projekte/sfb-732/inf/users/sarah/tools/tree_tagger/cmd/tree-tagger-latin'],stdin=inf,stdout=lat_out)

out,err = lt.communicate()

#me_out.write(out)

lat_out.close()
