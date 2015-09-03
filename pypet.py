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

mouse = {
	'name': 'Jerry',
	'age': 6,
	'weight': 1.5,
	'hungry': False,
	'photo': '<:3 )~~~~~'
}

pets = [cat, mouse]



def feed(pet):
	if pet['hungry'] == True:
		pet['hungry'] = False
		pet['weight'] = pet['weight'] + 1
		print 'omnomom'
	else:
		print 'The Pypet is not hungry'

for pet in pets:
	print '------------------------------'
	print 'Hello ' + pet ['name'] + '!'
	print pet ['photo']
	print 'Weight: ' + str(pet['weight'])
	feed(pet)
	print 'Weight: ' + str(pet['weight'])
	print '------------------------------'

print cat
feed(cat)
print cat
feed(cat)
