# > Use python for this assignment
# >
# > Check out [w3schools python 
# > tutorials for help](https://www.w3schools.com/python/python_lists.asp) 

# > Follow the instructions in the order found below
# >
# >
# > Create a file called `array.py `
# > 
# > Unless explicitly stated each of these problems should only take one line of code (Do not comment on the same line of code, use comments before or after the line of code)
# > 
# `problem 1. print your first and last name`
print("Justin Arteaga")
# `problem 2. In the array.py create an array named 'cars' with the following elements in this order  ---- Ford,Chrysler,Dodge,Ram,Jeep,Chevy,GMC` (use single quotes for each element)EX: 'Ford' not "Ford" spelling matters
cars = ['Ford', 'Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
# `problem 3. print the array to the console`
cars = ['Ford', 'Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
print(cars)
# `problem 4. print the length of the array to the console `
cars = ['Ford', 'Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
cars_length = len(cars)
print(cars_length)
# `problem 5. Append Buick to the Array`
cars = ['Ford', 'Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
cars.append('Buick')
# `problem 6. print the array to the console`
cars = ['Ford', 'Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
cars.append('Buick')
print(cars)
# `problem 7. Print the 4th element in the array (Not index 4, element 4)`
cars = ['Ford', 'Chrysler','Dodge','Ram','Jeep','Chevy','GMC']
print(cars[3])
# `problem 8. Insert 'Toyota' into element 3 in the array`
cars = ['Ford', 'Chrysler','Dodge','Ram','Jeep','Chevy','GMC'] 
cars.insert(3,'buick')
# `problem 9. print the array to the console`
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
cars.insert(3, 'Toyota')
print(cars)
# `problem 10. Remove element 5 of the array (hint look at options for pop())`
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
cars.pop(4)
# `problem 11. print the array to the console`
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
cars.pop(4)
print(cars)
# `problem 12. Sort the array in ascending order`
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
cars.sort()
# `problem 13. print the array to the console`
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
cars.sort()
print(cars)
# `problem 14. Sort the array in descending order`
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
cars.sort(reverse=True)
# `problem 15. print the array to the console`
cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC']
cars.sort(reverse=True)
print(cars)
# `problem 16. create a variable called my_array_length with a value of the cars array length (spelling, capitilization, and spaces matter)`
my_array_length = len(cars)
# `problem 17. create a variable called array_string with a value of 'The length of my array is ' (spelling, capitilization, and spaces matter)`
array_string = 'the length of my array is'
# `problem 18. print array_string concatenated with my_array_length to the console.`
my_array_length = len(cars)
array_string = 'The length of my array is '
print(array_string + str(my_array_length))
