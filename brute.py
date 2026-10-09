secret = 'qwerty'

f = open("passwords.txt")
passwords = []
for line in f.readlines():
    passwords.append(line.strip())

for p in passwords:
    print('Пробую пароль: ' + p)
    if p == secret:
        print('ПАРОЛЬ НАЙДЕН: ' + p)
        break