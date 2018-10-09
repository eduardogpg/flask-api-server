__USERS = [
    {
        'username': 'eduardo',
        'password' : 'password123'
    }
]

def get_user(username=''):
    users = [user for user in __USERS if user['username'] == username]
    if len(users) > 0:
        return users[-1].get('password')
    return None
