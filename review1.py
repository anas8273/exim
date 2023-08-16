from math import *
print("String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + " IT ")')
print("New lines can be created with a backslash and n.")

# creat lists ....
number=[1,2,3,"four",'five',True]
city=["aden","sana'a","taiz"]

# length
print(len(city))
print(city)

# concatenating (+)
print(number+city)
# هنا يتم مزج القوائم مع بعضها البعض بأشارة (+)

# هنا يتم طبع كل قائمة لحالها
print(number,city)

#indexing
print(number[0:4])
print(city[0])

# nasted list
name_friend=["ali",'ahmed','salh','saheer']
name_brothers=['amjed',"salman","taha"]
print(name_friend)

# Make the list double
print(number* 2)

# Append تستخدم في اضافة كلمة في القوائم فقط
# ايضا لا تقبل الا عنصر واحد فقط في حالة ()
list1=[1,"snad",9,0,7,8,6,'five']
list1.append(87) 
print(list1)
# عند ضافةا اكثر من عنصر نكتب []
list2=["abo ahmed",True]
list2.append([7,8,9])
print(list2)

# Pop off the 0 indexed item
# يستخدم في طباعة العنصر الاخير من القائمة
# وبعد ذلك عندما نريد طباعة القائمة يتم حذف العنصر الاخير
print(list1.pop())
print(list1)
print(list1.pop(2))

# Extend
# تستخدم في دمج قائمتين مع مكوناتهما
list3=["ali",7,"abdo"]
list4=["programming","database manager","web developer","database manager"]
list3.extend(list4)
print(list3)

# Insert
# تستخدم في استبدال عنصر بعنصر آخر
language=["css","c","java","html","paython","php","waf"]
language.insert(3,"c#") 
print(language)

jop=["programming","database manager","web developer","database manager"]
jop.insert(2,"analyst")
print(jop)

'''
You can also have multiple else statements on the same line:
Example
One line if else statement, with 3 conditions:
nasted IF
'''
y = 340
x= 330
print("A") if y < x else print("C") if y == x else print("y is greater then x") if y>x else print("x is lees then y")

# Multiple If Statements in Succession

requestedExtras = ['Coke', 'Ketchup', 'French fries']

if 'Coke' in requestedExtras:
    print('Include an extra large serving of Coca Cola')
elif 'Ketchup' in requestedExtras:
    print('Add some extra ketchup')
elif 'French fries' in requestedExtras:
    print('A bit more French fries, please!')

requestedExtras = ['Coke', 'Ketchup', 'French fries']

if 'Coke' in requestedExtras:
    print('Include an extra large serving of Coca Cola')
if 'Ketchup' in requestedExtras:
    print('Add some extra ketchup')
if 'French fries' in requestedExtras:
    print('A bit more French fries, please!')

# BOOLEN
a=10;b=20

