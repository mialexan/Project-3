astate = 'Allstate'
pro = 'Progressive'
sfarm = 'State Farm'
lmut = 'Libery Mutual'
gei = 'Geico'
njm = 'New Jersey Manufacturers'

insurance = [astate, pro, sfarm, lmut, gei]

#Developing the quiz topics with questions for user to answer
ins = {
	
	astate: [

	('Male Teen: $2,137, Male Adult: $1,819, Male Senior: $1,468\nFemale Teen: $1,889, Female Adult: $1,759, Female Senior: $1,447\nAverage Car Insurance Rating: 4.02')

	],

	pro: [

	('Male Teen: $2,953, Male Adult: $1,523, Male Senior: $1,190\nFemale Teen: $2,706, Female Adult: $1,575, Female Senior: $1,143\nAverage Car Insurance Rating: 4.05')

	],

	sfarm: [

	('Male Teen: $1,967, Male Adult: $1,418, Male Senior: $1,062\nFemale Teen: $1,721, Female Adult: $1,418, Female Senior: $1,062\nAverage Car Insurance Rating: 4.12')

	],

	lmut: [

	('Male Teen: $3,199, Male Adult: $2,862, Male Senior: $2,588\nFemale Teen: $2,625, Female Adult: $2,845, Female Senior: $2,583\nAverage Car Insurance Rating: 3.94')

	]

	gei: [

	('Male Teen: $1,492, Male Adult: $1,204, Male Senior: $1,088\nFemale Teen: $1,460, Female Adult: $1,200, Female Senior: $1,079\nAverage Car Insurance Rating: 4.13')

	]

}

def ins_option():

	while True:
		try:
			ins_num = int(input('Please select the car insurance you want information on:\n1 for {}\n2 for {}\n3 for {}\n4 for {}\n5 for {}\nChoice:'.format(astate, pro, sfarm, lmut, gei)))
		except ValueError:
			print("Your input is not a number, please try again.\n")
		else:
			if 0 >= ins_num or ins_num > len(quiz):
				print("Invalid value, please try again.\n")
			else:
				return ins_num