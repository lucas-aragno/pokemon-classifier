import urllib
import pykemon

client = pykemon.V1Client()
for x in range(1, 252):
  pokemon = client.get_pokemon(uid=x)[0]
  name = pokemon.name.lower()
  print name
  f = open('./sprites/{0}.png'.format(name), 'wb')
  print 'Requesting for {0} '.format(name)
  f.write(urllib.urlopen('https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/model/{0}.png?raw=true'.format(x)).read())
  f.close()
