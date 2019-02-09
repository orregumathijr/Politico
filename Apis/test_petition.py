import unittest
import petition

class TestUser(unittest.TestCase):
	'''
	Tests all candidates
	'''
	def test_get(self):
		text = {
			'id':id,
			'createdOn':createdOn,
			'createdBy':createdBy,
			'office':office,
			'body':body
		}
		result = petition.AllPetitions.get
		self.assertEqual(result,text)

	def test_post(self):
		text = {
			'id':id,
			'createdOn':createdOn,
			'createdBy':createdBy,
			'office':office,
			'body':body
		}
		result = petition.CreatePetition.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = petition.Petition.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = petition.Petition.delete
		self.assertEqual(result,text)

if __name__ == '__main__':
	unittest.main() 