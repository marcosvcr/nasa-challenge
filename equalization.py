import numpy as np
import cv2
import sys

input_image = cv2.imread(sys.argv[1])
if input_image is None:
    print('Could not load image: ', input_image)
    exit(0)


blue, green, red = cv2.split(input_image)


hist_blue = cv2.calcHist([blue], [0], None, [256], [0, 256])
hist_green = cv2.calcHist([green], [0], None, [256], [0, 256])
hist_red = cv2.calcHist([red], [0], None, [256], [0, 256])


cdf_blue = hist_blue.cumsum()
cdf_green = hist_green.cumsum()
cdf_red = hist_red.cumsum()


cdf_blue_masked = np.ma.masked_equal(cdf_blue, 0)
cdf_green_masked = np.ma.masked_equal(cdf_green, 0)
cdf_red_masked = np.ma.masked_equal(cdf_red, 0)


cdf_blue_masked = (cdf_blue_masked - cdf_blue_masked.min())*255 / (cdf_blue_masked.max() - cdf_blue_masked.min())
cdf_green_masked = (cdf_green_masked - cdf_green_masked.min())*255 / (cdf_green_masked.max() - cdf_green_masked.min())
cdf_red_masked = (cdf_red_masked - cdf_red_masked.min())*255 / (cdf_red_masked.max() - cdf_red_masked.min())

cdf_final_b = np.ma.filled(cdf_blue_masked, 0).astype('uint8')
cdf_final_g = np.ma.filled(cdf_green_masked, 0).astype('uint8')
cdf_final_r = np.ma.filled(cdf_red_masked, 0).astype('uint8')


blue_img = cdf_final_b[blue]
green_img = cdf_final_g[green]
red_img = cdf_final_r[red]


final_equ_img = cv2.merge((blue_img, green_img, red_img))
cv2.imwrite('result.png', final_equ_img)

cv2.waitKey(0)
cv2.destroyAllWindows()