# Pokemon Classifier

This repo uses a [sckit](http://scikit-learn.org) [Classification Tree](http://scikit-learn.org/stable/modules/tree.html#classification) to predict the type of a pokemon based on a picture


## How it works?

### Getting the images

To get the images I have a `download_sprites.py` script that goes to the [PokeAPI](http://pokeapi.co) repo and gets the sprites (images) for every pokemon on the first and second generation.

### The training data

For the training data we are going to assign all the pokemon types ( there are 19 of them ), fire, water, grass, etc to a list of integers with their id on the PokeAPI those id's will act as our labels for the training samples

Then we are going to use [Color Thief](https://github.com/fengsp/color-thief-py) and loop through each pokemon (from gen1 and gen2) get their type and then from its image we get the dominant color of that pokemon.

<p align="center">
  <img src="https://github.com/lucas-aragno/pokemon-classifier/blob/master/docs/color.gif">
</p>


In there we can see that we extract the RGB dominant color of each pokemon like so:

<p align="center">
  <img src="https://github.com/lucas-aragno/pokemon-classifier/blob/master/docs/colors.png">
</p>


and we are end up with a list Y with the type of each pokemon where each of those types corresponds with an item on the list X
which is the RGB representation of the dominant color for that pokemon ( in this case another list)


Finally we call `DecisionTreeClassifier` to create our classifier and fit our training data

```python
  clsf = tree.DecisionTreeClassifier()
  clsf.fit(POKEMON_COLORS, POKEMON_TYPES)
```


After that's done we can add a picture of a pokemon on the `predict` folder and use the file name on the function `predict_pokemon`.

For example we can add the picture of [torchic](https://github.com/PokeAPI/sprites/blob/master/sprites/pokemon/model/255.png?raw=true) a pokemon from the gen 3 ( that means that it wasn't part of our training data). That pokemon is a fire type and it's dominant color is orange.

If we use the classifier with that picture this is our ouput:

```python
Your prediction:
fire
```

which is correct! You can try to run it with ohter pokemons and see if it gets right or not or add more pokemons to the training data set!
