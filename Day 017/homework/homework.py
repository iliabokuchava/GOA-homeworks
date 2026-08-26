#slicing - ის დახმარებით ჩვენ შეგვიძლია სიიდან გამოვიტანოთ 1_ზე მეტი ელემენტი და მერე გამოვიყენოთ, და index - ის დახმარებით შეგვიძლია გამოვიტანოთ მარტო 1 ელემენტი

text = "Python"
print(text [0:3])
print(text [3:6])
print(text [1:4])

numbers = [10, 20, 30, 40, 50, 60]
print(numbers [0:3])
print(numbers [3:6])
print(numbers [1:5])

text = "PythonProgramming"
# print(text[2:10]) - thonProgr
# print(text[:6]) - Python
# print(text[6:]) - Programing
# print(text[::-1]) - gnimmargorPnohtyP
# print(text[::3]) - PhPgmn
# print(text[-5:]) - mming

fruits = ["apple", "banana", "orange", "kiwi", "mango"]
print(fruits [1:4])

#[:end] - გადათვლა იწყება თავიდან და მთავრდება end-ზე
#[start:] - start-იდან იწყება გადათვლა და მიდის ბოლომდე
#[:] - იწყება თავიდან და მიდის ბოლომდე