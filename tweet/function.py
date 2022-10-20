import cv2
import numpy as np
import joblib

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes
    
faceProto="tweet/face/opencv_face_detector.pbtxt"
faceModel="tweet/face/opencv_face_detector_uint8.pb"
ageProto="tweet/face/age_deploy.prototxt"
ageModel="tweet/face/age_net.caffemodel"
genderProto="tweet/face/gender_deploy.prototxt"
genderModel="tweet/face/gender_net.caffemodel"

MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['Male','Female']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

def photo(img):
    video=cv2.VideoCapture(f'.{img.url}') #이미지 읽어주는 코드 args.image 파일에 경로가 들어가 있음/media/
    padding=20
    result_gender = []
    result_age = []

    while cv2.waitKey(1)<0:
        hasFrame,frame=video.read()
        if not hasFrame:
            cv2.waitKey()
            break

        resultImg,faceBoxes=highlightFace(faceNet,frame)
        if not faceBoxes:
            print("No face detected")
            return 0, 0

        for faceBox in faceBoxes:
            face=frame[max(0,faceBox[1]-padding):
                    min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)
                    :min(faceBox[2]+padding, frame.shape[1]-1)]

            blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPreds=genderNet.forward()
            gender=genderList[genderPreds[0].argmax()]
            print(f'Gender: {gender}')
            result_gender.append(gender)

            ageNet.setInput(blob)
            agePreds=ageNet.forward()
            age=ageList[agePreds[0].argmax()]
            print(f'Age: {age[1:-1]} years')
            result_age.append(age)

            cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
            # cv2.imshow("Detecting age and gender", resultImg)
    
    return result_gender, result_age

def is_survived(passenger_info:list) -> int:
    # model = joblib.load('titanic_LR_model.pkl')
    # file_name = 'titanic_LR_model.pkl'
    model = joblib.load('titanic_LR_model.pkl')
    result = model.predict(passenger_info)
    # 입력 = [[객실등급, 성별(남자1, 여자0), 요금, 탑승위치(0, 1, 2), 나이(밴드형식), 같이온사람의 수, 혼자왔나?]]
    # 결과 = model.predict(입력)
    # 살았으면 1 죽었으면 0
    # # name, 객실 등급(1,2,3), 요금, 탑여승위치(인천항, 수 광양항, 부산항), 같이 온 사람들()
    return result