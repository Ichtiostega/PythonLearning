import myHeaders
myHeaders.printl("String Methods", 7)

course = 'Python for beginners'

print(len(course))          #String length (list length)
print(course.upper())       #Returns string in uppercase
print(course.lower())
print(course.title())       #Returns string with first letter of each word in uppercase
print(course.find('gin'))   #Returns indeks of the first occurence of arg
                            #Returns -1 if not found
print(course.replace('beginners', 'absolute beginners'))
                            #replaces arg1 in string with arg2
print('Python' in course)   #Expretion returns <Bool> True if first string is in the second one
