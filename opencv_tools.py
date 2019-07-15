#opencvで便利な関数を集めて置く

#日本語ファイル名対応
#https://qiita.com/SKYS/items/cbde3775e2143cad7455
import numpy as np
import cv2
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

import numpy as np
import cv2
import os
def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

#https://qiita.com/derodero24/items/f22c22b22451609908ee
#【Python】Pillow ? OpenCV 変換
#グレースケールやαチャンネル付きの画像でも変換できるように関数化しました。

#Pillow → OpenCV
import numpy as np
import cv2

def pil2cv(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(new_image, cv2.COLOR_RGBA2BGRA)
    return new_image
#cv2を使わずに書くなら，

import numpy as np

def pil2cv_np(image):
    ''' PIL型 -> OpenCV型 '''
    new_image = np.array(image)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = new_image[:, :, ::-1]
    elif new_image.shape[2] == 4:  # 透過
        new_image = new_image[:, :, [2, 1, 0, 3]]
    return new_image
#OpenCV → Pillow
from PIL import Image
import cv2

def cv2pil(image):
    ''' OpenCV型 -> PIL型 '''
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image
#cv2を使わずに書くなら，

from PIL import Image
def cv2pil_np(image):
    ''' OpenCV型 -> PIL型 '''
    new_image = deepcopy(image)
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = new_image[:, :, ::-1]
    elif new_image.shape[2] == 4:  # 透過
        new_image = new_image[:, :, [2, 1, 0, 3]]
    new_image = Image.fromarray(new_image)
    return new_image

#画像に日本語表示
#https://www.tech-tech.xyz/drawtext.html
from PIL import Image, ImageDraw, ImageFont

#def draw_text(img,text,pos=(10,10),color=(255,255,255),font_file="C:\Windows\Fonts\meiryob.ttc",font_size=27):
def draw_text(img,text,pos=(10,10),color=(255,255,255),font_file="TanukiMagic.ttf",font_size=27):
	#画像の読み込み
	#img = Image.open("cat.jpg")
	img_pil=cv2pil(img)
	#drawインスタンスを生成
	draw = ImageDraw.Draw(img_pil)
	#フォントの設定(フォントファイルのパスと文字の大きさ)
	font = ImageFont.truetype(font_file, font_size)
	#文字を書く
	#draw.text((10, 10), u'吾輩は猫である。', fill=(255, 0, 0), font=font)
	#改行できる
	#draw.text((10, 10), u'\n名前はまだ無い。', fill=(0, 0, 255), font=font)
	draw.text(pos, text, fill=color, font=font)
	#img.save("cat_text.jpg")
	return(pil2cv(img_pil))
