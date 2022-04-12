# Best Model for Credit Card Approval

# **프로젝트 개요:**

- **프로젝트 목표**:  신용카드 발급 승인 여부 모델
    - 기존 신용 승인/거절 고객들의 데이터를 기반으로 신규 신청 고객의 신용 승인/거절 예측하는 모델 구축
    - 선정 이유 : 신용 점수는 실생활에서도 매우 밀접하게 연관되어 있어서 흥미로운 주제로 선택
- **프로젝트 기간**: 2021.07.27 - 2021.09.02 [총 7일]
- **사용된 데이터** 🔗[링크](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction)
    - Application, Credit data 2개의 데이터로 구성
    - Good/Bad client의 분류가 별도로 되어 있지 않아 credit data에서의 대출상환 정보를 기반으로 Good/Bad Client 선정
    - Target은 Good Client/Bad Client으로 이중 분류 문제로 접근
- **가설**
    - Occupation type(직업 종류)보다 Total Amount income(연간 수입)의 영향도가 더 클 것이다.
    - XGBoost 모델의 정확도가 가장 클 것이다.

# **프로젝트 내용**

### 데이터 전처리

- Flag_mobil (휴대폰의 소유)는 모든 값이 1 ⇒ 제거
- Occupation type은 240,048(데이터의 총 30.9%)개의 결측치 보유 ⇒ 제거
- Count_children은 540,639(데이터의 총 69.5%)개의 값이 0 ⇒ 정수 값이라 유지
- Months_balance는 24,672(데이터의 총 3.2%)개의 값이 0  ⇒ 정수 값이라 유지

### 데이터 시각화

- Code link

### 모델에 영향을 미치는 feature 파악

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9987108b-710e-43c9-ace0-8ccc75a9e14f/Untitled.png)

- 상관관계를 보았을때 status와 큰 상관계수[ |0.2|로 설정]는 찾아보기 힘들었다.

# 모델링

### Random Forest Classifier

- 베이스라인 모델은 RandomForest 모델로 선정
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/79b2256a-1175-4841-bb96-e6ec1561fcee/Untitled.png)
    
    - 결정 트리를 만들 때 무작위로 선택한 특성들을 활용
    - Bagging sampling 기법을 사용하여 샘플을 복원추출하여 과적합을 피할 수 있는 장점
- 결과
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7bcd6899-208a-444c-8af0-7c8165677146/Untitled.png)
    
    - Data의 불균형으로 인하여 과적합이 일어난 것 확인
