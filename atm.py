import time

gtBankClient = {
    'Ayomide' : 1234,
    'David' : 4567,
    'Cynthia' : 8999,
    'Olaitan' : 2020

}
firstClient =  {
    'Timileyin' : 6687,
    'Abigiel' : 9872,
    'Body' : 6666,
    'Omotola' : 9090

}

ecoClient = {
    'James' : 1111,
    'Olaitan' : 2020,
    'Marain' : 3434     
}
stanbicClient = {
	'James':1111,
	'Queen':6868,
    'Ade':7867	


}
accessBankClient = {
    'Otunba':8999,
    'Chris':7456
}
balances = {
    'Ayomide' : 6000,
    'David' : 90000,
    'Cynthia' : 800000,
    'Otunba' : 50000,
    'Chris' : 60000,
    'James' : 1000000000,
    'Olaitan' : 5,
    'Queen' : 300000,
    'Ade' : 500000,
    'Timileyin' : 50000000000000
    
}

restart = 'y'
count = 4
class atm():

    def gtBank():
        counting = 4
        print('''
   ____ _____   ____    _    _   _ _  __
  / ___|_   _| | __ )  / \  | \ | | |/ /
 | |  _  | |   |  _ \ / _ \ |  \| | ' / 
 | |_| | | |   | |_) / ___ \| |\  | . \ 
  \____| |_|   |____/_/   \_\_| \_|_|\_\
                                        
''' )
        while counting > 0:
            counting -= 1
            print('\nTrials remaining: ', counting)
            print('\nYou Can Type in (b or back or B or BACK ) in the FIRST NAME,if you are in the wrong bank to choose bank again')
            print('\nWELCOME TO GT BANK')
            name = str(input('\nENTER YOUR FIRST NAME: '))
            if name in ('b','B','back','Back','BACK'):
            	break
            capitalize = name.capitalize()
            pin = int(input('PIN:  '))
            if capitalize in gtBankClient and  gtBankClient[capitalize] == pin:
                print('\nWELCOME BACK TO GT BANK %s'%(name))
                restart = 'Y'
                while restart not in ('n','no','No','NO'):
                    gtInput = input('\n 1: CASH TRANSACTION\t\t 2: ACCOUNT BALANCE\n '
                          '3: CUSTOMER SERVICE\t\t 4: EXIT\n '
                          '\nPLEASE INSERT THE NUMBER OF TRANSACTION TO PERFORM: ')
                    if gtInput == '1':
                        date = time.asctime(time.localtime(time.time()))
                        print('\n1: WITHDRAW CASH\t\t\t 2: TRANSFER CASH \t\t\t 3: DEPOSIT')
                        cashInput = input('\nINSERT NUMBER OF TRANSACTION TO PERFORM:  ')
                        if cashInput == '1':
                                withdraw = int(input('ENTER AMOUNT TO WITHDRAW:   #'))
                                if withdraw > balances[capitalize]:
                                    print('\nYOU ARE NOT ELIGIBLE FOR OVERDRAFT')
                                elif withdraw <= balances[capitalize]:
                                    balances[capitalize] = balances[capitalize] - withdraw
                                    print("\nYOUR BALANCE AS AT  %s IS # %i" % (date, balances[capitalize]))
                                    restart  = input('DO YOU WANT TO PERFORM ANOTHER TRANSACTION(y/n): ')
                                    if restart  in ('n', 'N', 'No', 'no', 'NO'):
                                        print('\nTHANKS FOR BANKING WITH US**** GT BANK love you')
                                        exit()

                        elif cashInput == '2':
                            while True:
                                receiverName = str(input('RECEIVER NAME:  '))
                                accountNum = int(input('RECEIVER ACCOUNT NUMBER:  '))
                                receiverBank = str(input('RECEIVER BANK NAME:   '))
                                amount = int(input('ENTER AMOUNT TO TRANSFER:  '))
                                print("YOU WANT TO %i to %s WHOSE ACCOUNT NUMBER IS %i ..... %s"
                                      % (amount, receiverName, accountNum, receiverBank))
                                print('PROCESSING.......')
                                if balances[capitalize] < amount:
                                    print('YOUR BALANCE IS NOT UP TO YOUR TRANSFER, pls make a deposit')
                                else:
                                    balances[capitalize] = balances[capitalize] - amount
                                    print('TRANSFER SUCCESSFUL')
                                    print('TRANSFER DETAILS...\n DATE: %s\n RECEIVER NAME: %s\n AMOUNT TRANSFERRED: %i\n'
                                          ' RECEIVER ACCOUNT NUMBER: %i\n RECEIVER BANK: %s\n'
                                          ' REMAINING BALANCE: # %i' % (
                                          date, receiverName, amount, accountNum, receiverBank, balances[capitalize]))
                                    tranfer = input('DO YOU WANT TO PERFORM ANOTHER TRANSFER TRANSACTION(y/n): ')
                                    if tranfer in ('n', 'N', 'No', 'no', 'NO'):
                                        break

                        elif cashInput == '3':
                            depositAmount = int(input('Enter amount to deposit:  #'))
                            balances[capitalize] = balances[capitalize] + depositAmount
                            print('YOUR BALANCE HAVE BEEN UPDATED..')
                            print('\nYOUR BALANCE AS AT %s  IS #%i' % (date, balances[capitalize]))
                            restart = input('DO YOU WANT TO PERFORM ANOTHER TRANSACTION(y/n): ')
                            if restart in ('n', 'N', 'No', 'no', 'NO'):
                                print('THANKS FOR BANKING WITH US ********* GT BANK love you')
                                exit()

                    elif gtInput == '2':
                        print('\nYOUR CURRENT BALANCE IS: #', balances[capitalize])

                    elif gtInput == '3':
                        complain = input('\nPLEASE LAY DOWN YOUR COMPLAIN: ...')
                        print('WE WILL GET BACK TO YOU VERY SOON\n\n'
                              ' OR CALL:\n08004500455 \n09000007666')
                        exit()

                    elif gtInput == '4':
                        restart = input('ARE YOU SURE YOU WANT TO END TRANSACTION(yes/no):  ')
                        if restart in ('y','yes','Yes','Y'):
                            exit()
                        else:
                            restart = 'Y'

            else:
                print('\nEITHER YOUR FIRST NAME OR YOUR PIN IS INCORRECT')
        else:
            print('\nNO MORE TRIAL FOR YOU......\n VISIT THE ACCESS BANK TO RETRIEVE YOU DETAILS')
            exit()
    def accessBank():
        counting = 4
        print('''
     _                           ____              _    
    / \   ___ ___ ___  ___ ___  | __ )  __ _ _ __ | | __
   / _ \ / __/ __/ _ \/ __/ __| |  _ \ / _` | '_ \| |/ /
  / ___ \ (_| (_|  __/\__ \__ \ | |_) | (_| | | | |   < 
 /_/   \_\___\___\___||___/___/ |____/ \__,_|_| |_|_|\_\
                                                        
''')
        while counting > 0:
            print('\nTrial remaining: ', count)
            print('\nYou Can Type in (b or back or B or BACK ) in the FIRST NAME if you are in the wrong bank to choose bank again')
            print('\nWELCOME TO ACCESS BANK')
            print('ENTER YOUR DETAILS BELOW:')
            accessName = str(input('\nFIRST NAME:  '))
            if accessName in ('b','B','back','Back','BACK'):
            	break
            capitalize = accessName.capitalize()
            accessPin = int(input('PIN:  '))
            if accessBankClient[capitalize] == accessPin:
                print('\nWELCOME TO ACCESS B',accessName)
                print('WELCOME', accessName, 'HOW HAVE YOU BEEN')
                restart = 'y'
                while restart not in ('n','N',"no",'No'):
                    accessTransactions = input(' \n1: CASH TRANSACTION\t\t\t\t 2:ACCOUNT BALANCE\t\t\t\t '
                                               '3:CUSTOMER SERVICE\t\t\t 4: exit()\n '
                                               'PLEASE INSERT THE NUMBER OF TRANSACTION TO PERFORM BELOW:')
                    if accessTransactions == '1':
                            date = time.asctime(time.localtime(time.time()))
                            print('1: WITHDRAW CASH\t\t 2: TRANSFER CASH\t\t 3: DEPOSIT ')
                            print('INSERT TRANSACTION TO PERFORM BELOW:  ')
                            cashInput = input()
                            if cashInput == '1':
                                while True:
                                    withdraw = int(input('ENTER AMOUNT TO WITHDRAW:   #'))
                                    if withdraw >  balances[capitalize]:
                                        print('YOU ARE NOT ELIGIBLE FOR OVERDRAFT')
                                    elif withdraw <=  balances[capitalize]:
                                        balances[capitalize] = balances[capitalize] - withdraw
                                        print("YOUR AVAILABLE AS AT %s is #%i" % (date, balances[capitalize]))
                                        restart = input('d(y/n): ')
                                        if restart in ('n', 'N', 'No', 'no', 'NO'):
                                            print('THANKS FOR BANKING WITH US ********* ACCESS BANK LOVE YOU')
                                            print('')
                                            break

                            elif cashInput == '2':
                                while True:
                                    receiverName = str(input('RECEIVER NAME:  '))
                                    accountNum = int(input('RECEIVER ACCOUNT NUMBER:  '))
                                    receiverBank = str(input('RECEIVER BANK NAME:   '))
                                    amount = int(input('ENTER AMOUNT TO TRANSFER:  '))
                                    print("YOU WANT TO %i to %s WHOSE ACCOUNT NUMBER IS %i ..... %s"
                                          % (amount, receiverName, accountNum, receiverBank))
                                    print('PROCESSING.......')
                                    if  balances[capitalize] < amount:
                                        print('YOUR BALANCE IS NOT UP TO YOUR TRANSFER, pls make a deposit')
                                    else:
                                        balances[capitalize] = balances[capitalize] - amount
                                        print('TRANSFER SUCCESSFUL')
                                        print('TRANSFER DETAILS...\n DATE: %s\n RECEIVER NAME: %s\n AMOUNT TRANSFERRED: %i\n'
                                              ' RECEIVER ACCOUNT NUMBER: %i\n RECEIVER BANK: %s\n'
                                              ' REMAINING BALANCE: # %i' % (
                                                  date, receiverName, amount, accountNum, receiverBank, balances[capitalize]))
                                        restart = input('DO YOU WANT TO PERFORM ANOTHER TRANSACTION(y/n): ')
                                        if restart in ('n', 'N', 'No', 'no', 'NO'):
                                            break
                            elif cashInput == '3':

                                depositAmount = int(input('Enter amount to deposit:  #'))
                                balances[capitalize] =  balances[capitalize] + depositAmount
                                print('your balances been updated.....')
                                print('YOUR BALANCE AS AT %s  IS #%i'%(date, balances[capitalize]))
                                restart = input('DO YOU WANT TO PERFORM ANOTHER TRANSACTION(y/n): ')
                                if restart in ('n', 'N', 'No', 'no', 'NO'):
                                    print('THANKS FOR BANKING WITH US ********* ACCESS BANK LOVES YOU')
                                    exit()

                    elif accessTransactions == '2':
                        balance = balances[capitalize]
                        print('YOUR CURRENT BALANCE IS: #', balance)

                    elif accessTransactions == '3':
                        complain = input('LAY DOWN YOUR COMPLAINT:  ')
                        print('WE WILL GET BACK TO YOU VERY SOON\n OR CALL:\n08004500455 \n09000007666')
                        exit()
                    elif accessTransactions == '4':
                        restart = input('ARE YOU SURE YOU WANT TO TERMINATE TRANSACTION(yes/no):  ')
                        if restart in ('y','Yes','yes','Y'):
                            break
                        else:
                            restart = 'y'

            else:
                print('either the name or the pasword is incorrect')
        else:
            print('No trial for you.....\n visit to collect correct your details\n thank you')
            exit()

    def stanbicBank():
        counting = 4
        print('''  ____  _              _     _        ____              _    
 / ___|| |_ __ _ _ __ | |__ (_) ___  | __ )  __ _ _ __ | | __
 \___ \| __/ _` | '_ \| '_ \| |/ __| |  _ \ / _` | '_ \| |/ /
  ___) | || (_| | | | | |_) | | (__  | |_) | (_| | | | |   < 
 |____/ \__\__,_|_| |_|_.__/|_|\___| |____/ \__,_|_| |_|_|\_\
                                                             
                                                              ''')
        while counting > 0:
	        print('\nTRAILS REMAIN:', counting)
	        counting -= 1
	        print('\nYou Can Type in (b or back or B or BACK ) in the FIRST NAME if you are in the wrong bank to choose bank again')
	        print('\nWELCOME TO STANBIC BANK ')
	        print('INSERT YOUR DETAILS BELOW: ')
	        stanbicName = input('\nENTER YOUR FIRST NAME:  ')
	        if stanbicName in ('b','B','back','Back','BACK'):
	        	break	        
	        capitalize = stanbicName.capitalize()
	        stanbicPin = int(input('PIN: '))
	        if capitalize in stanbicClient and  stanbicClient[capitalize] == stanbicPin:
	                print('\nWELCOME BACK TO STANBIC BANK %s'%(stanbicName))
	                restart = 'Y'
	                while restart not in ('n','no','No','NO'):
	                    stanbicInput = input('\n 1: CASH TRANSACTION\t\t 2: ACCOUNT BALANCE\n '
	                          '3: CUSTOMER SERVICE\t\t 4: EXIT\n '
	                          'PLEASE INSERT THE NUMBER OF TRANSACTION TO PERFORM BELOW:')
	                    if stanbicInput == '1':
	                        date = time.asctime(time.localtime(time.time()))
	                        print('1: WITHDRAW CASH\t\t\t 2: TRANSFER CASH \t\t\t 3: DEPOSIT')
	                        print('INSERT NUMBER OF TRANSACTION TO PERFORM BELOW:  ')
	                        cashInput = input()
	                        if cashInput == '1':
	                                withdraw = int(input('ENTER AMOUNT TO WITHDRAW:   #'))
	                                if withdraw > balances[capitalize]:
	                                    print('\nYOU ARE NOT ELIGIBLE FOR OVERDRAFT')
	                                elif withdraw <= balances[capitalize]:
	                                    balances[capitalize] = balances[capitalize] - withdraw
	                                    print("\nYOUR BALANCE AS AT %s IS # #%i" % (date, balances[capitalize]))
	                                    restart  = input('do you want to perform another withdraw transaction(y/n): ')
	                                    if restart  in ('n', 'N', 'No', 'no', 'NO'):
	                                        print('THANKS FOR CHOOSING GT BANKt********* GT BANK love you')
	                                        print('')
	                                        exit()
	
	                        elif cashInput == '2':
	                            while True:
	                                print('WELCOME TO DEPOSIT PAY POINT\n')
	                                receiverName = str(input('RECEIVER NAME:  '))
	                                accountNum = int(input('RECEIVER ACCOUNT NUMBER:  '))
	                                receiverBank = str(input('RECEIVER BANK NAME:   '))
	                                amount = int(input('ENTER AMOUNT TO TRANSFER:  '))
	                                print("YOU WANT TO %i to %s WHOSE ACCOUNT NUMBER IS %i ..... %s"
	                                      % (amount, receiverName, accountNum, receiverBank))
	                                print('PROCESSING.......')
	                                if balances[capitalize] < amount:
	                                    print('YOUR BALANCE IS NOT UP TO YOUR TRANSFER, pls make a deposit')
	                                else:
	                                    balances[capitalize] = balances[capitalize] - amount
	                                    print('\nTRANSFER SUCCESSFUL')
	                                    print('\nTRANSFER DETAILS...\n DATE: %s\n RECEIVER NAME: %s\n AMOUNT TRANSFERRED: %i\n'
	                                          ' RECEIVER ACCOUNT NUMBER: %i\n RECEIVER BANK: %s\n'
	                                          ' REMAINING BALANCE: # %i' % (
	                                          date, receiverName, amount, accountNum, receiverBank, balances[capitalize]))
	                                    tranfer = input('\nDO YOU WANT TO PERFORM ANOTHER TRANSFER TRANSACTION(y/n): ')
	                                    if tranfer in ('n', 'N', 'No', 'no', 'NO'):
	                                        break
	
	                        elif cashInput == '3':
	                            depositAmount = int(input('Enter amount to deposit:  #'))
	                            balances[capitalize] = balances[capitalize] + depositAmount
	                            print('\nYOUR BALANCE HAVE BEEN UPDATED.....')
	                            print('\nYOUR BALANCE AS AT %s  IS #%i' % (date, balances[capitalize]))
	                            restart = input('\nDO YOU WANT TO PERFORM ANOTHER TRANSACTION(y/n): ')
	                            if restart in ('n', 'N', 'No', 'no', 'NO'):
	                                print('\nTHANKS FOR CHOOSING GT BANK ********* GT BANK LOVE YOU')
	                                exit()
	
	                    elif stanbicInput == '2':
	                        print('YOUR CURRENT BALANCE IS: #', balances[capitalize])
	
	                    elif stanbicInput == '3':
	                        complain = input('please how can we help.....\t please lay down your complaint...')
	                        print('we will get back to you very soon\n\n'
	                              ' or call our customer service line:\n08004500455 \n09000007666')
	                        exit()
	
	                    elif stanbicInput == '4':
	                        restart = input('ARE YOU SURE YOU WANT TO END TRANSACTION(yes/no):  ')
	                        if restart in ('y','yes','Yes','Y'):
	                            exit()
	                        else:
	                            restart = 'Y'
	        else:
                 print('either your name or pin is incorrect')
        else:
            print('No more trial for you......\n visit your to reset your password')
            exit()
        		
    def firstBank():
        counting = 4
        print('''
  _____ ___ ____  ____ _____   ____    _    _   _ _  __
 |  ___|_ _|  _ \/ ___|_   _| | __ )  / \  | \ | | |/ /
 | |_   | || |_) \___ \ | |   |  _ \ / _ \ |  \| | ' / 
 |  _|  | ||  _ < ___) || |   | |_) / ___ \| |\  | . \ 
 |_|   |___|_| \_\____/ |_|   |____/_/   \_\_| \_|_|\_\
                                                       
 ''')
        while counting > 0:            
	        print('\nTRAILS REMAIN:', counting)
	        counting -= 1
	        print('\nYou Can Type in (b or back or B or BACK ) in the FIRST NAME if you are in the wrong bank to choose bank again')
	        print('\nWELCOME TO FIRST BANK ')
	        print('INSERT YOUR DETAILS BELOW: ')
	        firstName = input('\nENTER YOUR FIRST NAME:  ')
	        if firstName in ('b','B','back','Back','BACK'):
	        	break
	        capitalize = firstName.capitalize()
	        firstPin = int(input('PIN: '))
	        if capitalize in firstClient and  firstClient[capitalize] == firstPin:
	                print('\nwelcome back to First Bank %s'%(firstName))
	                restart = 'Y'
	                while restart not in ('n','no','No','NO'):
	                    firstInput = input('\n 1: CASH TRANSACTION\t\t 2: ACCOUNT BALANCE\n '
	                          '3: CUSTOMER SERVICE\t\t 4: EXIT\n '
	                          'PLEASE INSERT THE NUMBER OF TRANSACTION TO PERFORM BELOW:')
	                    if firstInput == '1':
	                        date = time.asctime(time.localtime(time.time()))
	                        print('1: WITHDRAW CASH\t\t\t 2: TRANSFER CASH \t\t\t 3: DEPOSIT')
	                        print('INSERT NUMBER OF TRANSACTION TO PERFORM:  ')
	                        cashInput = input()
	                        if cashInput == '1':
	                                withdraw = int(input('ENTER AMOUNT TO WITHDRAW:   #'))
	                                if withdraw > balances[capitalize]:
	                                    print('YOU ARE NOT ELIGIBLE FOR OVERDRAFT')
	                                elif withdraw <= balances[capitalize]:
	                                    balances[capitalize] = balances[capitalize] - withdraw
	                                    print("your available balance as at %s is # %i" % (date, balances[capitalize]))
	                                    restart  = input('do you want to perform another withdraw transaction(y/n): ')
	                                    if restart  in ('n', 'N', 'No', 'no', 'NO'):
	                                        print('thanks for banking with us ********* GT BANK love you')
	                                        print('')
	                                        exit()
	
	                        elif cashInput == '2':
	                            while True:
	                                receiverName = str(input('RECEIVER NAME:  '))
	                                accountNum = int(input('RECEIVER ACCOUNT NUMBER:  '))
	                                receiverBank = str(input('RECEIVER BANK NAME:   '))
	                                amount = int(input('ENTER AMOUNT TO TRANSFER:  '))
	                                print("YOU WANT TO %i to %s WHOSE ACCOUNT NUMBER IS %i ..... %s"
	                                      % (amount, receiverName, accountNum, receiverBank))
	                                print('PROCESSING.......')
	                                if balances[capitalize] < amount:
	                                    print('YOUR BALANCE IS NOT UP TO YOUR TRANSFER, pls make a deposit')
	                                else:
	                                    balances[capitalize] = balances[capitalize] - amount
	                                    print('TRANSFER SUCCESSFUL')
	                                    print('TRANSFER DETAILS...\n DATE: %s\n RECEIVER NAME: %s\n AMOUNT TRANSFERRED: %i\n'
	                                          ' RECEIVER ACCOUNT NUMBER: %i\n RECEIVER BANK: %s\n'
	                                          ' REMAINING BALANCE: # %i' % (
	                                          date, receiverName, amount, accountNum, receiverBank, balances[capitalize]))
	                                    tranfer = input('DO YOU WANT TO PERFORM ANOTHER TRANSFER TRANSACTION(y/n): ')
	                                    if tranfer in ('n', 'N', 'No', 'no', 'NO'):
	                                        break
	
	                        elif cashInput == '3':
	                            depositAmount = int(input('Enter amount to deposit:  #'))
	                            balances[capitalize] = balances[capitalize] + depositAmount
	                            print('your balances been updated.....')
	                            print('YOUR BALANCE AS AT %s  IS #%i' % (date, balances[capitalize]))
	                            restart = input('DO YOU WANT TO PERFORM ANOTHER TRANSACTION(y/n): ')
	                            if restart in ('n', 'N', 'No', 'no', 'NO'):
	                                print('thanks for banking with us ********* GT BANK love you')
	                                exit()
	
	                    elif firstInput == '2':
	                        print('YOUR CURRENT BALANCE IS: #', balances[capitalize])
	
	                    elif firstInput == '3':
	                        complain = input('please how can we help.....\t please lay down your complaint...')
	                        print('we will get back to you very soon\n\n'
	                              ' or call our customer service line:\n08004500455 \n09000007666')
	                        exit()
	
	                    elif firstInput == '4':
	                        restart = input('Are you want to end transaction(yes/no):  ')
	                        if restart in ('y','yes','Yes','Y'):
	                            exit()
	                        else:
	                            restart = 'Y'
	
	        else:
            	 print('either your name or pin is incorrect')
        else:
            print('No more trial for you......\n visit your bank to reset your password')
            exit()
        		
    def ecoBank():
        counting = 4
        print('''
  _____ ____ ___    ____    _    _   _ _  __
 | ____/ ___/ _ \  | __ )  / \  | \ | | |/ /
 |  _|| |  | | | | |  _ \ / _ \ |  \| | ' / 
 | |__| |__| |_| | | |_) / ___ \| |\  | . \ 
 |_____\____\___/  |____/_/   \_\_| \_|_|\_\
                                            
''')
        while counting > 0:            
	        print('\nTRAILS REMAIN:', counting)
	        counting -= 1
	        print('\nYou Can Type in (b or back or B or BACK ) in the FIRST NAME if you are in the wrong bank to choose bank again')
	        print('\nWELCOME TO ECO BANK ')
	        print('INSERT YOUR DETAILS BELOW: ')
	        ecoName = input('\nENTER YOUR FIRST NAME:  ')
	        if ecoName in ('b','B','back','Back','BACK'):
	        	break
	        capitalize = ecoName.capitalize()
	        ecoPin = int(input('PIN: '))
	        if capitalize in ecoClient and  ecoClient[capitalize] == ecoPin:
	                print('\nwelcome back to ECO Bank %s'%(ecoName))
	                restart = 'Y'
	                while restart not in ('n','no','No','NO'):
	                    ecoInput = input('\n 1: CASH TRANSACTION\t\t 2: ACCOUNT BALANCE\n '
	                          '3: CUSTOMER SERVICE\t\t 4: EXIT\n '
	                          'PLEASE INSERT THE NUMBER OF TRANSACTION TO PERFORM BELOW:')
	                    if ecoInput == '1':
	                        date = time.asctime(time.localtime(time.time()))
	                        print('\n1: WITHDRAW CASH\t\t\t 2: TRANSFER CASH \t\t\t 3: DEPOSIT')
	                        print('\nINSERT NUMBER OF TRANSACTION TO PERFORM:  ')
	                        cashInput = input()
	                        if cashInput == '1':
	                                withdraw = int(input('\nENTER AMOUNT TO WITHDRAW:   #'))
	                                if withdraw > balances[capitalize]:
	                                    print('\nYOU ARE NOT ELIGIBLE FOR OVERDRAFT')
	                                elif withdraw <= balances[capitalize]:
	                                    balances[capitalize] = balances[capitalize] - withdraw
	                                    print("\nyour available balance as at %s is # %i" % (date, balances[capitalize]))
	                                    restart  = input('\ndo you want to perform another withdraw transaction(y/n): ')
	                                    if restart  in ('n', 'N', 'No', 'no', 'NO'):
	                                        print('\nthanks for banking with us ********* ECO BANK loves you')
	                                        print('')
	                                        exit()
	
	                        elif cashInput == '2':
	                            while True:
	                                receiverName = str(input('RECEIVER NAME:  '))
	                                accountNum = int(input('RECEIVER ACCOUNT NUMBER:  '))
	                                receiverBank = str(input('RECEIVER BANK NAME:   '))
	                                amount = int(input('ENTER AMOUNT TO TRANSFER:  '))
	                                print("YOU WANT TO %i to %s WHOSE ACCOUNT NUMBER IS %i ..... %s"
	                                      % (amount, receiverName, accountNum, receiverBank))
	                                print('PROCESSING.......')
	                                if balances[capitalize] < amount:
	                                    print('\nYOUR BALANCE IS NOT UP TO YOUR TRANSFER, pls make a deposit')
	                                else:
	                                    balances[capitalize] = balances[capitalize] - amount
	                                    print('\nTRANSFER SUCCESSFUL')
	                                    print('\nTRANSFER DETAILS...\n DATE: %s\n RECEIVER NAME: %s\n AMOUNT TRANSFERRED: %i\n'
	                                          ' RECEIVER ACCOUNT NUMBER: %i\n RECEIVER BANK: %s\n'
	                                          ' REMAINING BALANCE: # %i' % (
	                                          date, receiverName, amount, accountNum, receiverBank, balances[capitalize]))
	                                    tranfer = input('DO YOU WANT TO PERFORM ANOTHER TRANSFER TRANSACTION(y/n): ')
	                                    if tranfer in ('n', 'N', 'No', 'no', 'NO'):
	                                        break
	
	                        elif cashInput == '3':
	                            depositAmount = int(input('Enter amount to deposit:  #'))
	                            balances[capitalize] = balances[capitalize] + depositAmount
	                            print('\nyour balances been updated.....')
	                            print('\npYOUR BALANCE AS AT %s  IS #%i' % (date, balances[capitalize]))
	                            restart = input('DO YOU WANT TO PERFORM ANOTHER TRANSACTION(y/n): ')
	                            if restart in ('n', 'N', 'No', 'no', 'NO'):
	                                print('thanks for banking with us ********* ECO BANK love you')
	                                exit()
	
	                    elif ecoInput == '2':
	                        print('YOUR CURRENT BALANCE IS: #', balances[capitalize])
	
	                    elif ecoInput == '3':
	                        complain = input('please how can we help.....\t please lay down your complaint...')
	                        print('we will get back to you very soon\n\n'
	                              ' or call our customer service line:\n08004500455 \n09000007666')
	                        exit()
	
	                    elif ecoInput == '4':
	                        restart = input('Are you want to end transaction(yes/no):  ')
	                        if restart in ('y','yes','Yes','Y'):
	                            exit()
	                        else:
	                            restart = 'Y'
	
	        else:
            	 print('either your name or pin is incorrect')
        else:
            print('No more trial for you......\n visit your bank to reset your password')
            exit()


    def chooseBank():
        print('''
     █████╗ ████████╗███╗   ███╗
    ██╔══██╗╚══██╔══╝████╗ ████║
    ███████║   ██║   ██╔████╔██║
    ██╔══██║   ██║   ██║╚██╔╝██║
    ██║  ██║   ██║   ██║ ╚═╝ ██║
    ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝
                                
''')
        print('\nTrail remaining:', count)
        welInput = input('\n 1: GT BANK\t\t\t 2: ACCESS BANK\n 3: FIRST BANK\t\t\t 4: STABIC BANK\n 5: ECO BANK\n '
                         '\nSELECT BANK FOR TRANSACT1ION: ')
        if welInput == '1':
            atm.gtBank()

        elif welInput == '2':
            atm.accessBank()
            
        elif welInput == '3':
            atm.firstBank()
            
        elif welInput == '4':
        	atm.stanbicBank()
        
        elif welInput == '5':
        	atm.ecoBank()

while count > 0:
        atm.chooseBank()
        count = count - 1
else:
        if count == 0:
            print('\n TO MUCH ERROR ENCOUNTERED..... PLEASE TRY AGAIN LATER ')