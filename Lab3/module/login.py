import os
from datetime import datetime

formatt = "%d-%m-%Y"


def checkSDate()->str:
	Date = input()
	try:
		res = bool(datetime.strptime(Date, formatt))
	except ValueError:
		res = False
	if res:
		return Date
	else:
		print("please write valid date i.e. 1-1-2020")
		checkSDate()
	
def fileExistance()->str:
	viewF = list(filter(os.path.isfile, os.listdir()))
	return viewF
	
def view():
	viewF = fileExistance()
	print(viewF)
	fileN = input("please enter your project's first name or date: ")
	listF = fileExistance()
	for i in listF:
		#print(i)
		if fileN in i:
			print(f"File with name {i} exist")
			try:
				fileA = open(i, 'r')
			except Exception as e:
				print(e)
			else:
				print("something")
				fileA.read()
				return		
	
def edit():
	fileN = input("please enter your project's first name or date: ")
	listF = fileExistance()
	for i in listF:
		#print(i)
		if fileN in i:
			print(f"File with name {i} exist")
			try:
				fileA = open(i, 'r+')
			except Exception as e:
				print(e)
			else:
				title = input("Set Title For Your Project: ")
				details = input("Details: ")
				target = input("Target Money: ")

				print("Put Start Date")
				sDate = checkSDate()
				print("Put End Date")
				eDate = checkSDate()
				print("Start Date:",sDate, "\nEnd Date: ",eDate)
				fileA.truncate(0)
				fileA.writelines([title+"\n", details+"\n", target+"\n", sDate+"\n", eDate+"\n"])
				newName = title.split(' ')[0]+" "+sDate+".txt"
				os.rename(i, newName)
				fileA.close()
				return		
		print("File Not Exist")
	
def delete():
	view()
	fName = input("Please Enter File Name: ")
	try:
		os.remove(fName)
	except Exception as e:
		print(e)
	else:
		print(view())
		
def search():
	fileN = input("please enter your project's first name or date: ")
	listF = fileExistance()
	for i in listF:
		if fileN in i:
			print("File Exist")
		else:
			print("File Not Exist")
	

def create():
	title = input("Set Title For Your Project: ")
	details = input("Details: ")
	target = input("Target Money: ")

	print("Put Start Date")
	sDate = checkSDate()
	print("Put End Date")
	eDate = checkSDate()
	print("Start Date:",sDate, "\nEnd Date: ",eDate)
	
	resED = bool(datetime.strptime(sDate, formatt))
	pname = title.split(' ')[0]+" "+sDate+".txt"
	
	try:
		afile = open(pname, 'w')
	except Exception as e:
		print(e)
	else:
		afile.writelines([title+"\n", details+"\n", target+"\n", sDate+"\n", eDate+"\n"])
		afile.close()

				
def pFiles():
	while True:
		inp = input("hit v to view, e to edit, d to delete, s to search, c to create, x to exit: ")
		if inp == "v":
			view()
		elif inp == "e":
			edit()
		elif inp == "d":
			delete()
		elif inp == "s":
			search()
		elif inp == "c":
			create()
		elif inp == "x":
			exit()
		

def login():    
	un = input("Please Enter Your Full Name: ")
	pa = input("Please Enter Your Password: ")
	
	check = 0
	try:
		f1 = open("userData.txt", 'r')
		
	except Exception as e:
		print(e)
	else:
		for x in f1:
			username = (x.split(' ')[0])
			password = (x.split(' ')[1])
			if un == username:
				if pa == password:
					print("login Successfully")
					pFiles()

  			
