import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
# print('Modules are imported.')

#import the data set#
corona_dataset_csv = pd.read_csv('covid19_Confirmed_dataset.csv')
# print(corona_dataset_csv.head(5))

#check the shape of csv
# print(corona_dataset_csv.shape)

#delete useless columns
corona_dataset_csv.drop(["Lat","Long","Province/State"], axis=1, inplace=True)
# print(corona_dataset_csv.head(10))

#Aggregating the rows by the countryside
cor_data_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
# print(cor_data_aggregated)
# print(cor_data_aggregated.shape)

#Visualizing data related to a country
# cor_data_aggregated.loc["Italy"].plot()
# cor_data_aggregated.loc["Spain"].plot()
# plt.legend()
# plt.show()

#Calculating a good measure
# cor_data_aggregated.loc["China"][:3].plot()
# plt.show()

#Calculatin and plotting the first deriative of curve
# cor_data_aggregated.loc["China"].diff().plot()
# plt.show()

#find maximum infection rate for China, Italy and Spain 
# print(cor_data_aggregated.loc["China"].diff().max())
# print(cor_data_aggregated.loc["Italy"].diff().max())
# print(cor_data_aggregated.loc["Spain"].diff().max())

#find maximum infection rate for all of the countries
countries = list(cor_data_aggregated.index)
max_infection_rate = []
for country in countries:
    max_infection_rate.append(cor_data_aggregated.loc[country].diff().max())
cor_data_aggregated["max_infection_rate"] = max_infection_rate
# print(cor_data_aggregated.head())

#create a data frame with only needed column
corona_data = pd.DataFrame(cor_data_aggregated["max_infection_rate"])
