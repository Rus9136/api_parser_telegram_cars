from database import SessionLocal
from models import Cars, Models, Brands

db = SessionLocal
# c1 = models.Models(name='Highlander')
# db.add(c1)
# db.commit()


link = 'https://kolesa.kz/a/show/136803522'
item = db.query(Cars).filter(Cars.link == link)

#res = db.query(Cars.id, Cars.link, Cars.price, Models.id, Models.name).join(Models).join(Brands).filter(Cars.price>16000000).all()

if item.count() == 0:
    print('нет данных')
else:
    print(type(item))




# for c in res:
#     c.price = 32
#     db.add(c)
#     db.commit()
#
#     print(c.price, c.link, c.name)
#     pass





#filter(Cars.price > 180000)

d ='2013г.,Б/укроссовер,3.5л,бензин,КППавтомат,спробегом110000км,серый,металлик,литыедиски,тонировка,ве'


