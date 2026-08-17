from PIL import Image
from typing import cast
from rgb_types import RGBTuple, RGBStream

def negate(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data()) #
        size: tuple[int, int] = in_img.size #the values we want to use for the output image
    out_stream: list[RGBTuple] = [] #list to hold the pixel data for the output image
    red: int
    green: int
    blue: int
    for (red, green, blue) in in_stream:
        out_stream.append((255 - red, 255- green, 255 - blue))
    out_img: Image.Image = Image.new('RGB', size) # create a blank image with the same size as the input image
    out_img.putdate(out_stream) #copy pixel data from the output stream to the output image

    out_img.save(output_path) #write the output image to the specified path
    
if __name__ == '__main__':
    negate('images/puppy.png', 'images/puppy_negative.png')
    print("Done!")