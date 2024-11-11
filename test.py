import cv2

path = r'C:\Users\Administrator\Desktop\交大_培訓\U-2-Net-master\test_data\test_images\bike.jpg'

img = cv2.imread(path)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()