from django.shortcuts import render
from django.shortcuts import render
from sklearn import preprocessing
import pandas as pd
import joblib

# Create your views here.
model = joblib.load('model.pkl')

def index(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        bmi = request.POST.get('bmi')
        children = request.POST.get('children')
        smoker = request.POST.get('smoker')
        region = request.POST.get('smoker')

        print(name, age, gender, bmi, children, smoker, region)

        # result = model.predict([[age, gender, bmi, children, smoker, region]])

        myDict = (request.POST).dict()
        df = pd.DataFrame(myDict, index=[0])
        print(df)
        # df.drop('name', axis=1, inplace=True)
        print(df)
        result = model.predict(ohevalue(df))

        return render(request, 'myapp/myform.html',{'name':name, 'result':  float("{:.2f}".format(result[0]))})

    else:
        return render(request, 'myapp/myform.html')


def ohevalue(df):
    ohe_col = joblib.load('all_cols.pkl')
    cat_columns = ['region']
    df_processed = pd.get_dummies(df, columns=cat_columns)
    newdict = {}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i] = df_processed[i].values
        else:
            newdict[i] = 0
    newdf = pd.DataFrame(newdict)
    return newdf