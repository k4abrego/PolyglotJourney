from PIL import Image
from typing import cast
from rgb_types import RGBMatrix

SCALE = 10 #constant value

def shrink(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        size: tuple[int, int] = in_img.size 
        in_grid: RGBMatrix = cast(RGBMatrix, in_img.load())
    width:int
    height: int
    width, height = size
    new_width = width // SCALE
    new_height = height // SCALE
    out_img: Image.Image = Image.new('RGB', (new_width, new_height))
    out_grid: RGBMatrix = cast(RGBMatrix, out_img.load())
    for y in range(new_height):
        for x in range(new_width):
            out_grid[x, y] = in_grid[x * SCALE, y * SCALE]
    out_img.save(output_path) 

if __name__ == '__main__':
    #shrink('images/tree.png', 'images/tree_shrinking.png')
    shrink('images/puppy.png', 'images/puppy_tiny.png')
    print("Done!")