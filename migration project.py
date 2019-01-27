# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 18:45:04 2019

@author: Radhey
"""



#open file containing data set and split the data to a list
file=open('cities_data_3.csv','r')
data=file.read()
data=data.split('\n')
data=set(data)
data=list(data)


for i in range(len(data)):
    data[i]=data[i].split(',')
country=[]
cities=[]
for i in range(len(data)):
        country.append(data[i][0])
        cities.append(data[i][1])
country_1=set(country)
country_1=list(country_1)
#store data in the dictionary
dict_cities={}
a=[]
for i in range(len(country_1)):
    for j in range(len(country)):
        if country_1[i]==country[j]:
            a.append(cities[j])
    dict_cities[country_1[i]]=a
    a=[]
    
