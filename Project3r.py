#import webbrowser

astate = 'Allstate'
pro = 'Progressive'
sfarm = 'State Farm'
lmut = 'Libery Mutual'
gei = 'Geico'

insurance = [astate, pro, sfarm, lmut, gei]

ins = {

astate: [

("The average price of insurance for Males using Allstate is:\n\n Male Teen: $2,137\n Male Adult: $1,819\n Male Senior: $1,468\n\n The average price of insurance for Females using Allstate is:\n\n Female Teen: $1,889\n Female Adult: $1,759\n Female Senior: $1,447\n\n The average car insurance rating for Allstate is: 4.02\n\n If you would like more information, Allstate's website is: www.allstate.com\n")

],

pro: [

("The average price of insurance for Males using Progressive is:\n\n Male Teen: $2,953\n Male Adult: $1,523\n Male Senior: $1,190\n\n The average price of insurance for Females using Progressive is:\n\n Female Teen: $2,706\n Female Adult: $1,575\n Female Senior: $1,143\n\n The average car insurance rating for Progressive is: 4.05\n\n If you would like more information, Progressive's website is: www.progressive.com\n")

],

sfarm: [

("The average price of insurance for Males using State Farm is:\n\n Male Teen: $1,967\n Male Adult: $1,418\n Male Senior: $1,062\n\n The average price of insurance for Females using State Farm is:\n\n Female Teen: $1,721\n Female Adult: $1,418\n Female Senior: $1,062\n\n The average car insurance rating for State Farm is: 4.12\n\n If you would like more information, State Farm's website is: www.statefarm.com\n")

],

lmut: [

("The average price of insurance for Males using Liberty Mutual is:\n\n Male Teen: $3,199\n Male Adult: $2,862\n Male Senior: $2,588\n\n The average price of insurance for Females using Libery Mutual is:\n\n Female Teen: $2,625\n Female Adult: $2,845\n Female Senior: $2,583\n\n The average car insurance rating for Liberty Mutual is: 3.94\n\n If you would like more information, Liberty Mutual's website is: www.libertymutual.com\n")

],

gei: [

("The average price of insurance for Males using Geico is:\n\n Male Teen: $1,492\n Male Adult: $1,204\n Male Senior: $1,088\n\n The average price of insurance for Females using Geico is:\n\n Female Teen: $1,460\n Female Adult: $1,200\n Female Senior: $1,079\n\n The average car insurance rating for Geico is: 4.13\n\n If you would like more information, Geico's website is: www.geico.com\n")

]

}

def ins_option():

	while True:
		try:
			ins_num = int(input('\n Please select the car insurance you want information on:\n\n 1 for {}\n 2 for {}\n 3 for {}\n 4 for {}\n 5 for {}\n\n Choice:'.format(astate, pro, sfarm, lmut, gei)))
		except ValueError:
			print("Your input is not a number, please try again.\n")
		else:
			if 0 >= ins_num or ins_num > len(ins):
				print("Invalid value, please try again.\n")
			else:
				return ins_num

option = ins_option()
ins_name = insurance[option - 1]

print("\n Ok, here is information about {}:\n\n {}".format(ins_name,ins[ins_name][0]))

restart = input(" Would you like to look at other car insurance companies? Please enter y/n: ").lower()
while restart == "y":

	option = ins_option()
	ins_name = insurance[option - 1]

	print("\n Ok, here is information about {}:\n\n {}".format(ins_name,ins[ins_name][0]))

	restart = input(" Would you like to look at other car insurance companies? Please enter y/n: ").lower()