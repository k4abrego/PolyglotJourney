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
from rgb_types import RGBMatrix


def tiling(input_path1: str, input_path2: str, input_path3: str, input_path4: str,output_path: str) -> None:
    in_img1: Image.Image
    with Image.open(input_path1) as in_img1:
        in_img1 = in_img1.convert('RGB')
        size: tuple[int, int] = in_img1.size
        in_grid1: RGBMatrix = cast(RGBMatrix, in_img1.load())

    in_img2: Image.Image
    with Image.open(input_path2) as in_img2:
        in_img2 = in_img2.convert('RGB')
        in_grid2: RGBMatrix = cast(RGBMatrix,in_img2.load())

    in_img3: Image.Image
    with Image.open(input_path3) as in_img3:
        in_img3 = in_img3.convert('RGB')
        in_grid3: RGBMatrix = cast(RGBMatrix,in_img3.load())

    in_img4: Image.Image
    with Image.open(input_path4) as in_img4:
        in_img4 = in_img4.convert('RGB')
        in_grid4: RGBMatrix = cast(RGBMatrix,in_img4.load())

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
            if x < width and y < height:
                out_grid[x, y] = in_grid1[source_x, source_y]
            elif x >= width and y < height:
                out_grid[x, y] = in_grid2[source_x, source_y]
            elif x < width and y >= height:
                out_grid[x, y] = in_grid3[source_x, source_y]
            else:
                out_grid[x, y] = in_grid4[source_x, source_y]

    out_img.save(output_path)


if __name__ == '__main__':
    tiling(
        'images/puppy.png','images/snake.png','images/tree.png','images/woman.png','images/tiling_output.png')
    print('Done!')