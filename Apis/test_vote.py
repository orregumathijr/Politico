import unittest
import vote

class TestUser(unittest.TestCase):
	'''
	Tests all votes
	'''
	def test_get(self):
		text = {
			'id':id,
			'createdOn':createdOn,
			'createdBy':createdBy,
			'office':office,
			'Candidate':candidate
		}
		result = vote.AllVoters.get
		self.assertEqual(result,text)

	def test_post(self):
		text = {
			'id':id,
			'createdOn':createdOn,
			'createdBy':createdBy,
			'office':office,
			'Candidate':candidate
		}
		result = vote.Createvote.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = vote.Voter.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = vote.Voter.delete
		self.assertEqual(result,text)

if __name__ == '__main__':
	unittest.main() 