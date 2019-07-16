# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data = pd.read_csv(path)
#print (data.head(2))
print (data.columns)
#Code starts here
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
print (data.columns)
print (data.head(10))



# --------------
#Code starts here

data['Better_Event'] = np.where(data['Total_Winter']<data['Total_Summer'],'Summer',np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter'))
print(data[['Total_Winter','Total_Summer','Better_Event']].head(3))
#cols = ['Country_Name','Total_Summer','Total_Winter','Better_Event']
#print(data.loc[data.Better_event=='Winter',cols].head(3).reset_index(drop=True))


better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)



# --------------
#Code starts here
cols_to_use=['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']
top_countries=data[cols_to_use]
#print (top_countries)
top_countries=top_countries.drop(top_countries.index[-1])

def top_ten(input_df,col_name):
    country_list=[]
    country_list = input_df.nlargest(10,col_name)['Country_Name'].tolist()
    return country_list
#print(top_countries.nlargest(10,'Total_Summer')['Country_Name'][:10].tolist())

top_10_summer = top_ten(top_countries,['Total_Summer'])
top_10_winter = top_ten(top_countries,['Total_Winter'])
top_10 = top_ten(top_countries,['Total_Medals'])
print (top_10_summer)
print (top_10_winter)
print (top_10)

common=list([i for i in top_10_summer if i in (top_10 and top_10_winter)])
print (common)



# --------------
#Code starts here

print (top_10_summer)
summer_df=data[data['Country_Name'].isin(top_10_summer)]
#,:].reset_index(drop=True)
#winter_df=data.loc[data.Country_Name.isin(top_10_winter),:].reset_index(drop=True)
winter_df=data[data['Country_Name'].isin(top_10_winter)]
#top_df=data.loc[data.Country_Name.isin(top_10),:].reset_index(drop=True)
top_df=data[data['Country_Name'].isin(top_10)]
#print(summer_df[['Country_Name','Total_Summer']])
plt.figure(figsize=(20,6))
plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.figure(figsize=(20,6))
plt.bar(winter_df['Country_Name'],summer_df['Total_Winter'])
plt.figure(figsize=(20,6))
plt.bar(top_df['Country_Name'],summer_df['Total_Medals'])
#fig,ax=plt.subplots(3,1,figsize=(22,30))
#summer_df.sort_values(by='Total_Summer',inplace=True)
#summer_df=summer_df.reset_index(drop=True)
#g1=summer_df.plot.bar(x='Country_Name',y='Total_Summer',ax=ax[0])
#for idx,row in summer_df.iterrows():
#    g1.text(idx,row['Total_Summer'],row['Total_Summer'])


#winter_df.sort_values(by='Total_Winter',inplace=True)
#winter_df=winter_df.reset_index(drop=True)
#g2=winter_df.plot.bar(x='Country_Name',y='Total_Winter',ax=ax[1])
#for idx,row in winter_df.iterrows():
#    g2.text(idx,row['Total_Winter'],row['Total_Winter'])

#top_df.sort_values(by='Total_Medals',inplace=True)
#top_df=top_df.reset_index(drop=True)
#g3=top_df.plot.bar(x='Country_Name',y='Total_Medals',ax=ax[2])
#for idx,row in top_df.iterrows():
#    g3.text(idx,row['Total_Medals'],row['Total_Medals'])

plt.show()





# --------------
#Code starts here

summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=max(summer_df['Golden_Ratio'])
print (summer_max_ratio)
summer_country_gold = summer_df.loc[summer_df.Golden_Ratio==summer_max_ratio,'Country_Name'].values[0]
print (summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=max(winter_df['Golden_Ratio'])
print (winter_max_ratio)
winter_country_gold = winter_df.loc[winter_df.Golden_Ratio==winter_max_ratio,'Country_Name'].values[0]
print (winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=max(top_df['Golden_Ratio'])
print (top_max_ratio)
top_country_gold = top_df.loc[top_df.Golden_Ratio==top_max_ratio,'Country_Name'].values[0]
print (top_country_gold)



# --------------
#Code starts here
data_1 = data.drop(data.index[-1])
data_1['Total_Points']=data_1.Gold_Total*3+data_1.Silver_Total*2+data_1.Bronze_Total*1


most_points=data_1['Total_Points'].max()
best_country=data_1.loc[data_1.Total_Points==most_points,'Country_Name'].values[0]
#print(data_1[data_1.Total_Points.]

print(most_points)
print(best_country)



# --------------
#Code starts here




best = data.loc[data.Country_Name==best_country,['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
#plt.figure(figsize=(15,7)

fig,ax=plt.subplots(figsize=(15,7))
best.plot.bar(stacked=True,color=['gold','silver','brown'],ax=ax)

plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
l=plt.legend()
l.get_texts()[0].set_text('Gold_Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver_Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze_Total :' + str(best['Bronze_Total'].values))






