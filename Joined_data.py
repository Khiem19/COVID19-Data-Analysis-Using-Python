import pandas as pd
import Corona_dataset as Corona
import World_happiness_dataset as happiness

#Join 2 datasets
data = Corona.corona_data.join(happiness.happiness_report_csv,how="inner")

#correlation matrix
correlation = data.corr()




