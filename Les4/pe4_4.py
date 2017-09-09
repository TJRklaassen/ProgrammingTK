def new_password(oldpassword,newpassword):

    containNumber = False
    for number in range(10):
        if str(number) in newpassword:
            containNumber = True

    if oldpassword != newpassword and len(newpassword) >= 6 and containNumber == True:
        print("Je wachtwoord is veranderd")
        return True
    else:
        print("Je ingevoerde wachtwoord voldeed niet aan de eisen")
        return False

password = 'wachtwoord'
newpassword = input('Typ een nieuw wachtwoord: ')

if new_password(password,newpassword) == True:
    password = newpassword
print("Wachtwoord: "+password)
