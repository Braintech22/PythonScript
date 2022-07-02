# this program will allow user to convert temperature 
# from any unit to another unit of choice.

print("1 = celcius")
print("2 = kelvin")
print("3 = Fehrenhiet")

celcius = 1
kelvin = 2
Fehrenhiet = 3

temp_format = input("Please enter your Temp Unit:  ")
temp_value = input("what is your temp in celcius:  ")
temp_value = int(temp_value)
kelvin = temp_value + 273.15
fahren = 9/5*temp_value + 32

print("Your {} degree celcius is {} in kelvin and {} in Fahrenheit " . format(temp_value,kelvin,fahren))


    



