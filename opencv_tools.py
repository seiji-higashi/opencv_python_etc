#opencv�ŕ֗��Ȋ֐����W�߂Ēu��

#���{��t�@�C�����Ή�
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
#�yPython�zPillow ? OpenCV �ϊ�
#�O���[�X�P�[���⃿�`�����l���t���̉摜�ł��ϊ��ł���悤�Ɋ֐������܂����B

#Pillow �� OpenCV
import numpy as np
import cv2

def pil2cv(image):
    ''' PIL�^ -> OpenCV�^ '''
    new_image = np.array(image)
    if new_image.ndim == 2:  # ���m�N��
        pass
    elif new_image.shape[2] == 3:  # �J���[
        new_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    elif new_image.shape[2] == 4:  # ����
        new_image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
    return new_image
#cv2���g�킸�ɏ����Ȃ�C

import numpy as np

def pil2cv_np(image):
    ''' PIL�^ -> OpenCV�^ '''
    new_image = np.array(image)
    if new_image.ndim == 2:  # ���m�N��
        pass
    elif new_image.shape[2] == 3:  # �J���[
        new_image = new_image[:, :, ::-1]
    elif new_image.shape[2] == 4:  # ����
        new_image = new_image[:, :, [2, 1, 0, 3]]
    return new_image
#OpenCV �� Pillow
from PIL import Image
import cv2

def cv2pil(image):
    ''' OpenCV�^ -> PIL�^ '''
    new_image = image.copy()
    if new_image.ndim == 2:  # ���m�N��
        pass
    elif new_image.shape[2] == 3:  # �J���[
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # ����
        new_image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image
#cv2���g�킸�ɏ����Ȃ�C

from PIL import Image
def cv2pil_np(image):
    ''' OpenCV�^ -> PIL�^ '''
    new_image = deepcopy(image)
    if new_image.ndim == 2:  # ���m�N��
        pass
    elif new_image.shape[2] == 3:  # �J���[
        new_image = new_image[:, :, ::-1]
    elif new_image.shape[2] == 4:  # ����
        new_image = new_image[:, :, [2, 1, 0, 3]]
    new_image = Image.fromarray(new_image)
    return new_image

#�摜�ɓ��{��\��
#https://www.tech-tech.xyz/drawtext.html
from PIL import Image, ImageDraw, ImageFont

def draw_text(img,text,pos=(10,10),color=(255,255,255),font_file="C:\Windows\Fonts\meiryob.ttc",font_size=27):
	#�摜�̓ǂݍ���
	#img = Image.open("cat.jpg")
	img_pil=cv2pil(img)
	#draw�C���X�^���X�𐶐�
	draw = ImageDraw.Draw(img_pil)
	#�t�H���g�̐ݒ�(�t�H���g�t�@�C���̃p�X�ƕ����̑傫��)
	font = ImageFont.truetype(font_file, font_size)
	#����������
	#draw.text((10, 10), u'��y�͔L�ł���B', fill=(255, 0, 0), font=font)
	#���s�ł���
	#draw.text((10, 10), u'\n���O�͂܂������B', fill=(0, 0, 255), font=font)
	draw.text(pos, text,', fill=color, font=font)
	#img.save("cat_text.jpg")
	return(pil2cv(img_img))
