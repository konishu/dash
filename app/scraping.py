from bs4 import BeautifulSoup
import requests
import datetime

import assets.database db_session
import assets.models Data

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
    
    _results = get_udemy_info('https://scraping-for-beginner.herokuapp.com/udemy')

    # 各要素を用意
    date = datetime.date.today()
    subscribers = _results['student']
    reviews = _results['reviews']
    
    row = Data(date=date,subscribers=subscribers,reviews=reviews)

    db_session.add(row)
    db_session.commit()

if __name__=="__main__":
    write_data()