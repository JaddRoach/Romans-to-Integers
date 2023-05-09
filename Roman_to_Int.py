# Roman to Integer
# Takes roman numeral values and converts the roman numerals to its integer value
roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
roman_numerals = input("Enter a roman numeral: ")
roman_values = []           # Roman numeral list

# Gets integer assigned to roman numeral letter and stores it in a list
for roman_numeral in roman_numerals:
    for key, value in roman.items():
        if roman_numeral.lower() == key.lower():
            roman_values.append(value)

counter = 0                 #       iterates through the while loop
roman_value = 0             #       one value from the roman value list
integer_values = []         #       integer value list

# print(roman_values)         #       Displays the list of integer values in roman_values list
roman_values.reverse()        #       Reverses the list, which technically makes it look from right to left
# print(roman_values)         #       Displays list again

while counter < len(roman_values):
    if roman_values[counter] >= roman_value:
        roman_value = roman_values[counter]
        integer_values.append(roman_value)
    elif roman_values[counter] < roman_value:
        roman_value = roman_values[counter]
        integer_values.append(roman_value*-1)
    counter += 1

# print(integer_values)
print(sum(integer_values))      # Sums the integers in list to get the converted roman numeral in integers








