#coding=utf-8

from flask import Flask
import pandas as pd
from flask import request
import waitress


app=Flask(__name__) 

@app.route('/')
def show_homepage():


    try:
        #df=pd.read_csv('Today_NEXT_predict_withindex.csv')
    
        #table_html=df.to_html()
        buffer="<html><body><h1>HOME</h1>\
                <li><a href=\"/todayall\">SEE TODAY ALL</a></li>\
                <li><a href=\"/todayhave\">SEE TODAY HAVE</a></li>\
                <li><a href=\"/todayfast\">SEE TODAY FAST</a></li><br>\
                </body></html>"

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

    df=pd.read_csv('Today_NEXT_predict_ALL.csv')
    page_name="TODAY ALL"
    table_html=df.to_html()
    buffer="<html><body><h1>{0}</h1>\
    <form method=\"post\">\
    inputdate<input name = \"inputdate\" type = \"text\" class=\"text\">\
    <button type=\"submit\">Do it!</button></form>\
    <li><a href=\"/\">BACK</a></li><br>\
    <div>{1}</div>\
    </body></html>".format(page_name,table_html)

    return buffer

@app.route('/todayhave')
def show_todayhave():
    df=pd.read_csv('Today_NEXT_predict_HOLD.csv')
    page_name="TODAY HAVE"
    table_html=df.to_html()
    buffer="<html><body><h1>{0}</h1><div>{1}</div><li><a href=\"/\">BACK</a></li></body></html>".format(page_name,table_html)

    return buffer


@app.route('/todayfast')
def show_todayfast():
    df=pd.read_csv('today_real_remix_result.csv')
    page_name="TODAY FAST"
    table_html=df.to_html()
    buffer="<html><body><h1>{0}</h1><div>{1}</div><li><a href=\"/\">BACK</a></li></body></html>".format(page_name,table_html)

    return buffer



# functions
def order(method,inputpath,ordercol):
    outputname='Today_NEXT_predict_changed.csv'
    
    df=pd.read_csv('savetest2018.csv')
    df2=df.sort_values('vol',ascending=method)
    df2.to_csv(outputname)

    return outputname

if __name__ == '__main__':
    inputpath="ipadd.txt"
    with open(inputpath, 'r', encoding='utf-8') as infile:
        ipadd=infile.readlines()
        print(ipadd)

    # debug
    #app.run(host=ipadd[0],port=5001)

    # real
    waitress.serve(app, host=ipadd[0], port='5001')