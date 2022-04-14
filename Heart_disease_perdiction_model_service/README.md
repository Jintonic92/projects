# Heart Failure Prediction Service

# **프로젝트 개요:**

- **프로젝트 발표 링크**: 🔗[링크](https://drive.google.com/file/d/14z8xwbDHON_YNIazv_lEDc6_QwuYV63a/view?usp=sharing)
- **프로젝트 목표**:  심부전 예방 모델 서비스
- **데이터 선정 이유** : 심혈관 질환(CVD)은 전 세계적으로 사망 원인 1위이며 매년 약 1,790만 명이 사망하며 이는 전 세계 사망률의 31%를 차지한다. 심부전은 CVD로 인해 발생하는 현상 중 하나이며 이 데이터 세트에는 심부전으로 인한 사망률을 예측하는 데 사용할 수 있는 12가지 기준(feature)이 포함되어 있다. **심혈관 위험이 높은 사람은 이번 서비스 모델을 통해 조기 발견 및 관리에 도움을 받을 수 있을 것으로 생각하여 데이터 셋을 선정했다.**
- **프로젝트 기간**: 2021.10.06 - 2021.10.12 [총 7일]
- **서비스 파이프라인**
    
    ![image](https://user-images.githubusercontent.com/86962114/163324854-0992973d-2170-4393-8e65-f2f478e56408.png)

    
- **사용된 데이터** 🔗[링크](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data)
    - Feature 설명 ( Target : Death_Event)
    
    ![image](https://user-images.githubusercontent.com/86962114/163324870-da3bbd4f-b8fb-4054-9c9c-042339703a43.png)
    

# **프로젝트 내용**

# EDA (using BI Tools)  🔗[링크](https://datastudio.google.com/reporting/7b040677-65cd-4e63-9411-549a2a936325)

![image](https://user-images.githubusercontent.com/86962114/163324887-c9d7e61e-5583-4ee9-9ad0-11c07d501feb.png)

- Death Event와 상관관계가 높은 feature들은 age, ejection_fraction, serum_creatinine, time 가 있었다.
    - time은 관찰일자 ⇒ 제거
- 상관관계가 높은 Feature와 Target과의 상관성을 확인하기 위한 도표
    
![image](https://user-images.githubusercontent.com/86962114/163324903-64c08002-091b-4893-a4ad-15aa5e84a532.png)
    
    - **나이가 많을 수록, 심장 박출계수가 높을 수록, 혈중 크레아틴 레벨이 높을수록 신부전 위험(사망률)이 높은 것을 확인**

# SQLITE DB 생성
![image](https://user-images.githubusercontent.com/86962114/163324922-f791b102-521f-426b-b572-bf7d8fb584e8.png)

# MODELING

## Random Forest Classifier

![image](https://user-images.githubusercontent.com/86962114/163324941-b90e1f45-b74c-4dcf-9ddf-8c338bcd9fe8.png)

- Random Forest Regressor vs Classifier
    - **Classifier는 class로 분류된 labeling된 데이터에 적합**
    - Regressor는 class로 분류되기 어려운 연속적인 결과|숫자에 적합
- Accuracy 98.52 의 모델을 Flask API에서 사용하기 위하여 pickle로 저장 및 불러오기 사용

# FLASK API

- FLASK app에서의 작성 화면 및 결과물
- 왼쪽 [ 사망자 정보 입력 화면 ] 오른쪽 [ 생존자 정보 입력 화면 ]

![image](https://user-images.githubusercontent.com/86962114/163324970-212c1f4b-9891-4c26-be15-24ad37fa5f4c.png)

# 결론 및 한계점

- 데이터 학습영역과 서비스 구현 영역을 분리하여 작업 할 수 있게 되었음
- **한계점**
    - HTML 학습을 통한 단조로운 화면 구성 수정 필요
    - FLASK를 처음 이용하는 것이다 보니 오류사항이 많아 모델링에 투자를 많이 못한 아쉬움
