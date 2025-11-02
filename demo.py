import cv2
import numpy as np
import crtpy as crt

if __name__ == '__main__':
    pattern = crt.PAT_HORIZONTAL_GLOW_6X6

    converter = crt.CRTConverter(pattern)

    pikachu = cv2.imread(f'./src/demo-images/pikachu.png')

    pikachu_crt, pikachu_org = converter.convert_crt(pikachu)

    result = np.concatenate([pikachu_org, pikachu_crt], axis = 1)

    cv2.imwrite(f'./src/results/pikachu.png', result)