from typing import Collection
from pandas._config.config import option_context
from pandas.io.formats.style import Styler
import streamlit as st
import pandas as pd
from datetime import datetime as dt
import plotly.express as px

favicon = 'nfs.png'
st.set_page_config(page_title='NABFINS Thodupuzha', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')

xl_file = st.file_uploader("Choose a XLSX file", type="xlsx")

if xl_file == None:
    xl_file = 'trackDec21.xlsx'
sheet = 'COLLECTION AGAINST DEMAND'

option = st.sidebar.selectbox('What do you want to see?',('Collection Amount', 'Achievement Percentage'))


df=''
ydata=''
colname = ''
if(option == 'Collection Amount'):
    df = pd.read_excel(xl_file,sheet_name=sheet,usecols='A,E',header = 3,skipfooter=21)
    colname='AMOUNT.1'
    ydata='Amount'
if(option == 'Achievement Percentage'):
    df = pd.read_excel(xl_file,sheet_name=sheet,usecols='A,G',header = 3,skipfooter=21)
    colname='Amount %'
    ydata='Amount%'


month_data = pd.read_excel(xl_file, skiprows=0, usecols='A', nrows=1, header=None, names=["Value"]).iloc[0]["Value"]


#fmt = "%m-%Y"
#styler = month_data.style.format({"Value": lambda t: t.strftime(fmt)})
#styler = styler
#st.table(styler)





st.header("NABFINS")

sub1,sub2=st.columns(2)
sub1.subheader("Graph Data of: ")
sub2.subheader(month_data)

bar_chart = px.bar (
                    df, x="Unnamed: 0",labels={"Unnamed: 0":"Name","AMOUNT.1":ydata},
                    y = colname,text = colname,
                    #color_discrete_sequence= ['#0388fc']*len(df),
                    template= 'plotly_white',
                    width=900
                    )
bar_chart.update_layout(xaxis_title='Name', yaxis_title=ydata)

st.plotly_chart(bar_chart)



pie_chart = px.pie(df,title='PieChart for Collection',values=colname,labels={"Unnamed: 0":"Name","AMOUNT.1":ydata},names='Unnamed: 0')
st.plotly_chart(pie_chart)





