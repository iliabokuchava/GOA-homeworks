num = int(input('შემოიყვანე რიცხვი 1-დან 7-დე: '))

if num == 1:
    print('ორშაბათი')
elif num == 2:
    print('სამშაბათი')
elif num == 3:
    print('ოთხშაბათი')
elif num == 4:
    print('ხუთშაბათი')
elif num == 5:
    print('პარასკევი' )
elif num == 6:
    print('შაბათი')
elif num == 7:
    print('კვირა')
else:
    print('არ ვიცი ეგ რა დღეა')

num1 =  int(input('შემოიყვანე რიცხვი: '))

if num1 > 50:
    print(num1 * 5)
else:
    print(num1 ** 2)

password = "goa123"
guess = input('შემოიყვანე კოდი: ')

if password == guess:
    print("Password is correct!")
else:
    print("Incorrect password!")