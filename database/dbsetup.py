__author__ = 'Arjen'


def create():
    from database import Base, engine
    Base.metadata.create_all(engine)


def insert_test_values():
    from database import Session
    from database.objects import User, Address, BlogPost, Keyword
    from random import randint

    letters = 'abcdefghijklmnopqrstuvwxyz'

    s = Session()

    keyword = Keyword('firstpost')

    for n in range(100):
        name = ''
        for l in range(randint(4,10)):
            letter = letters[randint(0,len(letters)-1)]
            name += letter
        user = User(name=name, fullname=name, password='test')
        user.addresses = [
            Address(email_address=('%s@google.com' % name)),
            Address(email_address=('%s@yahoo.com' % name))]
        post = BlogPost(("%ss Blog Post" % name), "This is a test", user)
        post.keywords.append(Keyword(name))
        post.keywords.append(keyword)
        s.add(post)

    s.commit()
    s.close()
