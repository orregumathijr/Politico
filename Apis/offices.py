from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
'''
API END POINT FOR CREATING A OFFICES
'''

'''
Define offices variable as an empty lits
'''
offices=[]
'''
Class AllOffices displays all offices
returns all offices
'''
class AllOffices(Resource):
	def get(self):
		return offices
'''
Class CreateOffice is for adding a offices
It has 4 parameters and returns back the offices
'''
class CreateOffice(Resource):
	def post(self,id,type,name):
		office = {
		'status':200,
		'id':id,
		'data':[{
			 'type':type,
			 'name':name
			}]
		}
		offices.append(office)
		return office
'''
Class ManageOffice has two functions
1. get function that loops through the offices and gives out the intended office
2. Delete method that deletes a specified office
'''
class ManageOffice(Resource):
	'''
	Get a specific office
	'''
	def get(self,id):
		for office in offices:
			if office['id'] == id:
				return office
		return{'id':None}
	'''
	Delete a petition function
	'''
	def delete(self, id):
		for ind,office in enumerate(offices):
			deleted_office = offices.pop(ind)
			return{'note':'delete success '}


api.add_resource(AllOffices,'/offices')
api.add_resource(CreateOffice,'/office/<int:id>/<string:type>/<string:name>')
api.add_resource(ManageOffice,'/office/<int:id>')

if __name__ == '__main__':
	app.run(debug=True)