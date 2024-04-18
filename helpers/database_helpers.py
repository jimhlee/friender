import random
from models import User
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def random_user_id(available_users):
    '''
    Gets a random user id from available users, returns 0 if no available user
    Takes a list of users, returns an integer. Integer willm be 0 if no available users
    '''
    if len(available_users) == 0:
        return 0

    random_id = random.choice(available_users)
    # Generate a random number between 1 and the total count of users

    return random_id

def get_users_in_radius(zip_codes):
    ''' Takes a list of zip codes, returns users in those zip codes '''


