users = [
    {'name': 'kim', 'age': 12, 'balance': 567898},
    {'name': 'lee', 'age': 22, 'balance': 100},
    {'name': 'yu', 'age': 22, 'balance': 23456},
    {'name': 'park', 'age': 8, 'balance': 1234},
]


def get_age(user):
    return user['age']


def get_balance(user):
    return user['balance']


users.sort(key=get_age)
users.sort(key=lambda user: user['balance'])


def a():
    def b():
        return 'b in a'

    return b

b = a()
print(b())
print(a()())