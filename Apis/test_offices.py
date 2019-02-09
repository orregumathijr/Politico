import unittest
import offices

class TestUser(unittest.TestCase):
	'''
	Tests all votes
	'''
	def test_get(self):
		text = {
		'status':200,
		'id':id,
		'data':[{
			 'type':type,
			 'name':name
			}]
		}
		result = offices.AllOffices.get
		self.assertEqual(result,text)

	def test_post(self):
		text = {
		'status':200,
		'id':id,
		'data':[{
			 'type':type,
			 'name':name
			}]
		}
		result = offices.CreateOffice.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = offices.ManageOffice.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = offices.ManageOffice.delete
		self.assertEqual(result,text)

if __name__ == '__main__':
	unittest.main() 