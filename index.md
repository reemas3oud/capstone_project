# SDA Capstone project

## Social Development Bank (Q1 of 2019)

The Social Development Bank was established in 1971. The bank’s objectives are focusing on social loans; over the years the services expanded to include business loans as well. One of the most important pillars of the Social Development Bank is to empower the citizens in the field of offering loans in a way that enables them to play an effective role in the community. The Social Development Bank dataset was taken from Saudi Open Data Portal. Here is the link: 
[Social Development Bank For 2019](https://data.gov.sa/Data/en/dataset/bank-loans-fo-2019/resource/e6d504c9-4aab-4e9b-b1e4-8cf38aba911f)

## Business Problem

Machine Learning in Data Science uses inputs from our daily lives and puts them in a process (or model), and then applies operations that the process has specified, and finally transforms them to outputs.

What is the funding value for a particular customer?
In our model we are predicting the funding value for a particular customer, based on the data provided in the Social Development Bank dataset.

After considering and exploring the customer information that has been provided to the Bank. We made a Linear Regression model that predicts the appropriate funding value that the customer is willing to get.OurLinear Regression model could help speed up the process for the Bank and shorten the time taken to finish it.

## Visualization

![First plot](https://github.com/reemas3oud/capstone_project/blob/main/plot2.png)


The line chart shows the exchange date for the first, second, and third months. As we see from the line chart, we noticed that females have higher funding value than male, but the bar chart shows the opposite!
Males have the most frequently requested funding values, but the average of the funding values by females was much higher.


![Second plot](https://github.com/reemas3oud/capstone_project/blob/main/plot3.png)

The bar chart shows the count of the age based on the range of the funding value. People with an age of greater than or equal to 30 have requested more than 66,000 SR, and they are the highest group of people who have requested loans

![Third plot](https://github.com/reemas3oud/capstone_project/blob/main/plot4.png)

The bar chart shows the average funding value based on family members. Families with less than 2 members have the highest average funding value, around 175,000 SR. Other families have the average between 50,000 SR and 75,000 SR.

![4th plot](https://github.com/reemas3oud/capstone_project/blob/main/plot5.png)

The pie chart shows the funding value based on social status. Married individuals have received the most funding value with a percentage of 86.3%.

![4th plot](https://github.com/reemas3oud/capstone_project/blob/main/plot6.png)

The pie chart shows the funding value based on funding type. Social fundings are the most requested fundings  with a percentage of 92.9%.

![5th plot](https://github.com/reemas3oud/capstone_project/blob/main/plot7.png)

The bar chart shows the average funding value based on customer sector and gender. Female governmental employees  have the highest average funding value, around 80,000 SR. Then the males   have lower  average funding values.

## Tableau Dashboard 
![Dashboard](https://lh6.googleusercontent.com/EyzSJwsTUhSJXKJ3Dn2LVovIVAjSwTUbRHtcRBQkFttAdX1ccMsHUjVyhh_3a--2alBs0JC1USU2gjSJTM0bl1XDKCw8ZrJekCLbLoPHndi2NkTiFPEwlkDCxRQEA6vCSLIa13E1)

The Tableau Dashboard illustrates information from our dataset. The map chart shows the total funding value based on every branch located in different cities in Saudi Arabia.
For further information about the dashboard, here is the link : 
[Tableau Dashboard](https://public.tableau.com/app/profile/shikhah/viz/SocialDevelopmentBankQ1of2019/DashboardofSocialBank)


## Model

After data exploring and cleaning we chose the target (funding value), and encoded the  categorical features as a one-hot numeric array then saved it inside a new dataframe. After that  we  created the baseline mean absolute error.

Baseline:

![Baseline](https://lh5.googleusercontent.com/a1UyqeXpa4QCOdyG26lb5J2hKT94UZ-gNC7BYsoN1O8C6O6FyJkn94kcYz9MGRLgoixyjIQwUFZIlWS5fgTVIHo12mCeOIBapUVljxEssSRX8pdDG4TwrogBqohgyVd62CO0JBXa)

Baseline value:

![Baseline value](https://lh6.googleusercontent.com/NgNoxE8kI5rboQ2XLZrMJWUepKkRTzGUkLccwJTxDf7XZY9UAfVLUIjoCIIfnQiNh-tWTIfgwG8IxamhPgwNmsbdmP0Azy7XaUEI6qDChFSZuIC9ok0WDKo72LW-p2HPolxRj_5z)


We chose 3 main models to predict the funding value and calculated the mean absolute error to compare and choose the best model for this data. 

The 3 main models are:

1- Lasso Regression: 
Lasso regression is a regularization technique. It is used over regression methods for a more accurate prediction. This model uses shrinkage. Shrinkage is where data values are shrunk towards a central point as the mean.

![Lasso Regression](https://lh3.googleusercontent.com/keep-bbsk/AGk0z-NeoOUgHo6Dne3dWwGGUOTsk9891QgiYW2F6YKcM5lusIm3EkE1ii7M2YrhUKqxBAvPtjkdTd6iNntk9FPiq5HruntlVOzYJgNOQW0)

