print ('Welcom to M-Smart')

groceries = {}

def creat_list():
	choice = input("Would you like to add an iteam? Type Y or N:")
	if choice == "Y":
		add_item
	else:
		print_list
		
def add_item():
	item = input("What would you like to add?")
	quantity = ("How many " + item + "s would you like to add?")
	groceries[item] = quantity
	
def update_item():
	item = input("What would like to update?")
	if items in groceries:
		quantity = input("How many " + item + "s would you like to add?")
		groceries[item] = quantity
	else:
		print (item + "not found.")
		new_item = input ("Would you like to add it to your list? Type Y or N:")
		if new_item == "Y":
			add_item()
	
def delete_item():
	item = input("What would like to delete?")
	del greceries[item] 	
	
def print_list():
	choice = input("Would you like to print receip? Type Y or N:")
	
creat_list()
add_iteam()