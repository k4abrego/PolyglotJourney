#----------------------------------------------------------
# Lab #1: Image Processing
#
# Date: 31-Aug-2026
# Authors:
#           A01753979 Ana Karen Abrego Flores
#           A01803514 Gabriel de Jesús Manzo Cuevas
#----------------------------------------------------------

from PIL import Image
from typing import cast
from rgb_types import RGBTuple, RGBMatrix


def warhol(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        size: tuple[int, int] = in_img.size
        in_grid: RGBMatrix = cast(RGBMatrix, in_img.load())
    width: int
    height: int
    width, height = size
    out_width: int = width * 2
    out_height: int = height * 2

    out_img: Image.Image = Image.new('RGB',(out_width, out_height))
    out_grid: RGBMatrix = cast(RGBMatrix,out_img.load())

    for y in range(out_height):
        for x in range(out_width):
            source_x: int = x % width
            source_y: int = y % height
            red, green, blue = in_grid[source_x, source_y]
            average: int = (red + green + blue) // 3
            palette: tuple[RGBTuple, RGBTuple, RGBTuple]

            if x < width and y < height:
                palette = ((120, 41, 15),(255, 125, 0),(255, 236, 209))
            elif x >= width and y < height:
                palette = ((88, 57, 39), (160, 129, 93),(244, 237, 228))
            elif x < width and y >= height:
                palette = ((28, 63, 99),(0, 160, 176),(237, 247, 232))
            else:
                palette = ((150, 0, 135),(172, 99, 255),(255, 237, 255))

            if average < 50:
                out_grid[x, y] = palette[0]
            elif average < 130:
                out_grid[x, y] = palette[1]
            else:
                out_grid[x, y] = palette[2]

    out_img.save(output_path)


if __name__ == '__main__':
    warhol('images/chihuahuA.jpg','images/warhol_effect_output.png')
    print('Done!')