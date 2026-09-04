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

def lsb_embedding(input_path: str, secret_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data())
        size: tuple[int, int] = in_img.size

    secret_img: Image.Image
    with Image.open(secret_path) as secret_img:
        secret_img = secret_img.convert('1')
        secret_stream: tuple[int, ...] = cast(tuple[int, ...],secret_img.get_flattened_data())
        secret_size: tuple[int, int] = secret_img.size
    assert size == secret_size
    out_stream: list[RGBTuple] = []
    red: int
    green: int
    blue: int
    secret: int
    for (red, green, blue), secret in zip(in_stream,secret_stream):
        secret_bit: int = secret // 255
        new_green: int = (green & 254) | secret_bit

        out_stream.append(
            (red, new_green, blue)
        )

    out_img: Image.Image = Image.new('RGB',size)
    out_img.putdata(out_stream)
    out_img.save(output_path)

if __name__ == '__main__':
    lsb_embedding('images/snake.png','images/one_bit_image.png','images/lsb_embedding_output.png')
    print("Done!")