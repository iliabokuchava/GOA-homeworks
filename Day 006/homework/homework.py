#1
#str() - ფუნქციით შეგვიძლია int-ი და float-ი გარდავქმნათ str-ად
Num1 = 25.6
Num2 = 7

num1 = str(Num1)
num2 = str(Num2)

#int() - ფუნქციით შეგვიძლია გარდავქმნათ მარტო str-ი int-ად
Num3 = '52'

num3 = int(Num3)

#float() - ფუნქციით შეგვიძლია int და str გარდავქმნათ sloat-ად
Num4 = 57
Num5 = '62'

num4 = float(Num4)
num5 = float(Num5)

#2
#Data - ნიშნავს მონაცემთა ტიპს, ჩვენ ვიცით 3 სახის მონაცემთა ტიპი: integer-ი, string-ი და float-ი

#3
print("10" + "20")
#ამ კოდში პასუხი გამოვა 1020 იმიტომ რომ, სტრინგების მათემათიკურად ეთმანეთთან მიმატება არ შეიძლება, ამიტომ აქ მოხვდა კონკატენაცია.


number1 = int(input('შეიყვანე პირველი რიცზვი: '))
number2 = int(input('შემოიყვანე მეორე რიცხვი: '))

print(number1 + number2)
print(number1 - number2)
print(number1 / number2)
print(number1 // number2)
print(number1 * number2)
print(number1 ** number2)
print(number1 % number2)
