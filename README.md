  ## project 2. Django_MachineLearning
  ## B-8 연봉팔조
 
   ![image](https://ifh.cc/g/JoKNoJ.jpg)

  <p>
      <img src="https://img.shields.io/badge/Django-4.1.1-green"/>
  </p>

  ***

  ### 소개
  - 얼굴 인식을통해 내가 타이타닉에서 살아남을 확률은 얼마나 될까?

  ***



  ### 개발 일정
  **진행기간** 2022년 10월 17일 ~ 2022년 10월 20일

  **10월 17일** S.A 내용 작성 

  **10월 18일** 업로드한 이미지 사물인식 구현,S.A 1차 수정 (와이어 프레임)

  **10월 19일** 업로드한 이미지에서 나이,얼굴 인식 구현 S.A2차수정 (ERD,API,git readme)

  **10월 20일** 19일날 한 작업물과 사용자의 정보를  타이타닉 데이터셋에 입력 후 생존확률 구현


  ### 프로젝트 참여한 명단 및 역할

  안범기: 머신러닝 +프론트엔드

  유형석: 머신러닝 +프론트엔드

  김규현: 머신러닝 +프론트엔드

  최윤선: 백엔드 +프론트엔드

  김서영: 백엔드 +프론트엔드

  ***


  ### API 설계

  |페이지|기능|API URL|Method|Request(요청)|Response(응답)|
  |------|------|------|------|------|------|
  |로그인|login|login/|POST||username,password|'user/login','user/login.html'|
  |회원가입|singup|signup/|GET,POST|username,passoword,nickname|'user/signup.html',redirect('/login')|
  |메인|images upload|home/|GET,POST|temp,temp2,category,result,|'tweet/home.html', {'total_img': result},redirect('/')|
  


  ***


  ### 와이어프레임

  * home,signup,main

    ![image](https://ifh.cc/g/BJ4DVx.png)



  * erd

  ![image](https://ifh.cc/g/fZOnoo.png)






  ***




  ***



  ### 주요 기능 

  - #### 사람의 얼굴 인식
    - 입력된 이미지에서 사람의 얼굴이 있는지 확인하고 머신러닝을통해서 나이와성별을 유추
  - ##### 타이타닉에서 생존확률 구하기
  -  얼굴에서 인식한 나이와 성별 그리고 몇가지의 정보를 토대로 타이타닉탑승객의 
        데이터셋을 비교해서 생존확률의 %를 나타냄

  사용한 데이터셋 모델 - Titanic - Machine Learning from Disaster

  https://www.kaggle.com/code/scatteredflo/titanic-tutorial-for-study-200409/data
  ## 1. 이미지 분석

## 2. 이미지 분석후 나온 결과값 타이타닉 데이터셋에 인풋

## 3. 타이타닉 데이터셋에 정보를 넣음

## 4. 2,3의 정보를 토대로 결과물 출력



  <br/>

  ***




