import myHeaders
myHeaders.printl("Modules", 22)

import converters

print(converters.kg_to_lbs(70))

from converters import kg_to_lbs

print(kg_to_lbs(70))

import utils

number_list = [3, 5, 3, 4, 6, 4, 5]
print(f"Maximum from list:\t{number_list}\nIs {utils.find_max(number_list)}")