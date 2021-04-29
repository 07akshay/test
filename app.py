#!/usr/bin/env python
# coding: utf-8

# In[3]:
import streamlit as st
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import re
# In[60]:


st.write("""
# Enter your team name to know recent match results
"\n"
## This is akshay
""")
#st.write("\n")
name = st.text_input("Enter team name :")
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
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)
    if name == 'mi':
        if result.text[1] == 'M' and result.text[2] == 'u':
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)
    if name == 'srh':
        if result.text[1] == 'S' and result.text[2] == 'u':
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)
    if name == 'pbks':
        if result.text[1] == 'P' and result.text[2] == 'u':
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)
    if name == 'kkr':
        if result.text[1] == 'K' and result.text[2] == 'o':
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)
    if name == 'dc':
        if result.text[1] == 'D' and result.text[2] == 'e':
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)
    if name == 'csk':
        if result.text[1] == 'C' and result.text[2] == 'h':
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)
    if name == 'rr':
        if result.text[1] == 'R' and result.text[2] == 'a':
            st.write(link.text + " : ")
            st.success(result.text)
        else:
            st.write(link.text + " : ")
            st.error(result.text)

# In[ ]:

