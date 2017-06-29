import pykemon
import csv
import pydotplus
from colorthief import ColorThief
from sklearn import tree

client = pykemon.V1Client()

TYPES = []

POKEMON_COLORS = []
POKEMON_TYPES = []

def populate_types_array():
  for x in range(1, 19):
    pkmn_type = pykemon.get(type_id=x)
    print pkmn_type
    TYPES.append(pkmn_type.name.lower())

def pokemon_colors():
    for x in range(1, 252):
        pokemon = client.get_pokemon(uid=x)[0]
        color_thief = ColorThief('./sprites/{0}.png'.format(pokemon.name.lower()))
        palette = color_thief.get_palette(color_count=2)
        POKEMON_TYPES.append(TYPES.index(pokemon.types[0]['name']))
        print "dominant color for {0} is {1}".format(pokemon.name, palette[0])
        POKEMON_COLORS.append(list(palette[0]))

def create_classifier():
    clsf = tree.DecisionTreeClassifier()
    print POKEMON_TYPES
    print POKEMON_COLORS
    return clsf.fit(POKEMON_COLORS, POKEMON_TYPES)

def predict_pokemon(file_name, classifier):
  color_thief = ColorThief('./predict/{0}'.format(file_name))
  palette = color_thief.get_palette(color_count=2)
  return classifier.predict(list(palette[0]))

populate_types_array()

pokemon_colors()

classifier = create_classifier()

print 'Your prediction'
type_index = predict_pokemon('255.png', classifier)[0]
print TYPES[type_index]
