import nltk

def manual_text():
    tx = u"أعلن الناقل الجوي الوطني في بريطانيا،'بريتيش أيرويز' الأربعاء"
    words = nltk.word_tokenize(tx)
    print(words)

# man = manual_text()
# if(man):
#     print("manual successfull")

from nltk.corpus import PlaintextCorpusReader as txtrd

def textFile():
    corpus_root = "./dset/cnn-arabic/"
    f = "./short/data-1.txt"
    wordlist = txtrd(corpus_root,'.*/*')
    cats = wordlist.categories()
    filelist = wordlist.fileids() 
    print(cats)
    #print(filelist)
    # words = nltk.word_tokenize(tx)
    # print(words)

import pyarabic.araby as arb 
import pyarabic.number as num

def tagText():
    tx = u"و نشر العدل من خلال قضاء مستقل"
    words = arb.tokenize(tx)
    arb.pos_tag(words)
    print(words)

#textFile()
#tagText()

from nltk.stem.isri import ISRIStemmer

def stemText():
    tx = "و نشر العدل من خلال قضاء المستقل"
    words = arb.tokenize(tx)
    st = ISRIStemmer()
    for w in words:
        st.stem(w)
        print(w)


from nltk.stem.arlstem2 import ARLSTem2

def stemTextAR():
    tx = "و نشر العدل من خلال قضاء المستقل"
    words = arb.tokenize(tx)
    st = ARLSTem2()
    for w in words:
        st.stem(w)
        print(w)

#stemTextAR()

from nltk.corpus import swadesh

def tranSwed():    
    ar2en = swadesh.entries(['ar', 'en'])
    translate = dict(ar2en)
    tx = "و نشر العدل من خلال قضاء المستقل"
    translate[tx]

tranSwed()
