from PIL import Image
from typing import cast
from rgb_types import RGBTuple, RGBStream

ALPHA: float = 0.5

def blending(input_path1: str, 
             input_path2: str, 
             output_path: str) -> None:
    in_img1: Image.Image
    with Image.open(input_path1) as in_img1:
        in_img1 = in_img1.convert('RGB')
        in_stream1: RGBStream = cast(RGBStream, in_img1.get_flattened_data()) #
        size1: tuple[int, int] = in_img1.size 

    in_img2: Image.Image
    with Image.open(input_path2) as in_img2:
        in_img2 = in_img2.convert('RGB')
        in_stream2: RGBStream = cast(RGBStream, in_img2.get_flattened_data()) #
        size2: tuple[int, int] = in_img2.size

    assert size1 == size2

    out_stream: list[RGBTuple] = []

    r1: int
    g1: int
    b1: int
    r2: int
    g2: int
    b2: int

    for (r1, g1, b1), (r2, g2, b2) in zip(in_stream1, in_stream2): #putting both images pixel data together to be able to blend them
        color = (
            int (r1 * ALPHA + r2 * (1 - ALPHA)),
            int (g1 * ALPHA + g2 * (1 - ALPHA)),
            int (b1 * ALPHA + b2 * (1 - ALPHA))
        )
        out_stream.append(color)
    out_img: Image.Image = Image.new('RGB', size1) 
    out_img.putdata(out_stream) 
    out_img.save(output_path) 

if __name__ == '__main__':
    blending('images/puppy.png', 'images/sunset.png', 'images/puppy_sunset.png')
    print("Done!")


