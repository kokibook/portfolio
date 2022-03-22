import os
from django.conf import settings
import environ
import shutil
import cv2
import numpy as np
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scamphotoproject import settings

classes = ["purikura", "mask", "snow", "degree", "normal"]


env = environ.Env()
env.read_env(os.path.join(settings.BASE_DIR, '.env'))
KEY = env('KEY')
ENDPOINT = env('ENDPOINT')

# 顔部分を正方形で取得する関数
def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top  = rect.top
    
    if rect.width > rect.height:
        width  = rect.width
        height = rect.width
    else:
        width  = rect.height
        height = rect.height

    return (left, top, width, height)


# 顔を切り取る関数
def face_cut(filepath, upload_filename):
    image = open(filepath, 'rb')
    img = cv2.imread(filepath)
    img = np.array(img)

    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    detected_faces = face_client.face.detect_with_stream(image)

    for face in detected_faces:
        x, y, w, h = getRectangle(face)
        face_cut = img[y:y+h, x:x+w]
        output_dir = "media/face_images"
        
        # output_dirを初期化
        shutil.rmtree(output_dir)
        os.makedirs(output_dir, exist_ok=True)

        face_image_filepath = "{}/{}".format(output_dir, upload_filename)
        cv2.imwrite(face_image_filepath, face_cut)

    return face_image_filepath