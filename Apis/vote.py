from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
'''
API END POINT FOR CREATING A VOTE
'''

'''
Define votes variable as an empty lits
'''
votes = []

'''
Class Voters has two functions
1. get function that loops through the votes and gives out the intended vote
2. Delete method that deletes a specified vote
'''
class Voter(Resource):
	'''
	Get a Votes function
	'''
	def get(self,id):
		for vote in votes:
			if vote['id'] == id:
				return vote
		return {'id':None}
	'''
	Delete a Vote function
	'''
	def delete(self,id):
		for ind,vote in enumerate(votes):
			if vote['id'] == id:
				deleted_voter = votes.pop(ind)
				return{'note':'delete success '}

'''
Class AddVote is for adding a vote
It has 5 parameters and returns back the vote
'''
class CreateVote(Resource):
	'''
	Add a vote function
	'''
	def post(self,id,createdOn,createdBy,office,candidate):
		vote = {
			'id':id,
			'createdOn':createdOn,
			'createdBy':createdBy,
			'office':office,
			'Candidate':candidate
		}
		votes.append(vote)
		return vote

'''
Class AllVoters displays all voters
returns all voters
'''
class AllVoters(Resource):
	def get(self): 
		return votes

'''
api.add_resource defines our routes
'''
api.add_resource(Voter,'/vote/<int:id>')
api.add_resource(CreateVote,'/vote/<int:id>/<string:createdOn>/<int:createdBy>/<string:office>/<string:candidate>')
api.add_resource(AllUsers,'/all_voters')

if __name__ == '__main__':
	app.run(debug=True)
