from pytesseract import Output
import csv
from preprocess import *

# text=pytesseract.image_to_string(main())
custom_config = r'-l eng+hin --psm 4'
img=main()
text=pytesseract.image_to_string(img, config=custom_config)
print(text)
with open('extracted_text.txt', 'w', newline="") as file:
    csv.writer(file, delimiter=" ").writerows(text)
    print('Text successfully extracted in "extracted_text.txt file')
details = pytesseract.image_to_data(img, output_type=Output.DICT)
# print(details.keys())
d = details
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imwrite('Boundin_box.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(text)
