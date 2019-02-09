from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
'''
API END POINT FOR CREATING A PETITION
'''

'''
Define votes variable as an empty lits
'''
petitions = []

'''
Class Petition has two functions
1. get function that loops through the petitions and gives out the intended petition
2. Delete method that deletes a specified petition
'''
class Petition(Resource):
	'''
	Get a specific petition 
	'''
	def get(self,id):
		for petition in petitions:
			if petition['id'] == id:
				return petition
		return {'id':None}
	'''
	Delete a petition function
	'''
	def delete(self,id):
		for ind,petition in enumerate(petitions):
			if petition['id'] == id:
				deleted_petition = votes.pop(ind)
				return{'note':'delete success '}

'''
Class AddPetition is for adding a petition
It has 5 parameters and returns back the petition
'''
class CreatePetition(Resource):
	'''
	Add a peition method
	'''
	def post(self,id,createdOn,createdBy,office,body):
		petition = {
			'id':id,
			'createdOn':createdOn,
			'createdBy':createdBy,
			'office':office,
			'body':body
		}
		petitions.append(vote)
		return petition

'''
Class AllPetitions displays all petitions
returns all petitions
'''
class AllPetitions(Resource):
	def get(self): 
		return petitions

'''
api.add_resource defines our routes
'''
api.add_resource(Petition,'/vote/<int:id>')
api.add_resource(CreatePetition,'/vote/<int:id>/<string:createdOn>/<int:createdBy>/<string:office>/<string:body>')
api.add_resource(AllPetitions,'/all_voters')

if __name__ == '__main__':
	app.run(debug=True)
