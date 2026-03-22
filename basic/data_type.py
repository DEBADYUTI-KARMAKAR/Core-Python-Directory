#Numeric
a = 10
b = 12.4
c = 12j
print(type(a)) # int
print(type(b)) # float
print(type(c)) # complex
#boolean
d=True
e=False
print(type(d)) # boolean
print(type(e)) # boolean

# Dictionary
student = {
    "name": "Deb",
    "age": 25
}
print(student)
print(student["name"])
print(student["age"])

#Set
set_data = {1,2,3,4,4.5,True,5,5,False,6}
print(set_data) # {False, 1, 2, 3, 4, 4.5, 5, 6} 
'''
{False, 1, 2, 3, 4, 4.5, 5, 6} 
true not showing because 1 is there 
True == 1
False == 0
and set contains unique value
'''
print(type(set_data))

# Sequence Type
# String
str_type = "Deb" 
str_type1 = "Deb's" 
str_type2 = 'Debs'
print(str_type)
print(str_type1)
print(str_type2)
print(type(str_type1))

# List
data1 = [1,2,3,4,5,4.5,True,True,4.5]
print(data1)
print(data1[0])

#Touple
t_data = (1,2,3,6,6,True,3.5,5+8j)
t_data =(1,3)
print(t_data) 
