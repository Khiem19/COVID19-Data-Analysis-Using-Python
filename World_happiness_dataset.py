import pandas as pd 

#import the data set
happiness_report_csv = pd.read_csv("worldwide_happiness_report.csv")
# print(happiness_report_csv.head())

#delete useless columns
happiness_report_csv.drop(["Overall rank","Score","Generosity","Perceptions of corruption"],axis=1,inplace=True)
# print(happiness_report_csv.head())

#Changing indices of dataframe
happiness_report_csv.set_index("Country or region",inplace=True)

