 
#   Task: Create a mock USSD service that takes user input, and provides appropriate response.
#   Description:
# *User provides a USSD code as input
# *User can then choose among a list of options(with numbers),
#  whether to check balance, send money, purchase airtime, etc.
# *For check balance, the user is prompted to provide his password(hard-coded by you.). 
# If correct, s/he is shown the balance—also hard-coded.
# *For sending money, the user is prompted to choose from a selection of banks,
#  after which he provides an account number, and then an amount to send.
#   And then a password, which if correct, would send the required amount, and deduct from account balance.
# *Follow a similar scheme as sending money, for purchasing airtime—except that in this case,
#  the user is ported for a phone number instead.
class CreateUserAccount:
    def __init__(self):
        self.account_balance = 200000
        self.password = 4034
def bank_service_app():
    while True:    
        print('''
        1) Use bank app
        2) Exit program''')
        reply = int(input('Enter 1 or 2 '))
        if reply == 1:
            while True:
                print('Enter ussd code')
                print('ussd code should be *903#')
                ussd_code = input()
                user = CreateUserAccount()
                if ussd_code == '*903#':
                    while True:    
                        print('''What would you like to do?
                        1) Check balance
                        2) Send money
                        3) Buy airtime
                        4) Quit
                        Enter 1, 2, 3 or 4 to select an option
                        ''')
                        response = int(input())
                        if response == 1:
                            pw = int(input('Enter your password: '))
                            if pw == user.password:
                                print(f'You currently have: {user.account_balance}$' )
                            else:
                                print('Incorrect password. Try again.')
                                continue
                        elif response == 2:
                            while True:
                                print('''Select a bank:
                                1) Ecobank
                                2) First bank
                                3) GTCo.
                                4) Fidelity Bank
                                5) WEMA Bank
                                6) United Bank for Africa
                                7) Union Bank
                                8) Cancel
                                Enter the digits preceding each bank to make a selection''')
                                bank_selection = int(input())
                                if bank_selection not in range(1,9):
                                    print('invalid selection')
                                    continue
                                elif bank_selection in range(1,8):    
                                    while True:
                                        print('Enter receipient\'s ten-digit account number: ')
                                        r_a_n = input()
                                        if len(r_a_n) != 10:
                                            print('Check that the account number entered is 10 digits.')
                                            continue
                                        else:
                                            while True:
                                                amount = int(input('How much would you like to transfer? '))
                                                if amount > user.account_balance:
                                                    print('Insufficient funds')
                                                    continue
                                                else:
                                                    while True:
                                                        print('Enter your password: ')
                                                        pw = int(input())
                                                        if pw != user.password:
                                                            print('Incorrect password! Try again.')
                                                            continue
                                                        elif pw == user.password:
                                                            print(f'You have successfully transferred ${amount}')
                                                            user.account_balance -= amount
                                                            break
                                                    break
                                            break
                                    break
                                elif bank_selection == 8:
                                    break
                                
                        elif response == 3:
                            while True:
                                phone_number = input('Enter the receipient\'s phone number: ')
                                if len(phone_number) != 11:
                                    print('Ensure that the number is in normal format, like so; 080********')
                                    continue
                                else:
                                    while True:
                                        print('Enter password: ')
                                        pw = int(input())
                                        if pw != user.password:
                                            print('Incorrect password, try again.')
                                            continue
                                        elif pw == user.password:
                                            while True:    
                                                print('How much airtime would you like to recharge? ')
                                                airtime_amount = int(input())
                                                if airtime_amount > user.account_balance:
                                                    print('Insufficient funds to  perform transaction. ')
                                                    continue
                                                else:
                                                    print(f'You have successfully recharged {airtime_amount}')
                                                    user.account_balance -= airtime_amount
                                                    break
                                        break
                                    break
                        elif response == 4:
                            break
                    break
                else:
                    print('Invalid code.')
                    continue
        elif reply == 2:
            break
        else:
            print('Invalid selection, enter 1 or 2')
            continue



bank_service_app()