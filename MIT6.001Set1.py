# #################
# #Problem Set 1
# #MIT OCW 6.001
# #Charlson So
# #################


# #Problem 1
# #---------------------------------------------------------------------------------------------
# #Paying the Minium:
# #Program that will find the amount left on your credit card after making minimum payments

# print('Find out the balance of your credit card after X amount of months!')

# princBal = float(raw_input('What is the balance you borrowed on your credit card? '))
# interRate = float(raw_input('What is the yearly interest rate on your credit card? (0.XX)'))
# minMonRate = float(raw_input('What minimum percentage will you make on your credit card? (0.XX)'))
# totalPaid = 0
# #calculates the monthly payment and interest payment, deducts interest from monthly pay and removes the remaining balance
# #from the principal. calculates the remaining balance after 12 months
# for x in range(1,13):
# 	print 'Month ' + str(x)
# 	monPay = round(minMonRate*princBal,2)
# 	totalPaid += monPay
# 	print 'Monthly Payment made is $' + str(monPay)
# 	monInt = round(princBal*interRate/12,2)
# 	print 'Montly Interest is $' +str(monInt)
# 	prinPay = monPay - monInt
# 	princBal -=prinPay
# 	print 'You will be making a principal payment of ' + str(prinPay) +' and your remaining balance is '+str(princBal)
# 	print '-----------------------'
# print '-----RESULT-----'
# print 'Total amount paid $'+str(totalPaid)
# print 'Remaining Balance $'+str(princBal)

# #Problem 2
# #-----------------------------------------------------------------------------------------------
# #Paying Debt Off In a Year

# print('Figure out how much your payments need to be to pay off your balance in a year')

# princBal = float(raw_input('What is the balance you borrowed on your credit card? '))
# interRate = float(raw_input('What is the yearly interest rate on your credit card? (0.XX)'))
# checkBal = princBal
# monthPay = 0
# month = 0
# while checkBal > 0:
# 	month = 0
# 	monthPay +=10
# 	checkBal = princBal
# 	while month <12 and checkBal>0:
# 		month +=1
# 		checkBal = checkBal + (interRate*checkBal/12) - monthPay

# print 'Monthly Payment to pay off debt in 1 year: ',monthPay
# print 'Number of months needed ', month
# print 'Balance: ', round(checkBal,2)

#Problem 3
#----------------------------------------------------------------------------------------------
#Paying Deb Off In a Year, Bisectional Search
print('Figure out how much your payments need to be to pay off your balance in a year')

princBal = float(raw_input('What is the balance you borrowed on your credit card? '))
interRate = float(raw_input('What is the yearly interest rate on your credit card? (0.XX)'))

#epsilion value which indicates that the low and high is close enough. the value should be the closest cent.
ep=0.005

#low would be paying a the balance in 12 equal installements which is a low estimate since interest is not accounted for
low = princBal/12
#high would be 12 payments compound interest paying nothing
#payment without paying any montly payments = initial principal *(total compound interest)/12
high = (princBal*((1+(interRate/12))**12))/12

#begin bisectional search
while True:
	balance = princBal
	payment = (low+high)/2
	monthPaid = 0

	for month in range(1,13):
		monthPaid +=1
		interestPayment = interRate*balance/12
		balance += interestPayment - payment
		if balance <= 0:
			break
	#debugging tests
	print 'Payment amount', payment
	print 'low', low
	print 'high', high
	print 'ep', high - low
	print balance
	print ''

	if (high - low) < ep and balance <0:
		print 'Result'
		print 'Montly payment to pay off debt in 1 year: ', payment
		print 'Number of months needed: ', month
		print 'Remaining Balance: ', balance
		break

	elif balance < 0:
		high = payment
	else:
		low = payment

