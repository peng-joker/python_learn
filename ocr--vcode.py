# import easyocr
# reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
# result = reader.readtext('haha.png',detail = 0)
# print(result)


# from PIL import Image
# import pytesseract
#
# # 打开图片
# image = Image.open("yzm.png")
#
# # 识别图片中的文字
# text = pytesseract.image_to_string(image)
#
# print("识别结果：", text)

# # 线上图片地址
# import ddddocr
# import urllib.request
#
# def urlretrieve_with_headers(url, fileName, headers={}):
#     req = urllib.request.Request(url, headers=headers)
#     with urllib.request.urlopen(req) as response:
#         with open(fileName, 'wb') as out_file:
#             out_file.write(response.read())
#
#     ocr = ddddocr.DdddOcr(show_ad=False,use_gpu=False)
#     image = open(fileName, "rb").read()
#     result = ocr.classification(image)
#     print(result)
#     return result
#
# url = 'https://eparts.ceair.com/station/muframe-web/login/images/captcha/ca88515d-957b-d37b-af40-330d5b2ef722'
# fileName = 'haha1.jpg'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# urlretrieve_with_headers(url, fileName, headers)


# 本地图片地址
import ddddocr
import urllib.request
def urlretrieve_with_local(file_name):
    ocr = ddddocr.DdddOcr(show_ad=False, use_gpu=False)
    image = open(file_name, "rb").read()
    result = ocr.classification(image)
    print(result)
urlretrieve_with_local("yueA.png")
