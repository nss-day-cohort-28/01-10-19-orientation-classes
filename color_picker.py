class ColorPicker:

  # This one gets crazy, but I'll try to explain.
  # The thinking here was that our app may one day want to create colors for all kinds of things, not just Vehicles. And even if it was just for vehicles, some vehicles have carpet colors ( like a car ), some do not ( like a motorcycle ). So, we want to be able to not just create a list of colors, but a collection of colors that are unique to the properties of a thing that need to be colored.

  # The **kwargs argument allows us to pass in any number of named arguments, like carpet="blue" and "seats="gray", and have them turned into a dictionary -- { "carpet": "blue", "seats": "gray"}.
  # Then we format those to be attributes on an instance of ColorPicker -- self.carpet = "blue".
  # 'setattr' does that for us by taking two arguments: the key and the value. Our keys will be each of the keys from the **kwargs dictionary.

  # In get_colors() we're using a dictionary comprehension. It will create key value pairs ( k: v) by looping through a dictionary we make from the instance's attributes ( self.__dict__.items() ), but only add the attribute to the dictionary if its key contains the string 'color'

  # By adding "_color" to the end of each key before we turn them into an attribute, that allows us to filter for all attributes that represent a color when we get_colors(). Later, if this class ends up having other attributes added to it, self.name or self.whatever, get_colors() will only give us the attributes that are colors.

  def __init__(self, primary_color, **kwargs):
    self.primary_color = primary_color
    for key, value in kwargs.items():
      setattr(self, key + "_color", value)

  def get_colors(self):
    return {k: v for k, v in self.__dict__.items() if 'color' in k}
