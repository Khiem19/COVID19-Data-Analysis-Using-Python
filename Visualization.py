import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
import Joined_data as joined 

fig, axes = plt.subplots(2,2)

#Plotting GDP vs max infection rate
x1_ = joined.data["GDP per capita"]
y1_ = joined.data["max_infection_rate"]

sns.scatterplot(x=x1_,y=np.log(y1_),ax=axes[0, 0])

sns.regplot(x=x1_,y=np.log(y1_),ax=axes[0, 0])

#Social support vs maximum infection rate
x2_ = joined.data["Social support"]
y2_ = joined.data["max_infection_rate"]

sns.scatterplot(x=x2_,y=np.log(y2_),ax=axes[0, 1])

sns.regplot(x=x2_,y=np.log(y2_),ax=axes[0, 1])

#Healthy life expectancy vs MIR
x3_ = joined.data["Healthy life expectancy"]
y3_ = joined.data["max_infection_rate"]

sns.scatterplot(x=x3_,y=np.log(y3_),ax=axes[1, 0])

sns.regplot(x=x3_,y=np.log(y3_),ax=axes[1, 0])

#Freedom vs MIR
x4_ = joined.data["Freedom to make life choices"]
y4_ = joined.data["max_infection_rate"]

sns.scatterplot(x=x4_,y=np.log(y4_),ax=axes[1, 1])

sns.regplot(x=x4_,y=np.log(y4_),ax=axes[1, 1])


plt.show()

