from django.test import TestCase
import torch
import cv2

# Create your tests here.
def change_img(file_path):
    # file_path -> img_upload
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    img = cv2.imread(file_path)

    results = model(img)

    changed_file_path = ''
    # results.save()
    result = results.pandas().xyxy[0].to_numpy()

    result = [item for item in result if item[6]=='person']

    category_list = list({x[6] for x in result})

    return changed_file_path, category_list