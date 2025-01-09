'''Strings are immutable.
1. Once we deckare the string we cannot modify it, if we try to modify the string
we try to modify the Strings it will create new String.

2. If we String does not have any reference variable then it wil be removed.

3. Python Internally uses String Interning

4. String Interening is the Process of Checking string Intern Pool
before creating any new object.

Whenever we want create new objects, Python first will check string
intern pool, wheather that object already exist or not.

When Object already exist in the string intern Records then address of existing
object will be reused.'''


# s1 = 'Kodnest'
# s1=s1.upper()
# print(s1)

# s1 = 'k'
# print(s1, id(s1))

s1 = 'Hello'
s2 = 'World!'
print(s1, id(s2))
print(id(s1), s2)

print(s1[0])
print(s1[-1])

print('ID of H:',id(s1[0]))
print('ID of O:',id(s1[-1]))

print('ID of O:',id(s2[1]))
print('ID of w:',id(s2[3]))
