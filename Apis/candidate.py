from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
'''
API END POINT FOR CREATING A USER
'''

'''
Define candidates variable as an empty list
'''
candidates = []

'''
Class candidates has two functions
1. get function that loops through the candidates and gives out the intended candidate
2. Delete method that deletes a specified candidate
'''
class Candidates(Resource):
	'''
	Get a candidate function
	'''
	def get(self,id):
		for candidate in candidates:
			if candidate['id'] == id:
				return candidate
		return {'id':None}
	'''
	Delete a candidate function
	'''
	def delete(self,id):
		for ind,candidate in enumerate(candidates):
			if candidate['id'] == id:
				deleted_user = users.pop(ind)
				return{'note':'delete success '}

'''
Class candidates is for adding a candidate
It has 4 parameters and returns back the candidate
'''
class AddCandidate(Resource):
	'''
	Add a candidate function
	'''
	def post(self,id,office,party,candidate):
		candidate = {
		'id':id,
		'office':office,
		'party':party,
		'candidate':candidate
		}
		candidates.append(candidate)
		return candidate

'''
Class Allcandidates displays all candidates
returns all candidates
'''
class AllCandidates(Resource):
	def get(self): 
		return candidates

'''
api.add_resource defines our routes
'''
api.add_resource(Candidates,'/cand/<int:id>')
api.add_resource(AddCandidate,'/cand/<int:id>/<int:office>/<int:party>/<int:candidate>')
api.add_resource(AllCandidates,'/all_cands')

if __name__ == '__main__':
	app.run(debug=True)
