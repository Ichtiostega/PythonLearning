import myHeaders
myHeaders.printl("Formatted Strngs", 6)

first = 'John'
last = 'smith'

message = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder.'           #'f' before string makes formatted string
                                                #Allows adding variables to the string with {}
print(message)
print(msg)