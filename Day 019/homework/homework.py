#indexing - ი გამოიყენება იმისთვის რომ სიიდან გამოვიტანოთ ერთი ელემენტი და გამოვიყენოთ, ყოველ სიის ელემენტს აქვს თავისი ინდექსი, ინდექსის ათვლა იწყება 0 - დან, და უარყოფოთი ინდექსის შემთხვევაში -1 - დან

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers [:4])
print(numbers [5:])
print(numbers [2:6])
print(numbers [::-1])

word = "PYTHONPROGRAMMING"
print(word [:6])
print(word [6:])
print(word [:5])
print(word [12:])
print(word [::-1])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters [-1:])
print(letters [-4:])
print(letters [-8:-2])
print(letters [-5:-2])
print(letters [::-1])



