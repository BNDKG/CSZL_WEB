#coding=utf-8

from flask import Flask
import pandas as pd
from flask import request

app=Flask(__name__) 

@app.route('/')
def show_homepage():


    try:
        df=pd.read_csv('Today_NEXT_predict_withindex.csv')
    
        table_html=df.to_html()
        buffer="<html><body><h1>HOME</h1>\
                <li><a href=\"/todayall\">SEE TODAY ALL</a></li>\
                <li><a href=\"/todayhave\">SEE TODAY HAVE</a></li><br>\
                </body></html>".format(table_html)

    except:
        buffer="something goes wrong!!!"

    return buffer
    

@app.route('/todayall', methods=['GET', 'POST'])
def show_todayall():

    if request.method == 'POST':
        if request.form['inputdate'] == 'aaa':
            print ("aaa")
        else:
            print ("bbb")

    df=pd.read_csv('Today_NEXT_predict_withindex.csv')
    page_name="TODAY ALL"
    table_html=df.to_html()
    buffer="<html><body><h1>{0}</h1><div>{1}</div>\
    <form method=\"post\">\
    inputdate<input name = \"inputdate\" type = \"text\" class=\"text\">\
    <button type=\"submit\">Do it!</button></form>\
    <li><a href=\"/\">BACK</a></li></body></html>".format(page_name,table_html)

    return buffer

@app.route('/todayhave')
def show_todayhave():
    df=pd.read_csv('Today_NEXT_predict_withindex.csv')
    page_name="TODAY HAVE"
    table_html=df.to_html()
    buffer="<html><body><h1>{0}</h1><div>{1}</div><li><a href=\"/\">BACK</a></li></body></html>".format(page_name,table_html)

    return buffer

def order(method,inputpath,ordercol):
    outputname='Today_NEXT_predict_changed.csv'
    
    df=pd.read_csv('savetest2018.csv')
    df2=df.sort_values('vol',ascending=method)
    df2.to_csv(outputname)

    return outputname



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)