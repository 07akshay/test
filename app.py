#!/usr/bin/env python
# coding: utf-8

# In[58]:


import streamlit as st
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as mlt
import numpy as np
import smtplib, ssl
import re
# In[60]:


st.sidebar.write("""
# Enter your team name to know recent match results
""")
num=0
#st.write("\n")
name = st.sidebar.text_input("Enter team name : (e.g rcb)")
if name=='rcb':
    num=59
if name=='csk':
    num=58
if name=='dc':
    num=61
if name=='kkr':
    num=63
if name=='rr':
    num=64
if name=='pbks':
    num=65
if name=='srh':
    num=255
if name=='mi':
    num=62

page = requests.get("https://www.cricbuzz.com/cricket-team/l/"+str(num)+"/results")
soup = BeautifulSoup(page.text,"html.parser")

links = soup.findAll("a",class_="text-hvr-underline")
results = soup.findAll("a",class_="cb-text-complete")
for i in range(len(results)):
    link = links[i]
    result = results[i]
    if name == 'rcb':
        if result.text[1] == 'R' and result.text[2] == 'o':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
    if name == 'mi':
        if result.text[1] == 'M' and result.text[2] == 'u':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
    if name == 'srh':
        if result.text[1] == 'S' and result.text[2] == 'u':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
    if name == 'pbks':
        if result.text[1] == 'P' and result.text[2] == 'u':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
    if name == 'kkr':
        if result.text[1] == 'K' and result.text[2] == 'o':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
    if name == 'dc':
        if result.text[1] == 'D' and result.text[2] == 'e':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
    if name == 'csk':
        if result.text[1] == 'C' and result.text[2] == 'h':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
    if name == 'rr':
        if result.text[1] == 'R' and result.text[2] == 'a':
            st.sidebar.write(link.text + " : ")
            st.sidebar.success(result.text)
        else:
            st.sidebar.write(link.text + " : ")
            st.sidebar.error(result.text)
st.title("Enter team names for head to head stats")
st.write('\n')
name1 = st.text_input("Enter team1 e.g : rcb")
name2 = st.text_input("Enter team2 e.g : mi")
if name1=='rcb':
    num1=57
if name1=='csk':
    num1=58
if name1=='dc':
    num1=60
if name1=='kkr':
    num1=61
if name1=='rr':
    num1=64
if name1=='pbks':
    num1=63
if name1=='srh':
    num1=244
if name1=='mi':
    num1=62
dict={'rcb':'red','csk':'yellow','mi':'blue','dc':'#282968','srh':'orange','rr':'pink','pbks':'silver','kkr':'brown'}
team={'rcb':'bangalore','csk':'chennai','mi':'mumbai','dc':'delhi','srh':'hyderabad','rr':'rajasthan','pbks':'punjab','kkr':'kolkata'}
url = "https://www.mykhel.com/cricket/ipl-"+team[name1]+"-vs-"+team[name2]+"-head-to-head-s4/?team_id="+str(num1)
page = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page.text,"html.parser")
links = soup.findAll("div",class_="won-row")
score1 = soup.findAll("div",class_="won per")[0].text
score2 = soup.findAll("div",class_="won per-right")[0].text
col1=dict[name1]
col2=dict[name2]
color = [col1,col2]
#agains = [name1,name2]
#data = [score1,score2]
#mlt.pie(data, labels = agains,colors=color,shadow=True)

agains = [name1.upper(),name2.upper()]
data = np.array([score1,score2]).astype(np.float)
def func(pct, allvalues):
    absolute = round(1.0*pct*np.sum(allvalues) / 100.)
    return "{:.2f}%\n({:d} games)".format(pct, absolute)
wedges,texts, autotexts = mlt.pie(data, labels = agains,colors=color,shadow=True,autopct = lambda pct: func(pct, data))
# mlt.axis('equal')
mlt.legend(wedges, agains,
          title ="Teams",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
  
mlt.setp(autotexts, size = 8, weight ="bold")
mlt.title(name1.upper()+" vs "+name2.upper())
mlt.show()
fig = mlt.show()

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)
to_user = st.text_input("Enter email id if you wish to recieve stats via e mail")

g_user  = "72du123@gmail.com"
g_psd = "loyaldollar123"

sent_from = g_user
to = [to_user]
subject = 'Head to head IPL stats'
body = "Head to head stats for "+name1.upper()+" vs "+name2.upper()+" are as follows :\nTotal games played : "+str(int(score1)+int(score2))+"\n"+name1.upper()+" : "+str(score1)+"\n"+name2.upper()+" : "+str(score2)+"\n\nThank you for availing this service"
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
try:
    context = ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(g_user, g_psd)
        server.sendmail(g_user, to, email_text)
    st.success("Email sent successfully!!")
except:
    st.error("Sorry! could not send the mail")
# In[ ]:




