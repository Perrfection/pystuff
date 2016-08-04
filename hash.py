from hashlib import *

longinDict = {}

def makeHash(password):
	return sha256(password.encode('utf-8')).hexdigest() 
	
def login(loginDict):
	
	
def prompt():
	question = input('Do you have a login? Type yes or no.')
		if input == "yes":
			print("Login")
			username = input("Username:")
			login(loginDict)
			if longinDict[username]:
				password = input("Password:")
				makeHash(password)
				login(loginDict)
				if longinDict[username] = passward
					true
				else:
				print("incorrect pasward")
			else:
				print("incorrect username")
		if input == "no"
			print("SignUp")
			username = input("Username:")
            login(loginDict)
			if longinDict[username]:
				print("username is taken try again")
			else:
				password = input("Password:")
				longinDict[username] = makeHash(password)
			
	 #prompt for username
	 # call login function
	# if user has login
		#check for username in dictionary
		# prompt for password
		# encrypt
		# check encrypted pw same as saved password
	# if user does not have a login, have them sign up
		#SignUp => username, password	
		#what function do I need to encrypt password
		# add username, encrpted pw to dictionay