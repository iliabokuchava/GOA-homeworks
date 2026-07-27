#if else statement - ან პირობითი პირობითი ოპერატორები, აძლევენ კოდს იმის საშვალებას რომ პირობაზე დაყრდნობით მივიდეთ ერთ სწორ პსუხთან

num1 = int(input('შემოივანე პირველი რიცხვი: '))
num2 = int(input('შემოიყვანე მეორე რიცხვი: '))

if num1 > num2:
    print("პირველი მეტია")
else:
    print("მეორე მეტია ან ტოლია")

num3 =  int(input('შემოივანე რიცხვი: '))

if num3 > 100:
    print("100-ზე მეტია")
else:
    print("100-ზე ნაკლები ან ტოლია")

name = 'Nika'
enter_name = input('შემიყვანე შენი სახელი: ')

if name == enter_name:
    print("გამარჯობა, ნიკა!")
else:
    print("უცნობი მომხმარებელი")

temp = int(input('შემოიყვანე ტემპერატურა: '))

if temp < 0:
    print('იყინება')
else:
    print("არ იყინება")

price = int(input('შემოიყვანე პროდუქტის ფასი: '))

if price >= 100:
    print('ეკუთვნის ფასდაკლება')
else:
    print("ფასდაკლება არ გეკუთვნის")

num4 =  int(input('შემოივანე რიცხვი: '))

if num4 == 0:
    print("ნულია")
else:
    print("ნული არ არის")

balance = int(input('შემოიყვანე შენი ანგარიში: '))

if balance >= 50:
    print("საკმარისი ბალანსია")
else:
    print("ბალანსი არასაკმარისია")