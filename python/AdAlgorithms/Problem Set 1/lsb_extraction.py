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
from rgb_types import RGBStream


def lsb_extraction(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data())
        size: tuple[int, int] = in_img.size
    out_stream: list[int] = []
    green: int
    for (_, green, _) in in_stream:
        out_stream.append(green & 1)
    out_img: Image.Image = Image.new('1', size)
    out_img.putdata(out_stream)
    out_img.save(output_path)



if __name__ == '__main__':
    lsb_extraction('images/snake.png','images/lsb_extraction_output.png')
    print('Done!')