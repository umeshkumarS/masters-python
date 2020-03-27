import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import pandas as pd
import sys

engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# user = User("admin","password")
# session.add(user)

pd.options.display.max_rows = 999

df = pd.read_excel('masters-final.xlsx')
print(len(df))

for i in range(len(df)):
    r=df['REG.NO'][i]
    d=df['Date of Birth'].dt.date[i]
    r=str(r)
    d=str(d)
    user = User(r,d)
    session.add(user)
    session.commit()
    print(r,"\n",d)

#user = User("python","python")
#session.add(user)

user = User("umesh","umesh")
session.add(user)

# commit the record the database
session.commit()

session.commit()
