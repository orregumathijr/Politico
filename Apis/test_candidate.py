import unittest
import candidate

class TestUser(unittest.TestCase):
	'''
	Tests all users
	'''
	def test_get(self):
		text = {
		'id':id,
		'office':office,
		'party':party,
		'candidate':candidate
		}
		result = candidate.AllCandidates.get
		self.assertEqual(result,text)

	def test_post(self):
		text = {
		'id':id,
		'office':office,
		'party':party,
		'candidate':candidate
		}
		result = candidate.AddCandidate.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = candidate.Candidates.get
		self.assertEqual(result,text)

	def test_get(self):
		text = {'id': 1}
		result = candidate.Candidates.delete
		self.assertEqual(result,text)

if __name__ == '__main__':
	unittest.main() 