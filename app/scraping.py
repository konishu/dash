from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime

def get_udemy_info(url) :
    requests.get(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
#     各要素の取得
    name = soup.select('.card-title')[0].string
    student = soup.select('.subscribers')[0].string
    student = int(student.split('：')[1])
    reviews = soup.select('.reviews')[0].string
    reviews = int(reviews .split('：')[1])
#     取得したデータをリストに収納
    results = {
    'name':name,
    'student':student,
    'reviews':reviews,
    }
    
    return results



def write_data():
    df = pd.read_csv('assets/data.csv')
    _results = get_udemy_info('https://scraping-for-beginner.herokuapp.com/udemy')

    # 各要素を用意
    date = datetime.datetime.today().strftime('%Y/%-m/%-d')
    subscribers = _results['student']
    reviews = _results['reviews']
    # データフレームの形にする
    results = pd.DataFrame([[date,subscribers,reviews]], columns=['date','subscribers','reviews'])
    # データの結合
    df = pd.concat([df,results])
    # データの出力
    df.to_csv('assets/data.csv',index='False')

if __name__=="__main__":
    write_data()