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
from rgb_types import RGBTuple, RGBStream

def posterization(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream,in_img.get_flattened_data())
        size: tuple[int, int] = in_img.size
    out_stream: list[RGBTuple] = []
    red: int
    green: int
    blue: int
    for (red, green, blue) in in_stream:
        average: int = (red + green + blue) // 3
        if average < 50:
            out_stream.append((120, 41, 15))
        elif average < 130:
            out_stream.append((255, 125, 0))
        else:
            out_stream.append((255, 236, 209))

    out_img: Image.Image = Image.new('RGB', size)
    out_img.putdata(out_stream)
    out_img.save(output_path)


if __name__ == '__main__':
    posterization('images/posterization-img.jpg', 'images/posterization_output.png')
    print('Done!')