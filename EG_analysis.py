# natural language processing from a podcast transcript in a txt file
# using NLTK's Natural Language Toolkit
# a Python library for natural language processing

#Import libraries

import streamlit as st
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import re

#header
st.header('Select the transcript in text file:')

#load the transcript from a txt file

uploaded_file = st.file_uploader("Load the text file located in the root of the github folder.")
if uploaded_file is not None:
    data = uploaded_file.read().decode('utf-8')

#cleaning the transcript

data_tokens = word_tokenize(data)
data_tokens = [re.sub(r'[^\w\s]','',word) for word in data_tokens]

# delete empty strings
data_tokens = [word for word in data_tokens if word != '']

#delete any word with number
data_tokens = [word for word in data_tokens if not any(char.isdigit() for char in word)]

#delete special characters
data_tokens = [word for word in data_tokens if any(char.isalpha() for char in word)]

#bigrams
bi_data = list(nltk.bigrams(data_tokens))
tri_data = list(nltk.trigrams(data_tokens))


preposition = ['der','die','das','den','dem']
prep = st.select_slider(
     'Preposition:',
     options=preposition)

st.text('Shows the preposition before and after one word.')

#check for word in bigrams
after = []
for i in bi_data:
  if i[1] == prep:
    after.append(i[0]+' '+i[1])

after.sort()
after = pd.DataFrame(after, columns=['words'])
after = after.drop_duplicates()
st.dataframe(data=after, width=None, height=None)

before = []
for i in bi_data:
  if i[0] == prep:
    before.append(i[0]+' '+i[1])

before.sort()
before = pd.DataFrame(before, columns=['words'])
before = before.drop_duplicates()
st.dataframe(data=before, width=None, height=None)

#Word behaviour
word_enter = st.text_input('Enter a word:')
st.text('Shows the word in the first, second and third position on a sentence of 3 words.')

#check for word in trigrams
words13 = []
for i in tri_data:
  if i[0] == word_enter:
    words13.append(i[0]+' '+i[1]+' '+i[2])

words13.sort()
words13 = pd.DataFrame(words13, columns=['words'])
words13 = words13.drop_duplicates()
st.dataframe(data=words13, width=None, height=None)

words23 = []
for i in tri_data:
  if i[1] == word_enter:
    words23.append(i[0]+' '+i[1]+' '+i[2])

words23.sort()
words23 = pd.DataFrame(words23, columns=['words'])
words23 = words23.drop_duplicates()
st.dataframe(data=words23, width=None, height=None)

words33 = []
for i in tri_data:
  if i[2] == word_enter:
    words33.append(i[0]+' '+i[1]+' '+i[2])

words33.sort()
words33 = pd.DataFrame(words33, columns=['words'])
words33 = words33.drop_duplicates()
st.dataframe(data=words33, width=None, height=None)


#streamlit run EG_analysis.py

