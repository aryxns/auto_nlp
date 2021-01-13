import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])

install('stanza')

import stanza
stanza.download('en')
nlp = stanza.Pipeline('en')


class Aspect:
    def recognizer(txt):
        txt = txt.lower()
        sentList = nltk.sent_tokenize(txt)
        for line in sentList:
            txt_list = nltk.word_tokenize(line)
            taggedList = nltk.pos_tag(txt_list)
        #print(taggedList)
        newwordList = []
        flag = 0
        for i in range(0,len(taggedList)-1):
            if(taggedList[i][1]=="NN" and taggedList[i+1][1]=="NN"):
                newwordList.append(taggedList[i][0]+taggedList[i+1][0])
                flag=1
            else:
                if(flag==1):
                    flag=0
                    continue
                newwordList.append(taggedList[i][0])
                if(i==len(taggedList)-2):
                    newwordList.append(taggedList[i+1][0])
        finaltxt = ' '.join(word for word in newwordList)
        #print(finaltxt)

        stop_words = set(stopwords.words('english'))
        new_txt_list = nltk.word_tokenize(finaltxt)
        wordsList = [w for w in new_txt_list if not w in stop_words]
        taggedList = nltk.pos_tag(wordsList)
        #print(finaltxt)
        doc = nlp(finaltxt)
        dep_node = []
        for dep_edge in doc.sentences[0].dependencies:
          dep_node.append([dep_edge[2].text, dep_edge[0].id, dep_edge[1]])
        for i in range(0, len(dep_node)):
          if (int(dep_node[i][1]) != 0):
            dep_node[i][1] = newwordList[(int(dep_node[i][1]) - 1)]
            #print(dep_node)
        featureList = []
        categories = []
        totalfeatureList = []
        for i in taggedList:
            if(i[1]=='JJ' or i[1]=='NN' or i[1]=='JJR' or i[1]=='NNS' or i[1]=='RB'):
                featureList.append(list(i))
                totalfeatureList.append(list(i)) # This list will store all the features for every sentence
                categories.append(i[0])
        #print(featureList)
        #print(categories)
        fcluster = []
        for i in featureList:
            filist = []
            for j in dep_node:
                if((j[0]==i[0] or j[1]==i[0]) and (j[2] in ["nsubj", "acl:relcl", "obj", "dobj", "agent", "advmod", "amod", "neg", "prep_of", "acomp", "xcomp", "compound"])):
                    if(j[0]==i[0]):
                        filist.append(j[1])
                    else:
                        filist.append(j[0])
            fcluster.append([i[0], filist])
        #print(fcluster)
        return categories   
