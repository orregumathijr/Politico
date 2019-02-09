import unittest
import party

class TestUser(unittest.TestCase):
	'''
	Tests all parties
	'''
	def test_get(self):
		text = {
		'id':id,
		'data':[{
			'name':name,
			'Logo Url':logo
			}]
		}
		result = party.AllParties.get
		self.assertEqual(result,text)

	def test_post(self):
		text = {
		'id':id,
		'data':[{
			'name':name,
			'Logo Url':logo
			}]
		}
		result = party.CreateParty.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = party.ManageParty.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = party.ManageParty.delete
		self.assertEqual(result,text)

if __name__ == '__main__':
	unittest.main() 