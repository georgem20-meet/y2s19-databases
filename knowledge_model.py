from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Football(Base):
	__tablename__ = "Football"
	football_id= Column(Integer, primary_key = True)
	name = Column(String)
	Ballon_dor= Column(Integer)
	GOAT = Column(Boolean)


	def __repr__(self):
		return("Football name: {}\n"
			"Ballon_dor: {}\n"
			"GOAT: {}\n").format(
				self.name,
				self.Ballon_dor,
				self.GOAT)

# x = Football(name= "Cristiano Ronaldo", Ballon_dor= 5, GOAT= False)
# print(x)


	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	