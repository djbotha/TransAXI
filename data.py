import pprint

pp = pprint.PrettyPrinter()
users = []
wallets = []
transactions = []
payment_details = []

def Users():
    users = [
        {
            'name': 'Daniel Botha',
            'email': 'botha.daniel1@gmail.com',
            'password': '123456',
            'wallet_id': 1, 
            'role': 'commuter',
        },
        {
            'name': 'Christiaan van der Merwe',
            'email': 'chris@gmail.com',
            'password': '123asd456',
            'wallet_id': 2, 
            'role': 'commuter',
        },
        {
            'name': 'Darrian Marais',
            'email': 'darrian@gmail.com',
            'password': '1234asfas56',
            'wallet_id': 3, 
            'role': 'commuter',
        },
        {
            'name': 'OJ',
            'email': 'oj@gmail.com',
            'password': '1asdfa23456',
            'wallet_id': 4, 
            'role': 'driver',
        }
    ]
    return users

def Wallets():
    wallets = [
        {
            'user_id': 1,
            'amount': 13245.11    
        },
        {
            'user_id': 2,
            'amount': 1245.11    
        },
        {
            'user_id': 3,
            'amount': 45.11    
        },
        {
            'user_id': 4,
            'amount': 425.11    
        }        
    ]
    return wallets

def Transactions():
    transactions = [
        {
            'user_from': 1,
            'user_to': 4,
            'amount': 5.12
        },
        {
            'user_from': 2,
            'user_to': 4,
            'amount': 50.12
        },
        {
            'user_from': 3,
            'user_to': 4,
            'amount': 10.00
        }
    ]
    return transactions