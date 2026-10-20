#custom ფუნქციები ან def ფუნქცია გამოიყენება პითონში ფუნქციების შესაქმნელად და ლოგიკების ასაწყობად
#ფუნქციის შექმნისას უნდა გავითვალისწინოთ 5 წესი:
#1. def ფუნქციის გაწერა   2. ფუნქციისთვის სახელის დაწერა  3. () გადაცემა  4. : მიწერა  5. თავისით ფუნქციის დაწერა
#parameter - ეს არის მნიშვნელობა რომელსაც ელოდება ფუნქცია, და ვქმნით ფუნქციის შექმნისას
#argument - ეს არის ფუნქციაში გამზადებული პარამეტრის მნიშვნელობა

def counter(num1, num2):
    return num1 + num2
print(counter(12, 34))

def chek_even(num1):
    if num1 % 2 == 0:
        return "რიცხვი ლუწია"
    else:
        return "რიცხვი კენტია"
print(chek_even(34))

def counter(num1):
    return num1 ** 2
print(counter(9))

def upper(txt1):
    return txt1.upper()
print(upper("ilia"))

def name_lastname(name, lastname):
    return f"{name} {lastname}"
print(name_lastname("ilia", "bokuchava"))

