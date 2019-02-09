from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
'''
API END POINT FOR CREATING A USER
'''

'''
Define users variable as an empty lits
'''
users = []

'''
Class Users has two functions
1. get function that loops through the users and gives out the intended user
2. Delete method that deletes a specified user
'''
class Users(Resource):
	'''
	Get a user function
	'''
	def get(self,id):
		for user in users:
			if user['id'] == id:
				return user
		return {'id':None}
	'''
	Delete a user function
	'''
	def delete(self,id):
		for ind,user in enumerate(users):
			if user['id'] == id:
				deleted_user = users.pop(ind)
				return{'note':'delete success '}

'''
Class AddUser is for adding a user
It has 7 parameters and returns back the user
'''
class AddUser(Resource):
	'''
	Add a user function
	'''
	def post(self,id,firstname,lastname,othername,email,number,passport):
		user = {
		'status':200,
		'id':id,
		'data':[{
			'Firstname':firstname,
			'Lastname':lastname,
			'Othername':othername,
			'Email':email,
			'Phone Number':number,
			'Passport Url':passport
			}]
		}
		users.append(user)
		return user

'''
Class AllUsers displays all users
returns all users
'''
class AllUsers(Resource):
	def get(self): 
		return users

'''
api.add_resource defines our routes
'''
api.add_resource(Users,'/user/<int:id>')
api.add_resource(AddUser,'/user/<int:id>/<string:firstname>/<string:lastname>/<string:othername>/<string:email>/<int:number>/<string:passport>')
api.add_resource(AllUsers,'/all_users')

if __name__ == '__main__':
	app.run(debug=True)
