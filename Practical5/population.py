# store the population of UK countries
# store the populations of the neighbouring provinces of Zhejiang
#Print	two	lists of sorted values using the data above for the populations of countries in the UK and Zhejiang-neighbouring provinces in China
# make two pie chart of the populations of countries in the UK and Zhejiang-neighbouring provinces in China
uk_countries=[57.11,3.13,1.91,5.45]
neighbouring_provinces=[65.77,41.88,45.28,61.27,81.15]
uk_countries_sort=sorted(uk_countries)
neighbouring_provinces_sort=sorted(neighbouring_provinces)#create new lists to store the sorted values
print(uk_countries_sort)
print(neighbouring_provinces_sort)
import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('Countries')
plt.ylabel('Population')
plt.title('Population of countries in the UK')
plt.pie(uk_countries,explode=(0.1,0,0,0),labels=['England','Scotland','Wales','Northern Ireland'],autopct='%1.1f%%')
plt.show()
plt.xlabel('Provinces')
plt.ylabel('Population')
plt.title('Population of neighbouring provinces of Zhejiang')
plt.pie(neighbouring_provinces,colors=['royalblue','skyblue','green','lightgreen','darkgreen'],explode=(0,0,0,0.1,0),labels=['zhejiang','Fujian','Jiangxi','Anhui','Jiangsu'],autopct='%1.1f%%')
plt.show()



# to draw two pictures into the same window
import matplotlib.pyplot as plt
import numpy as np
fig,(ax1,ax2)=plt.subplots(1,2)
ax1.set_title('Population of countries in the UK')
ax1.set_xlabel('Countries')
ax1.set_ylabel('Population')
ax1.pie(uk_countries,explode=(0.1,0,0,0),labels=['England','Scotland','Wales','Northern Ireland'],autopct='%1.1f%%')
ax2.set_title('Population of neighbouring provinces of Zhejiang')
ax2.set_xlabel('Provinces')
ax2.set_ylabel('Population')
ax2.pie(neighbouring_provinces,explode=(0,0,0,0.1,0),labels=['zhejiang','Fujian','Jiangxi','Anhui','Jiangsu'],autopct='%1.1f%%')
plt.tight_layout()#make the two pictures not overlap
plt.show()
