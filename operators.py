#ADDITIONAL OPERATORS
a = 60
b = 45.5
c = a + b
#print('the sum of a and b is ',  c, type(c))

#SUBTRACTION OPERATOR
d = b - a
#print('the subtraction of a from b is', d, type(d))

#DIVISION OPERATOR
e = 20
f = 4
division_result = e/f
#print('e divided by f is', division_result, type(division_result))

#MODULUS OPERATOR (REMAINDER)
x = 25
y = 4
modulus_result = x % y
#print('the remainder from x modulo y is :', modulus_result , type(modulus_result))

#LOGICAL OPERATORS

#AND OPERATOR (Logical conjuction)
x = True
y = True

z = x and y
print(z)

eligible_to_vote = True
first_user = True
second_user = False

print('can the first user vote?' , eligible_to_vote and first_user , type(eligible_to_vote and first_user))
print('can the second user vote?' , eligible_to_vote and second_user ,  type(eligible_to_vote and first_user))

#OR OPERATOR
print('can the first user vote?' , eligible_to_vote or first_user , type(eligible_to_vote or first_user))
print('can the second user vote?' , eligible_to_vote or second_user ,  type(eligible_to_vote or first_user))


#NOT OPERATOR
print('can the first user vote?' , not first_user, type(not first_user))
print('can the second user vote?' , not second_user, type(not second_user))