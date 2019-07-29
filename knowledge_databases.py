from knowledge_model import Base, Football

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Football.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_football(name, Ballon_dor, GOAT):

	football_object = Player(
		name=name,
		Ballon_dor=Ballon_dor,
		GOAT=GOAT)
	session.add(football_object)
	session.commit()

add_football("Messi",5, True)




def query_all_articles(input_data):
	football_all = session.query(
       Football).filter_by(
       name=input_data).all()
    return football_all   

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
