name=input("enter name")
if name=="priya singh":
	mobile=int(input("enter mobile"))
	if mobile==9305226297:
		gmail=input("enter your gmail")
		if gmail=="priyasingh2003@gmail.com":
			password=input("enter password")
			if password=="priya12@":
				print("login")
			else:
				print("wrong password")
		else:
			print("wrong gmail")
	else:
		print("wrong mobile no.")
else:
	print("wrong name")