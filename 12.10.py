exit = 0
zash = ''
rozh=''
while exit != 'вийти':
    dija = input('Ведіть дію:зашифрувати чи розшифрувати\n'.lower())
    message = input('Ведіть речення\n'.lower())
    if dija == 'зашифрувати':
        for letter in message:
            value = ord(letter) + 3
            bukva = chr(value)
            zash = zash + bukva
    elif dija == 'розшиврувати':
        for letter in message:
            value = ord(letter) - 3
            bukva = chr(value)
            rozh = rozh + bukva
    print(zash,rozh)
    exit = input("Вийти чи продовжити".lower())
