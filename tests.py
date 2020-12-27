import unittest

from app import app, db
from app.models import User


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='testName')
        u.set_password('goodPassword')
        self.assertFalse(u.check_password('wrongPassword'))
        self.assertTrue(u.check_password('goodPassword'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
