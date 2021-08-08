def VerifyUser(ID, Pass):
	User = "YourName"
	Password = "ABCD1234!@#$"
	if (ID == User) and (Pass == Password):
		return True
	else:
		return False
choice = 1
if choice == 1:
	ID = "YourName"
	Pass = "ABCD1234!@#"
	# ID = input("Enter the User ID")
	# Pass = input("Enter Your Password")
	verified = VerifyUser(ID, Pass)
	print(verified)