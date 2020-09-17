# Seed File to make sample data for pets db

from models import Pet, db
from app import app

# create all tables
db.drop_all()
db.create_all()

# if table isnt empty, empty it
Pet.query.delete()

# add pets
whiskey = Pet(name='Whiskey', species='dog')
bowser = Pet(name='Bowser', species='dog', hunger=10)
spike = Pet(name='Spike', species='porcupine')

# add new objects to session, so they'll persisist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# commit -otherwise this never gets saved!
db.session.commit()
