# Variables

my_string_variable= "my string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable =str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# concatenacion de vatiables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)
print("esta es el valor de: ", my_bool_variable)

# algunas funciones del sistema 
print(len(my_string_variable))

# variables en un sola linea. cuidado con abusar de esta sintaxis 
name, surname, alias, age = "jefferson", "lascano", "fusilero", 29
print("me llamo:", name, surname, ". mi edad es:", age, ". y mi alias es:", alias)

#Inputs

"""name = input("cual es tu nombre? ") #puede mutar la variable 
age = input("cuantos años tienes")

print(name)
print(age) """


#Cambiamos su tipo
name= 35
age = "Jefferson"
print(name)
print(age)

# forzamos el tipo

direccion: str = "Mi direccion"
direccion = 32
print (type(direccion))