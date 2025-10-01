def hello(name, first, last):
 name = input('Enter your name:').strip().title()
 first, last = name.split(" ")
 print(f'My name is {first}')
 