# Code Switching

Aim: detect the languages of the words and use this information for a POS tagging that 
tags the different languages in their context of a foreign language

************************

## Language detection

Training and testing done in a 10-fold cross validation setting.
Results so far 95% of accuracy

Algorithm used: CRF
features: output and confidence of Middle-English tree tagger, Latin tree tagger, character-bigram and character-trigram 
context: window of 5 on all features


##POS tagging

Waiting for train data