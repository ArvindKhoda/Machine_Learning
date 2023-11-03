import pymongo
from pymongo import MongoClient
from flask import Flask,render_template,request
import pickle

uri ="mongodb+srv://arvind:7725920259@cluster0.8s9dokk.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(uri)
db=client["Agriculture"]
user=db['user']

#Object Creation of application
app=Flask(__name__)

#crop prediction
classifier=pickle.load(open('crop_rf.pkl','rb'))
data=pickle.load(open('Label.pkl','rb'))

@app.route('/Main',methods=['POST'])
def result():
    n=int(request.form.get('N'))
    p=int(request.form.get('P'))
    k=int(request.form.get('K'))
    ph=float(request.form.get('PH'))
    t=float(request.form.get('T'))
    h=float(request.form.get('H'))
    r=float(request.form.get('R'))

    result=int(classifier.predict([[n,p,k,t,h,ph,r]]))
    final_result=data.index[data.Label==result][0]
    return render_template('main.html', result=final_result)



#Routing
@app.route('/')
def home():
    return render_template('Home.html')
@app.route('/register')
def register():
    return render_template('Register.html')

@app.route('/signup',methods=['POST'])
def signup():
    Name=request.form.get('Name')
    Contact=request.form.get("Contact")
    Email=request.form.get("Email")
    Password=request.form.get("Password")
    City=request.form.get("City")
    State=request.form.get("State")
    Occupation=request.form.get("Occupation")
    data={
        'Name':Name,
        'Contact':Contact,
        'Email':Email,
        'Password':Password,
        'City':City,
        'State':State,
        'Occupation':Occupation
    }
    user.insert(data)
    return "Your Registration is Done,Now You Can <a href='/'> Login</a>"

@app.route('/problem')
def problem():
    return render_template('problem.html')

@app.route('/p',methods=['POST'])
def p():
    problem=request.form.get('problem')
    comment=request.form.get('comment')
    print(problem)
    return "Your Problem is Registered and it will be resolved soon"

@app.route('/login',methods=['POST'])
def login():
    email=request.form.get('email')
    password=request.form.get('password')
    credentials={
        'Email':email,
        'Password':password
    }
    if (user.find_one(credentials)):
       return render_template('dashboard.html')
    else:
        return(render_template('wrong_cred.html'))




@app.route('/crop_predict')
def crop_predict():
    return render_template('main.html')
#Running App
app.run(debug=True)
