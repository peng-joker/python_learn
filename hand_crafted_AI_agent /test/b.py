from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch",show_log= False)  # need to run only once to download and load model into memory
count = 1
while count <= 48:
    img_path = f"./pic/pic{count}.jpg"
    result = ocr.ocr(img_path)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            if len(line[1][0]) < 5:
                continue
            print(line[1])
        print(f"{count}--------------------------")
    count += 1
