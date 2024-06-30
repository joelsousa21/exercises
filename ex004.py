# Create a program that reads something from the keyboard and display on the screen it's primitive type and all the possible informations about it

# - Has space? True / False
# - Is it a number? True / False
# - Is it alphanumeric? True / False
# - Is it uppercase? True / False
# - Is it lowercase? True / False
# - Is it capitalized? True / False
 

n = input("Type something: ")
print("The primitive type of this is ", type(n)) 

print("Has only space? ", n.isspace())
print("Is numeric? ",n.isnumeric())
print("Is alphanumeric? ",n.isalpha())
print("Is uppercase? ",n.isupper())
print("Is lowerCase? ",n.islower())
print("Is capitalized? ",n.istitle())
