import re
regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'




def checkPass() -> str:
	password = input("Enter Your Password: ")
	cPassword = input("Confirm Your Password: ")
	if password != cPassword:
		print("not match")
		checkPass()
	return password


		
def checkStr(string: str):
	if string == "" or string.isnumeric():
		print("Invalid Name !!")
		string = input(f"PLease Enter Your {string}  ")
		checkStr(string)
		
		
def checkMail(mail: str):
	if not re.search(regex,mail) :
		print("Invalid Email")
		m = input("Would You Enter Your mail: ")
		checkMail(m)

def checkPhone(ph: str):
	if not ph.isnumeric() or len(ph)<11:
		print("Invalid Format, please Enter Numbers Only and should be 11 digit")
		ph = input("Would You Enter Your Mobile PHone: ")
		checkPhone(ph)
	firstNum = ph[0:3]
	if  not firstNum == "010":
		if  not firstNum == "011":
			if  not firstNum == "012":
				print("You Should Enter Phone Number According to Egypt Country ")
				ph = input("Would You Enter Your Mobile PHone: ")
				checkPhone(ph)
	
	
def checkExistance(fn:str, ln:str) -> int:
	fullname = fn+ln
	check = 0
	try:
		f1 = open("userData.txt", 'r')
		
	except Exception as e:
		print(e)
	else:
		for x in f1:
			username = (x.split(' ')[0])
			if fullname == username:
				print("User Existnce, Try Another Name")
				return 0



  			

def regester():
	fname = input("PLease Enter Your first Name: ")
	checkStr(fname)	
	lname = input("Please Enter Your Last Name: ")
	checkStr(lname)
	existance = checkExistance(fname, lname)
	if existance == 0:
		regester()
	email = input("Would You Enter Your mail: ")
	checkMail(email)
	password = checkPass()
	mPhone = input("Would You Enter Your Mobile PHone: ")
	checkPhone(mPhone)
	
	try:
		afile = open("userData.txt", "a")
	except Exception as w:
		print(e)
	else:
		afile.writelines([fname+lname+" ", password+" ",email+" ", mPhone+" "])
		afile.writelines("\n")
		afile.close()
		
		
