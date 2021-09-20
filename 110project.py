import pandas as pd 
import csv 
import plotly.figure_factory as ff
import statistics
import random

df=pd.read_csv(r"C:\Users\ADMIN\New folder (3)\medium_data.csv")
data=df["claps"]
x1=statistics.mean(data)
print(x1)

dataset=[]
for i in range(0,100):
    set_of_mean=random.randint(0,len(data)-1)
    value=data[set_of_mean]
    dataset.append(value)


m1=statistics.mean(dataset)
print(m1)

st_dv1=statistics.stdev(dataset)
print(st_dv1)

fig=ff.create_distplot([dataset],["claps"],show_hist=False)
fig.show()


