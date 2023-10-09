# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 19:30:49 2023

@author: DELL
"""


#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
df=pd.read_csv("placement.csv")

#understanding the dataset
df.shape
df.columns
df.head()
df.tail()


#dist plot on cgpa and placement_exam_marks
plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
sns.distplot(df["cgpa"])
#age is fairly normally distributed

plt.subplot(1,2,2)
sns.distplot(df["placement_exam_marks"])
plt.show()
#right skewed

#2nd method
df["cgpa"].skew()
#-0.01452

df["placement_exam_marks"].skew()
#0.835

df["placement_exam_marks"].describe()
#mean =32, min=0, max=100, there can be outliers towards the right side

#boxplot
sns.boxplot(df["placement_exam_marks"])


#IQR
Q1=df["placement_exam_marks"].quantile(0.25)
Q1
#17
Q3=df["placement_exam_marks"].quantile(0.75)
Q3
#44

IQR=Q3-Q1
IQR
#27
#upper limit and lower limit?(Q3 and Q1)
upper_limit=Q3+1.5*IQR
upper_limit
#84.5

lower_limit=Q1-1.5*IQR
lower_limit
#-23.5


#any number beyond upper limit and lower limit will be outliers


#finding outlier
df[df["placement_exam_marks"]>upper_limit]
df[df["placement_exam_marks"]<lower_limit]

#techniques to treat outliers
#trimming

trimmed_df=df[df["placement_exam_marks"]<upper_limit]
trimmed_df

#check the boxplot
sns.boxplot(trimmed_df["placement_exam_marks"])

#capping
new_df_cap=df.copy()
new_df_cap

new_df_cap["placement_exam_marks"]=np.where(
    new_df_cap["placement_exam_marks"]>upper_limit,
    upper_limit,
    np.where(
        new_df_cap["placement_exam_marks"]<lower_limit,
             lower_limit,
             new_df_cap["placement_exam_marks"]
             )
    )


                                            
new_df_cap.shape
