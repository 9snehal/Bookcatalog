from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Create category of Scienec Fiction
category1 = Categories(user_id=1,name="Science Fiction Books")
session.add(category1)
session.commit()


# Create category of Drama
category2 = Categories(user_id=1,name="Drama Books")
session.add(category2)
session.commit()

# Create category of Action and Adventure
category3 = Categories(user_id=1,name="Action and Adventure Books")
session.add(category3)
session.commit()

# Create category of Mystery
category4 = Categories(user_id=1,name="Mystery Books")
session.add(category4)
session.commit()

# Create category of cookbooks
category5 = Categories(user_id=1,name="CookBooks")
session.add(category5)
session.commit()

# Create category of Biography
category6 = Categories(user_id=1,name="Biography Book")
session.add(category6)
session.commit()

# Create category of Self Help
category7 = Categories(user_id=1,name="Self Help Books")
session.add(category7)
session.commit()

# Create category of Poetry Book
category8 = Categories(user_id=1,name="Poetry Book ")
session.add(category8)
session.commit()

# Create category of comics
category9 = Categories(user_id=1,name="Comics Books")
session.add(category9)
session.commit()

# Create category of Yoga
category10 = Categories(user_id=1,name="Yoga Books")
session.add(category10)
session.commit()

# Add Items into categories
categoryItem1 = CategoryItem(user_id=1,name="The Nectar of Pain",
                             description="The Nectar of Pain is a collection of poetry and prose that \
                             the pain of love and loss gave birth to. When pain knocks on your door, \
                             let it in. If you don't, \
                             it will knock harder and harder.",
                              price="$2.99",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="The Secret",
                             description="The Secret is a best-selling 2006 self-help book by Rhonda Byrne, \
                             based on the earlier film of the same name. It is based on the law of attraction, \
                             which claims that thoughts can change the world directly",
                             price="$3.00",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Yoga As Medicine",
                             description="The definitive book of yoga therapy, \
                              this groundbreaking work comes to you from the medical editor \
                               of the country's premier yoga magazine, \
                              who is both a practicing yogi and a Western-trained physician.",
                             price="$3.99",
                             categories=category10)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="The Dark Lake",
                             description="The lead homicide investigator in a rural town,\
                              Detective Sergeant Gemma Woodstock is deeply unnerved when a high \
                              school classmate is found strangled, her body floating in a lake. .",
                              price="$3.35",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Harry Potter and the Deadly Hallows",
                             description="The story follows Harry Potter,\
                             who has been tasked by Dumbledore, with finding and destroying \
                             Lord Voldemors.",
                             price="$4.00",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Heart Talk",
                             description="A poet, artist, and speaker, Cleo Wade has carved out a reputation \
                             as the voice of a generation blending positivity with arresting honesty to inspire people of all ages. \
                              With Heart Talk, she's poured her spiritually and poetically infused wisdom \
                               into an accessible book you won't want to be ",
                             price="$2.00",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Joy of Cooking",
                             description="Joy of Cooking, often known as The Joy of Cooking, \
                             is one of the United States' most-published cookbooks. \
                             It has been in print continuously since 1936 and has sold more than 18 million copies.",
                             price="$3.34",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Steve Jobs",
                             description="Steve Jobs is the authorized self-titled biography book of Steve Jobs.\
                              The book was written at the request of Jobs by Walter Isaacson, a former executive at CNN and \
                              TIME who has written best-selling biographies of Benjamin Franklin and Albert Einstein.",
                               price="$2.25",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="The Green Lantern Corps",
                             description="The Green Lantern Corps is the name of a fictional intergalactic military/police force \
                              appearing in comics published by DC Comics. \
                              They patrol the farthest reaches of the DC Universe at the behest of the Guardians, \
                               a race of immortals residing on the planet Oa",
                             price="$3.00",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="The Apollo Illusion",
                             description="The Apollo Illusion is the story for the hackers,\
                              the techies, the seekers, and the rebels of the world.",
                             price = "$4.00",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Gone Girl",
                             description="Gone Girl is a thriller novel by the writer Gillian Flynn \
                              It was published by Crown Publishing Group in June 2012.",
                              price="$5.00",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="All about Cake",
                             description="In Milk Bar: All About Cake,it shows all receipes of cake",
                             price="$4.00",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="The Story of My Experiments with Truth",
                             description="The Story of My Experiments with Truth is the autobiography of \
                              Mohandas K. Gandhi, covering his life from early childhood through to 1921 \
                               It was written in weekly instalments and published in his journal Navjivan from 1925 to 1929. ",
                             price="$4.00",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Spider-Verse",
                             description="Spider-Verse is a 2014 comic book storyline published by Marvel Comics\
                              It features multiple alternative versions of Spider-Man that had appeared in various media, \
                             all under attack by Morlun and his family, the Inheritors.",
                               price="$3.65",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Fahrenheit 451",
                             description="Fahrenheit 451 is a dystopian novel by American writer \
                              Ray Bradbury, published in 1953 \
                              the temperature at which book paper catches fire and burns.",
                              price="$2.99",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Twelve Angry Men",
                             description="Twelve Angry Men is a landmark American drama,\
                             that inspire a classic film and broadway revival-\
                             featuring an itroduction by David Mamet.",
                              price="$3.99",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Think and Grow Rich",
                             description="Think and Grow Rich was written in 1937 by Napoleon Hill, \
                              promoted as a personal development and self-improvement book. \
                              Hill writes that he was inspired by a suggestion from business magnate \
                              and later-philanthropist Andrew Carnegie.",
                             price="$4.00",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,name="Life of Pi",
                             description="Life of Pi is the canadian fantacy adventure novel \
                             by Yann Martel published in 2001.",
                             price="$2.75",
                             categories=category3)
session.add(categoryItem1)
session.commit()

print "added category items!"
