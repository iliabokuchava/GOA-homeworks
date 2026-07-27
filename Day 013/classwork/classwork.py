num1 = int(input('შემოიყვანე რიცხვი: '))
if num1 > 0:
    print('რიცხვი დადებითა')
else:
    print('რიცხვია უარყოფითია ან ნულია')

age = int(input('შემოიყვანე შენი ასაკი: '))
if age >= 18:
    print('სრულწლოვანია')
else:
    print('არასრულწლოვანია')

point = int(input('შემოიყვაბე შენი ქულა: '))
if point >= 50:
    print('ჩააბარა')
else:
    print('ვერ ჩააბარა')

password = "python123"
guess = input('შემოიყვანე პაროლი: ')
if guess == password:
    print("წვდომა ნებადართულია")
else:
    print("არასწორი პაროლი")