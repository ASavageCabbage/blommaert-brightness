from dinos import bronto
from src.dino import read_image, write_image


image = read_image("images/LuxoDoubleChecker.exr")
tonemapped = bronto(image)
write_image("_output/test2.png", tonemapped)
