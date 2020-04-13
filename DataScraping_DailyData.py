from lxml import html
import requests
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame()
DayMth = np.array([[1, 31],[2,28],[3,31],[4,30],[5,31],[6,30],[7,31],[8,31],[9,30],[10,31],[11,30],[12,31]])
Data = np.zeros((1,7300))            


for year in np.arange(2000,2020):
    cnt = 0
    for month in np.arange(1,13):
        StrMth = str(month)
        if month < 10:
            StrMth = '0'+StrMth
    
        for day in np.arange(1,DayMth[month-1,1]+1):
                   StrDay = str(day)
                   if day < 10:
                       StrDay = '0'+StrDay  
                   page = requests.get('https://www.prevision-meteo.ch/climat/horaire/geneve-cointrin/'+str(year)+'-'+StrMth+'-'+StrDay)
                   tree = html.fromstring(page.content)
                   a = str(html.tostring(tree))
                   b1 = a[a.find('Precipitations totale'):-1]
                   b2 = b1[b1.find('min</td>')+6:-1]
                   b3 = b2[b2.find(';">')+3:b2.find(';">')+8]
                   if '<' in b3:
                       b3 = b3[0:b3.find('<')]
                   Data = float(b3)
                   s1 = pd.Series({'Year' : int(year),
                                   'Month' : int(month),
                                   'Day' : int(day),
                                   'Precipitation' : Data})
                   df = df.append([s1])


        print(str(year)+'-'+StrMth)

df.to_csv(r'PrecipitationGVA_daily.csv', index = False)