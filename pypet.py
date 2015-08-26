print 'Welcome to Pypet!'

name = 'Fluffy'
age = 5
weight = 9.5 
hungry = False 
photo = '(=^o.o^=)__'


print 'Hello' + name
print photo 
cat {
	'name': 'Fluffy',
	'hungry': True,
	'weight': 9.5,
	'age': 5,
	'photo': '(=^o.o^=)__',
}
print 'Hello' + cat['name']
print cat ['photo']

print cat

def feed(pet):
	pet['hungry'] = False


feed(cat)
def feed(pet):
if pet['hugnry'] == True:
	pet['hungry'] = False
	pet['weight'] = pet['weight'] + 1
else:
	print 'The Pypet is not hungry'
print cat
feed(cat)
print cat
