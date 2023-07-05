from paddleocr import PaddleOCR, draw_ocr
# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch") # need to run only once to download and load model into memory
# img_path = './doc/imgs/11.jpg'
# img_path = './doc/imgs/00015504.jpg'
img_path = './doc/imgs/00111002.jpg'
result = ocr.ocr(img_path, cls=True)

ocr_result = []
for line in result:
    # print(len(line))
    # print(line)
    ocr_result=line
# for line in ocr_result:
#     print(line)
#     print("\n")

# 显示结果
from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in ocr_result]
txts = [line[1][0] for line in ocr_result]
scores = [line[1][1] for line in ocr_result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result2.jpg')
