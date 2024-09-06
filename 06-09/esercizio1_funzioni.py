import random

def check_number(num1, num2):
    if num1 == num2:
        return True
    else:
        if num1 > num2:
            print('Inserire numero più alto')
        else:
            print('inserire numero più basso')
        return False

random_number = random.randint(1, 100)
stop = False
while stop != True :
    inserted_number = input('Indovina il numero o premi q per uscire: ')
    if inserted_number == 'q':
        break
    else:
        stop = check_number(random_number, int(inserted_number))