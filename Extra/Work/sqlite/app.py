from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer,String, ForeignKey, Select
from sqlalchemy import select

from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    #articles = relationship('Article', secondary='article_authors')
    
    
class Article(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    content = Column(String)
    authors = relationship('User', secondary='article_authors')
    
class ArticleAuthors(Base):
    __tablename__ = 'article_authors'
    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    article_id = Column(Integer, ForeignKey('article.article_id'), primary_key=True)
    
    
engine = create_engine('sqlite:///./db.sqlite3')

if __name__ == '__main__':
    '''
    with Session(engine) as session:
        articles = session.query(Article).filter(Article.article_id == 1).all()
        for article in articles:
            print (article.title)
            for author in article.authors:
                print (author.username)
    '''
    #stmt = Select(User)
    #print (stmt)
    #with engine.connect() as conn:
    #    for row in conn.execute(stmt):
    #        print(row)
    
    with Session(engine, autoflush=False) as session:
        session.begin()
        try:
            article = Article(title='Article 1', content='My new article')
            session.add(article)
            session.flush()
            aa = ArticleAuthors(user_id=1, article_id=article.article_id)
            session.add(aa)
        except:
            print ('rolling back')
            session.rollback()
            raise
        else:
            print ('committing..')
            session.commit()