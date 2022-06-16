import requests
from bs4 import BeautifulSoup
from database import SessionLocal
from models import Cars
import csv

URL = 'https://kolesa.kz/cars/toyota/highlander/shymkent/?auto-custom=2&year[from]=2012&year[to]=2014'
db = SessionLocal
base_url = 'https://kolesa.kz'

r = requests.get(URL)

soup = BeautifulSoup(r.text, 'lxml')

info = soup.findAll('div', class_='a-card__info')

for i in info:
    car_name = i.find(class_='a-card__link')
    title = i.find(class_='a-card__description')
    price = i.find(class_='a-card__price')
    date = i.find(class_='a-card__param a-card__param--date')
    link = i.find(class_='a-card__link').get('href')


    if price is not None:

        link = base_url + link
        item = db.query(Cars).filter(Cars.link == link)

        if item.count() == 0:
            s = price.text.replace(" ", "")[:-1]
            b = s.split()
            b = ''.join(b)

            new_item = Cars(name=car_name.text,
                            title=title.text.replace(" ", ""),
                            price=int(b),
                            link=link,
                            # year=int(title[:4]),
                            brand_id=1,
                            model_id=3)
            db.add(new_item)
            db.commit()





        #print(title.text.replace(" ", ""), price.text.strip(), date.text.strip())



