import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
from bokeh.plotting import figure
import xlrd


st.title('App for data of PhDs awarded in the US')
st.write(""" 

	## Table 1

Oroginal data of Doctorate recipients from U.S. colleges and universities: 1958–2017



	""")

df = pd.read_excel('sed17-sr-tab001.xlsx',skiprows = 3)
df.iloc[:,2][0] = 0
df.iloc[:,2][18] = 0
df

st.write(""" 

	## Figure 1

This plot shows the number of Doctorate recipients from 1958 - 2017



	""")


fig, ax = plt.subplots()
ax.scatter(x = df.iloc[:,0],y = df.iloc[:,1])
ax.set_title('Number of Doctorate Recipients')
st.pyplot(fig)






st.write(""" 

	## Figure 2

This plot shows the percentage of change from previous of # of Doctorate recipients from 1958 - 2017



	""") 


fig2, ax2 = plt.subplots()
ax2.plot(df.iloc[:,0],df.iloc[:,2])
ax2.set_title('Number of e Recipients')
st.pyplot(fig2)





