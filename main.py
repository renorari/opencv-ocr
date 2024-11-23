import sys
import cv2
import pyocr
from PIL import Image

# 画像ファイルのパス
image = "test.png"

# 画像ファイルの読み込み
img = cv2.imread(image)

# python ocrで使用するツールを取得(今回はtesseractを使用)
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

# 画像ファイルをOCRで読み込む
res = tool.image_to_string(
    Image.open(image)
    ,lang="eng")

# 結果を出力
print(res)