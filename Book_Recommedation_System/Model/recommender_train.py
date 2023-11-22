# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 01:12:49 2023

@author: Arvind
"""

#Importing Required Libraries
import pickle
import pandas as pd
import numpy as np

#Importing Required Dataset
data=pd.read_excel('data.xlsx')

#Info About Data
data.info()

#changing index as Name Column
data.set_index('Name',inplace=True)

#Removing Image_URL Column
data.drop(columns={'Image_URL'},inplace=True)

#Making duplicate copy of data
data_cp=data.copy(deep=True)

#Finding Categorical Columns
cat_col=[]
for col in data.columns:
    if(data[col].dtypes=='object'):
        cat_col.append(col)

#Encoding
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
cat_class=[]
for col in cat_col:
    data[col]=encoder.fit_transform(data[col])
    cat_class.append(encoder.classes_)
    
#Similarity Model
from sklearn.metrics.pairwise import cosine_similarity
similar=cosine_similarity(data)    
s=pd.DataFrame(similar)
s.to_csv("similar.csv")


#Saving Similar File in Pickle Format
pickle.dump(s, open("similar_book.pkl",'wb'))

def recommend(name):    
 index=np.where(data.index==name)[0][0]
 item=sorted(list(enumerate(similar[index])),key=lambda x:x[1],reverse=True)[0:6]
 Item_index=[]  
 for i in item:
     Item_index.append(i[0])
 return Item_index
    
similar_index=recommend("Jaun Elia: Ek Ajab Ghazab Shayar - Hindi")

#Results
for i in similar_index:
    print(i)
    print(data_cp.iloc[i])
    print()
