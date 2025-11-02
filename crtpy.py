import os
import cv2
import numpy as np

PAT_CIRCLE_10X10 = f'./src/crt-patterns/PAT_CIRCLE_10X10.png'

PAT_DIAGONAL_SHADOW_4X4 = f'./src/crt-patterns/PAT_DIAGONAL_SHADOW_4X4.png'
PAT_DIAGONAL_SAMSUNG_8X8 = f'./src/crt-patterns/PAT_DIAGONAL_SAMSUNG_8X8.png'
PAT_DIAGONAL_16X16 = f'./src/crt-patterns/PAT_DIAGONAL_16X16.png'
PAT_DIAGONAL_PANASONIC_16X16 = f'./src/crt-patterns/PAT_DIAGONAL_PANASONIC_16X16.png'

PAT_HORIZONTAL_6X6 = f'./src/crt-patterns/PAT_HORIZONTAL_6X6.png'
PAT_HORIZONTAL_8X8 = f'./src/crt-patterns/PAT_HORIZONTAL_8X8.png'
PAT_HORIZONTAL_16X16 = f'./src/crt-patterns/PAT_HORIZONTAL_16X16.png'

PAT_HORIZONTAL_GLOW_3X3 = f'./src/crt-patterns/PAT_HORIZONTAL_GLOW_3X3.png'
PAT_HORIZONTAL_GLOW_6X6 = f'./src/crt-patterns/PAT_HORIZONTAL_GLOW_6X6.png'

PAT_HORIZONTAL_SPARSE_5X5 = f'./src/crt-patterns/PAT_HORIZONTAL_SPARSE_5X5.png'
PAT_HORIZONTAL_SPARSE_GLOW_5X5 = f'./src/crt-patterns/PAT_HORIZONTAL_SPARSE_GLOW_5X5.png'

PAT_VERTICAL_8X8 = f'./src/crt-patterns/PAT_VERTICAL_8X8.png'
PAT_VERTICAL_16X16 = f'./src/crt-patterns/PAT_VERTICAL_16X16.png'
PAT_VERTICAL_SPARSE_15X15 = f'./src/crt-patterns/PAT_VERTICAL_SPARSE_15X15.png'

class CRTConverter():
    def __init__(self, pattern = PAT_HORIZONTAL_GLOW_3X3):

        self.pattern = pattern

        self.pattern = cv2.imread(self.pattern)

        self.pattern = (self.pattern / 255.).astype(np.float32)

        self.pat_y, self.pat_x, _ = self.pattern.shape

        return

    def convert_crt(self, image):
        res_y, res_x, _ = image.shape

        _image = image.copy().astype(np.float32)

        _pattern = self.pattern.copy()
        _pattern = np.tile(_pattern, [res_y, res_x, 1])

        _image = cv2.resize(_image, dsize = (res_x * self.pat_x, res_y * self.pat_y), interpolation = cv2.INTER_NEAREST)

        _pattern = (_pattern * _image).astype(np.uint8)
        _image = _image.astype(np.uint8)

        return _pattern, _image

if __name__ == '__main__':
    converter = CRTConverter(PAT_HORIZONTAL_GLOW_6X6)

    file_path = f'./src/demo-images/'
    file_list = os.listdir(file_path)

    for file_name in file_list:
        pkm = cv2.imread(file_path + file_name)

        pkm_crt, pkm_org = converter.convert_crt(pkm)

        result = np.concatenate([pkm_org, pkm_crt], axis = 1)
        cv2.imwrite(f'./src/results/{file_name}', result)