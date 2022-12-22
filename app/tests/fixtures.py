import pytest
from auth import models


from auth import models
@pytest.fixture(scope='function')
def add_user(db_session): #db_session:db_session
    def _add_user(name, last_name):
        db_user = models.User(name=name,last_name=last_name)
        db_session.add(db_user)
        db_session.commit()
        return db_user
    return _add_user