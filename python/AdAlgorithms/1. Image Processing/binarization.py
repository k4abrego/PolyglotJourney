from PIL import Image
from typing import cast
from rgb_types import RGBTuple, RGBStream

threshold = 130
#threshold = 100
#threshold = 200

def binarization(input_path: str, output_path: str) -> None:
    in_img: Image.Image
    with Image.open(input_path) as in_img:
        in_img = in_img.convert('RGB')
        in_stream: RGBStream = cast(RGBStream, in_img.get_flattened_data()) 
        size: tuple[int, int] = in_img.size
    out_stream: list[RGBTuple] = []
    green: int
    for (_, green, _) in in_stream:
        out_stream.append(0 if green < threshold else 1) #the conditional statement below will determine if the pixel is black or white based on the threshold value
        # if green < threshold:
        #     out_stream.append(1)
        # else:
        #     out_stream.append(0)

    out_img: Image.Iamge = Image.new('1', size)
    out_img.putdata(out_stream)
    out_img.save(output_path)

if __name__ == '__main__':
    binarization('images/woman.png', 'images/binarify_woman.png')
