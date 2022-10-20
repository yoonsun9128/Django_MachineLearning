from django.test import TestCase
import torch
import cv2
import joblib

# Create your tests here.
def change_img(file_path):
    # file_path -> img_upload
    model = torch.hub.load('ultralytics/yolov5', 'yolov5l', pretrained=True)

    fixed_path = f'./media/images/{file_path}'
    changed_file_store_path = f'./media/images/after_image{file_path}'

    origin_img = cv2.imread(fixed_path)
    changed_img = cv2.imread(fixed_path)

    results = model(origin_img)
    result = results.pandas().xyxy[0].to_numpy()

    for i in range(len(result)):
        cv2.rectangle(changed_img, (int(results.xyxy[0][i][0].item()), int(results.xyxy[0][i][1].item())), 
              (int(results.xyxy[0][i][2].item()), int(results.xyxy[0][i][3].item())), (255,0,0))
    
    cv2.imwrite(changed_file_store_path, changed_img)
    # filename, changed_img

    category_list = list({x[6] for x in result})

    changed_img_file_path = f'after_image{file_path}'

    return changed_img_file_path, category_list

def is_survived(passenger_info:list) -> int:
    model = joblib.load('./Django_MachineLearning/titanic_LR_model.pkl')
    test_test = model.predict
    return 