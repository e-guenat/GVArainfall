from lxml import html
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

year in np.arange(2000,2020):
    Data = np.zeros((1,12))
    cnt = 0
    for month in np.arange(1,13):
        StrMth = str(month)
        if month < 10:
            StrMth = '0'+StrMth
            
        page = requests.get('https://www.prevision-meteo.ch/climat/journalier/geneve-cointrin/'+str(year)+'-'+StrMth)
        tree = html.fromstring(page.content)
        a = str(html.tostring(tree))
        b1 = a[a.find('Total'):-1]
        b2 = b1[b1.find('min'):-1]
        b3 = b2[b2.find('<td>')+4:b2.find('<td>')+8]
        if '<' in b3:
            b3 = b3[0:b3.find('<')]
        Data[0,cnt] = float(b3)
        cnt+=1
    Yr = pd.Series({'1': Data[0,0],
                      '2' : Data[0,1],
                      '3' : Data[0,2],
                      '4' : Data[0,3],
                      '5' : Data[0,4],
                      '6' : Data[0,5],
                      '7' : Data[0,6],
                    '8' : Data[0,7],
                    '9' : Data[0,8],
                    '10' : Data[0,9],
                    '11' : Data[0,10],
                    '12' : Data[0,11]})
    df =    pd.DataFrame([Yr], index=[str(year)])
    df1 = df1.append(df)
    print(year)
df1 = df1.drop('0')  

df1.to_csv(r'PrecipitationGVA_month.csv', index = True)

