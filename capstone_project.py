# -*- coding: utf-8 -*-
"""capstone_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1icLcm4L0XV5yB-zr0GBNgihIl6hayRUB
"""

import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import Ridge
from sklearn.feature_selection import SelectKBest,f_regression


# Cost Functions
from sklearn.metrics import mean_absolute_error



# Feature Engineering
from sklearn.preprocessing import OneHotEncoder

# Plot style
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn-whitegrid")
import plotly.express as px

df= pd.read_csv("Social Development Bank Loans For 2019(Edited)22.csv").drop(columns="ID")

df.head()

# Plot the missing values
df.isnull().sum().plot(kind = "barh", color = "k"); plt.title("Missing Values");

# Save the plot 
plt.savefig('plot1.png',bbox_inches='tight')

df["Customer sector"].isnull().sum()

# Handle NaN
df["Customer sector"] = df["Customer sector"].fillna(method= "backfill") # back fill for missing values in customer sector
#fill NaN with most frequent Family members
df["Family members"] = df["Family members"].fillna(df["Family members"].value_counts().index[0]) 
#fill NaN with most frequent Income
df["Income"] = df["Income"].fillna(df["Income"].value_counts().index[0])
#fill NaN with most frequent Age
df["Age"] = df["Age"].fillna(df["Age"].value_counts().index[0])

# Save data after handle NaN
df.to_csv("dataset.csv",index=False)

# first plot
# Get the Funding value where value in Gender is Female
histF = df.loc[(df['Gender']=='Female')]['Funding value']

# Get the Funding value where value in Gender is Male
histM = df.loc[(df['Gender']=='Male')]['Funding value']

#plot size

fig = plt.figure(figsize=(22, 14))

#  subplot 1
# plot firt quarter funding value for each gender

plt.subplot(231)
x3 = df.groupby('Funding value').Gender.hist(color = '#20B2AA')
plt.xlabel('Gender') 
plt.ylabel('Count') 
plt.title(" The Funding value for each Gender")
fig.tight_layout(pad=3.0)

#  subplot 2
# plot funding value for each gender over change date

plt.subplot(2,3,2)
ax1=sns.lineplot(x="Exchange date", y="Funding value", data=df ,hue = "Gender",palette=['#008080','#00CED1'])
plt.title('Fundings for each gender in the first quarter 2019')
fig.tight_layout(pad=3.0)

# Save the plots
plt.savefig('plot2.png',bbox_inches='tight')
plt.show()

# Second plot
#create new dataframe (new_DF)
new_DF=pd.DataFrame()

new_DF=df[["Age","Funding value"]].copy().reset_index()# copy the columns from Data frame
new_DF['Counts'] = new_DF.groupby(['Age'])['Funding value'].transform('count') 
new_DF=new_DF.groupby('Age').agg({'Funding value':'mean','Counts':'mean'})# calculate mean for funding value and count
new_DF['Age'] = new_DF.index

#plot size
plt.figure(figsize =(10,8))

#plot barchart with age fundinges counter
ax = sns.barplot(x='Age', y='Counts', data=new_DF, palette=['#008080','#20B2AA', '#00CED1','#AFEEEE'])
plt.ylabel('Count of age')
ax2 = ax.twinx()

#plot linechart with age fundinges value and age fundenges count

ax2.plot(ax.get_xticks(), new_DF["Funding value"],label="Funding value", color= '#40E0D0')
plt.setp(ax.get_xticklabels())#, rotation=90)
plt.title("funding value orderd by age".title())
plt.ylabel('funding value')
plt.legend()
plt.xticks(rotation=50)
# Save the plot
plt.savefig('plot3.png',bbox_inches='tight')
plt.show();

#Third plot
#plot median of fundeng value based on fmily members
g = sns.catplot(
    data = df,
    kind = "bar",
    x="Family members",
    y="Funding value",
    alpha = 1,
    palette=['#008080','#20B2AA', '#00CED1','#AFEEEE'] #colors pattren list
)

plt.title("Average funding value")
plt.xticks(rotation=45)
# Save the plot
plt.savefig('plot4.png',bbox_inches='tight')
plt.show()

#Fourth plot
# Change the size of the figure
plt.figure(figsize=(10,6)) 

#colors pattren list
mycolors = ['#20B2AA','#008080', '#00CED1','#AFEEEE']

#plot persentege of who ask fundings based on Social status
p= plt.pie(df["Social status"].value_counts(),labels=df["Social status"].value_counts().index,autopct='%.1f%%', colors= mycolors) # plot pink scatter plot

# add title and change color to black
plt.title("Funding value based on social status ", c="black") 
plt.savefig("plot5.png", bbox_inches = "tight")
plt.show() # show results

#Five plot
# Change the size of the figure
plt.figure(figsize=(10,6))
#colors pattren list
mycolors = ['#20B2AA','#008080', '#00CED1']
# plot fundeng type persentage with pie plot
p= plt.pie(df["Funding type"].value_counts(),labels=df["Funding type"].value_counts().index,autopct='%.1f%%', colors= mycolors) 
# add title and change color to black
plt.title("Funding type", c="black") 
#save plot as png image
plt.savefig("plot6.png", bbox_inches = "tight")
plt.show() # show results

# Six plot
# Change the size of the figure
plt.figure(figsize=(40,10)) 
#plot median of fundeng value based on costemer sector and gender 
sns.catplot(
    data = df,
    kind = "bar",
    x="Customer sector",
    y= "Funding value",
    hue = "Gender",
    alpha = 1,
    palette=['#008080','#00CED1']
)
plt.title("Avrage funding value based on customer sector")
plt.xticks(rotation=80)
plt.savefig('plot7.png',bbox_inches='tight')
plt.show()

# Create our One Hot Encoder object

one_hot = OneHotEncoder()

# One Hot encode the column
col_names = ['Bank branch', 'Funding classification', "Gender",'Installement value','Exchange date', 'Age','Social status','Special needs','Family members', 'Saving loan', "Customer sector","Funding type","Income"]
one_hot_df=one_hot.fit_transform(df[col_names]).toarray()

def col_names(one_hot_model):
    
    "Create columns names list for one hot encoded feature"
    
    column_names = []
    
    col_names = ['Bank branch', 'Funding classification', "Gender",'Installement value','Exchange date', 'Age','Social status','Special needs','Family members', 'Saving loan', "Customer sector","Funding type","Income"]
    for y in range(len(one_hot_model.categories_)):
        for z in range(len(one_hot_model.categories_[y])):
            # print(one_hot.categories_[y][z])
            column_names.append(col_names[y]+"_"+one_hot_model.categories_[y][z])
            
    return column_names

column_names = col_names(one_hot)

# Cast One Hot Encoded values into a dataframe
oh_df = pd.DataFrame(
    one_hot_df,
    index=df.index,
    columns = column_names
)

#baseline
pred = [df["Funding value"].mean() for x in range(len(df))]
mean_absolute_error(df["Funding value"], pred)

X = oh_df # Determining X values 
y = df["Funding value"] # Determining target value 

# Split train and test 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=13)

# Initializing the linear regression
Linear = LinearRegression()
Linear.fit(X_train, y_train)# fit train data
preds_Linear = Linear.predict(X_test) #Predicting X_test
#calculate mean absolute error
mean_absolute_error(y_test, preds_Linear)

#Initializing the lasso regressor with normalization factor as true
lasso_reg = Lasso(alpha=1.0 ,normalize=True)
lasso_reg.fit(X_train,y_train)#fit the train data 
preds_lasso =lasso_reg.predict(X_test)#Predicting X_test
#calculate mean absolute error
mean_absolute_error(y_test,preds_lasso)

#Initializing the ridge
ridge = Ridge()
ridge.fit(X_train, y_train)# fit train data
preds_ridge= ridge.predict(X_test)#Predicting X_test
#calculate mean absolute error
mean_absolute_error(y_test, preds_ridge)

#Initializing the Random Forest Regressor with 10 estimators  and mean absolute error criterion
class_forest = RandomForestRegressor(
    n_estimators = 10,
    criterion = 'mae',
    random_state = 0)

class_forest.fit(X_train, y_train) # fit train data
preds_forest = class_forest.predict(X_test)# prdict X_test
#calculate mean absolute error
mean_absolute_error(y_test, preds_forest)

#Initializing the SelectKBest with f_regression and K =30
select = SelectKBest(score_func=f_regression, k=30)
select_traing= select.fit_transform(X_train, y_train) #Fit to data train, then transform it.
select_test= select.transform(X_test) #transform X_test data

#Initializing the SVR 
model = SVR()
model.fit(select_traing,y_train)#fit train data
preds_SVR = model.predict(select_test)# predict select_test
#calculate mean absolute error
mean_absolute_error(y_test, preds_SVR)

#Initializing the KNeighborsRegressor
KNeighbors = KNeighborsRegressor()
KNeighbors.fit(X_train, y_train)# fit train data
preds_KNeighbors = KNeighbors.predict(X_test)# predict X_test
#calculate mean absolute error
mean_absolute_error(y_test, preds_KNeighbors)