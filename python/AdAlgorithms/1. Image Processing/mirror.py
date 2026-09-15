from PIL import Image
from typing import cast
from rgb_types import RGBMatrix

def mirror(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        size: tuple[int, int] = in_img.size #the values we want to use for the output image
        in_grid: RGBMatrix = cast(RGBMatrix, in_img.load())
    width:int
    height: int
    width, height = size
    out_img: Image.Image = Image.new('RGB', size) # create a blank image with the same size as the input image
    out_grid: RGBMatrix = cast(RGBMatrix, out_img.load())
    for y in range(height):
        for x in range(width):
            out_grid[x, y] = in_grid[(width - 1) - x, (height - 1) - y]
    out_img.save(output_path) #write the output image to the specified path

if __name__ == '__main__':
    mirror('images/tree.png', 'images/tree_mirror.png')
    print("Done!")