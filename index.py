from car import Car
from color_picker import ColorPicker

# MAke an instance of a Car, passing in the price, no. of airbags and seat material
bumblebee = Car(34, 3, "steel wool")

# Becuase a car instance inherits from Vehicle, we can call the method from Vehicle that turns our car to a rocket-powered bot
bumblebee.transformerize("dude", 5)
print("bumbee name?", bumblebee.v_type)

# Now we make an instance of the ColorPicker Class to create a dictionary of custom color key-value pairs.
bumblebee_colors = ColorPicker("yellow", interior="black", pinstripe="turquoise")

# Then we can compose the colors collection into our Car instance
bumblebee.add_colorscheme(bumblebee_colors.get_colors())

# And now our car has color!
print(bumblebee.colorscheme)
