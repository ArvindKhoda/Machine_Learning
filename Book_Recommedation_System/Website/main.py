#Importing Required Libraries
import pickle
import pandas as pd
import numpy as np
from flask import Flask,render_template,request

#Importing Required Data
data=pd.read_excel('Biography_Books_Amazon_Dataset.xlsx')
Data=pd.read_excel('Biography_Books_Amazon_Dataset.xlsx')

#Changing index column as name 
data.set_index('Name',inplace=True)

#Removingn Image_URL columns
data.drop(columns={'Image_URL'},inplace=True)

#Dumping File
similar=pickle.load(open('similar_book','rb'))

#Function for recommendation
def recommend(name):
 index=np.where(data.index==name)[0][0]
 item=sorted(list(enumerate(similar[index])),key=lambda x:x[1],reverse=True)[0:5]
 Item_index=[]
 for i in item:
     Item_index.append(i[0])
 return Item_index


#Creation of APP
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods=['POST'])
def result():
    Name=request.form.get('name')
    r = recommend(Name)
    result = Data.iloc[r]

    Name = list(result.Name)
    Paper_Type = list(result.Paper_Type)
    First_Availability_Month = list(result.First_Availability_Month)
    First_Availability_Day = list(result.First_Availability_Day)
    First_Availability_Year = list(result.First_Availability_Year)
    Author = list(result.Author)
    Ratings = list(result.Ratings)
    Rating_Total = list(result.Rating_Total)
    Paperback_Price = list(result.Paperback_Price)
    MRP = list(result.MRP)
    Discount_Percentage = list(result.Discount_Percentage)
    Publisher = list(result.Publisher)
    Language = list(result.Language)
    Pages = list(result.Pages)
    ISBN_10 = list(result.ISBN_10)
    ISBN_13 = list(result.ISBN_13)
    Age = list(result.Age)
    Weight_g = list(result.Weight_g)
    Dimensions_L = list(result.Dimensions_L)
    Dimensions_B = list(result.Dimensions_B)
    Dimensions_W = list(result.Dimensions_W)

    Importer = list(result.Importer)
    Packer = list(result.Packer)
    Image_URL = list(result.Image_URL)

    return render_template('result.html',name=Name,
paper_type=Paper_Type,
first_availability_month=First_Availability_Month,
first_availability_day=First_Availability_Day,
first_availability_year=First_Availability_Year,
author=Author,
ratings=Ratings,
rating_total=Rating_Total,
paperback_price=Paperback_Price,
mrp=MRP,
discount_percentage=Discount_Percentage,
publisher=Publisher,
language=Language,
pages=Pages,
isbn_10=ISBN_10,
isbn_13=ISBN_13,
age=Age,
weight_g=Weight_g,
dimensions_l=Dimensions_L,
dimensions_b=Dimensions_B,
dimensions_w=Dimensions_W,
importer=Importer,
packer=Packer,
image_url=Image_URL)
    #return render_template('demo.html')
app.run(debug=True)