
# coding: utf-8

# IMPORTACAO DAS BIBLIOTECAS

# In[7]:

import sys
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble
from sklearn.model_selection import train_test_split


#  REQUISITANDO O ARQUIVO TXT DA PAGINA

# In[8]:

function get_url(){
	end = sys.argv[0]
 	print end
	return end
}

response = requests.get('https://www.folhabv.com.br/noticia/Servidores-fazem-manifesto-em-frente-ao-TJRR/46132')


# CONVERTANDO EM ARQUIVO DE FORMATO HTML

# In[9]:


soup =  BeautifulSoup(response.text, 'html.parser')


# NOS CIBLAMOS DENTRO DO ARQUIVO HTML INFORMACAÇAO NECESSARIA QUE PRECISARMOS

# In[10]:


links = soup.findAll('div', attrs={'class': 'text'})
titulo = soup.find('title')


# APENAS PARA VISUALIZAR INFORMAÇÃO OBTIDA

# In[11]:


info = []
sent = []
fim = []
tit = []
for link in links:
    info.append((link.text,link.get('p')))
sent = info[0][0].split('\n')
for ele in sent:
    if (ele != '') and (ele != ' '):
        fim.append(ele)
tit.append ((titulo.text,titulo.get('title')))
tit=tit[0][0]


# In[12]:


dado = pd.DataFrame({'texto':fim})
dado['title'] = tit
dado.head()


# In[ ]:


# split the dataset into training and validation datasets 


# In[14]:


train_x, valid_x, train_y, valid_y = model_selection.train_test_split(dado['texto'], dado['title'])


# In[ ]:


# label encode the target variable 


# In[16]:


encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
valid_y = encoder.fit_transform(valid_y)


# In[ ]:


# create a count vectorizer object 
# transform the training and validation data using count vectorizer object


# In[21]:



count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')  
count_vect.fit(dado['texto'])

xtrain_count =  count_vect.transform(train_x)
xvalid_count =  count_vect.transform(valid_x)

