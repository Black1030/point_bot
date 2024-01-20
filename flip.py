from validators import valid_user_register
from functions import load_to_base

username: str = input('username - ')
password: str = input('password - ')
result: Exception = valid_user_register(username, password)

while result:
    print(f'{result}')
    if str(result).split()[1] == 'PASSWORD':
        password = input('password - ')
    elif str(result).split()[1] == 'USERNAME':
        username = input('username - ')
    result = valid_user_register(username, password)

print('SUCCESS REGISTER')
load_to_base(username, password)
