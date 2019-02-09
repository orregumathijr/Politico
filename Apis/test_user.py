import unittest
import user

class TestUser(unittest.TestCase):
	'''
	Tests all users
	'''
	def test_get(self):
		text = {
		'id':id,
		'data':[{
			'Firstname':firstname,
			'Lastname':lastname,
			'Othername':othername,
			'Email':email,
			'Phone Number':number,
			'Passport Url':passport
			}]
		}
		result = user.AllUsers.get
		self.assertEqual(result,text)

	def test_post(self):
		text = {
		'id':id,
		'data':[{
			'Firstname':firstname,
			'Lastname':lastname,
			'Othername':othername,
			'Email':email,
			'Phone Number':number,
			'Passport Url':passport
			}]
		}
		result = user.AddUser.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = user.Users.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = user.Users.delete
		self.assertEqual(result,text)

if __name__ == '__main__':
	unittest.main() 