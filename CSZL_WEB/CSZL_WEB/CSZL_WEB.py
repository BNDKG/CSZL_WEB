#coding=utf-8

from flask import Flask
import pandas as pd
from flask import request

app=Flask(__name__) 

@app.route('/')
def show_homepage():

    #if request.method == 'POST':
    #    if request.form['submit_button'] == 'THING1':
    #        print ("THING3")

    df=pd.read_csv('savetest2018.csv')
    
    table_html=df.to_html()
    buffer="<html><body><h1>HOME</h1>\
            <li><a href=\"/todayall\">SEE TODAY ALL</a></li>\
            <li><a href=\"/todayhave\">SEE TODAY HAVE</a></li><br>\
            <input type=\"submit\" name=\"submit_button\" value=\"THING1\">\
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

def order(method,inputpath,ordercol):
    outputname='savetest2019.csv'
    
    df=pd.read_csv('savetest2018.csv')
    df2=df.sort_values('vol',ascending=method)
    df2.to_csv(outputname)

    return outputname



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)