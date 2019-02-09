from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
'''
API END POINT FOR CREATING A PARTIES
'''

'''
Define parties variable as an empty lits
'''
parties = []

'''
Class AllParties displays all parties
returns all parties
'''
class AllParties(Resource):
	def get(self):
		return parties
'''
Class CreateParty is for adding a parties
It has 4 parameters and returns back the parties
'''
class CreateParty(Resource):
	def post(self,id,name,logo):
		party = {
		'id':id,
		'data':[{
			'name':name,
			'Logo Url':logo
			}]
		}
		parties.append(party)
		return party

'''
Class ManageParty has two functions
1. get function that loops through the parties and gives out the intended partY
2. Delete method that deletes a specified partY
'''
class ManageParty(Resource):
	'''
	Get a specific petition 
	'''
	def get(self,id):
		for party in parties:
			if party['id'] == id:
				return party
		return {'id':None}

	'''
	Delete a petition function
	'''
	def delete(self, id):
		for ind,party in enumerate(parties):
			deleted_party = parties.pop(ind)
			return{'note':'delete success '}

'''
api.add_resource defines our routes
'''
api.add_resource(AllParties,'/parties')
api.add_resource(CreateParty,'/party/<int:status>/<int:id>/<string:name>/<string:logo>')
api.add_resource(ManageParty,'/party/<int:id>')

if __name__ == '__main__':
	app.run(debug=True)