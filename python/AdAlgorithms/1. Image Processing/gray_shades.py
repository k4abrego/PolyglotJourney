from PIL import Image
from typing import cast
from rgb_types import RGBTuple, RGBStream

def grayify(input_path: str,
            out_path1: str,
            out_path2: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data()) 
        size: tuple[int, int] = in_img.size
    out_stream1: list[int] = [] #list to hold the pixel data for the output image
    out_stream2: list[int] = [] #list to hold the pixel data for the output image
    red: int
    green: int
    blue: int
    for (red, green, blue) in in_stream:
        average: int = (red + green + blue) // 3
        out_stream1.append(average)
        luma: int = int(0.299 * red + 0.587 * green + 0.114 * blue)
        out_stream2.append(luma)

    out_img1: Image.Image = Image.new('L', size) 
    out_img1.putdata(out_stream1) 
    out_img1.save(out_path1)

    out_img2: Image.Image = Image.new('L', size) 
    out_img2.putdata(out_stream2) 
    out_img2.save(out_path2)

if __name__ == '__main__':
    grayify('images/snake.png', 'images/snake_gray_avg.png', 'images/snake_gray_luma.png')