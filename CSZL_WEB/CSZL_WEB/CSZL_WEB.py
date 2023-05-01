#coding=utf-8

from flask import Flask
import pandas as pd
from flask import request

app=Flask(__name__) 

@app.route('/')
def show_homepage():
    df=pd.read_csv('savetest2018.csv')
    
    table_html=df.to_html()
    buffer="<html><body><h1>HOME</h1>\
            <li><a href=\"/todayall\">SEE TODAY ALL</a></li>\
            <li><a href=\"/todayhave\">SEE TODAY HAVE</a></li>\
            </body></html>".format(table_html)

    return buffer
    

@app.route('/todayall')
def show_todayall():
    df=pd.read_csv('savetest2018.csv')
    page_name="TODAY ALL"
    table_html=df.to_html()
    buffer="<html><body><h1>{0}</h1><div>{1}</div><li><a href=\"/\">BACK</a></li></body></html>".format(page_name,table_html)

    return buffer

@app.route('/todayhave')
def show_todayhave():
    df=pd.read_csv('savetest2018.csv')
    page_name="TODAY HAVE"
    table_html=df.to_html()
    buffer="<html><body><h1>{0}</h1><div>{1}</div><li><a href=\"/\">BACK</a></li></body></html>".format(page_name,table_html)

    return buffer


app.run(host="127.0.0.1",port=5000)