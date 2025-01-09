'''Strings are immutable.
1. Once we deckare the string we cannot modify it, if we try to modify the string
we try to modify the Strings it will create new String.

2. If we String does not have any reference variable then it wil be removed.'''


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