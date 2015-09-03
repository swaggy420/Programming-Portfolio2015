print 'Welcome to Pypet!'

name = ' Jerry'
age = 6
weight = 1.5
hungry = False
photo = '<:3 )~~~~'


print 'Hello' + name
print photo
mouse = {
	'name': ' Jerry',
	'age': 6,
	'weight': 1.5,
	'hungry': False,
	'photo': '<:3 )~~~~',
}

name = ' Tom'
age = 5
weight = 9.5 
hungry = False 
photo = '(=^o.o^=)__'

cat = {
	'name': ' Tom',
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
	if pet['hungry'] == True:
		pet['hungry'] = False
		pet['weight'] = pet['weight'] + 1
	else:
		print 'The Pypet is not hungry'

pets = [cat, mouse]

for pet in pets:
	feed(pet)
	print pet

print cat
feed(cat)
print cat
