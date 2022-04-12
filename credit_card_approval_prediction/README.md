# Best Model for Credit Card Approval

# **프로젝트 개요:**
- **프로젝트 발표 링크**: https://drive.google.com/file/d/1Aig6aaIZvkwFduWtx5scsAITmVtrsj0T/view?usp=sharing
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

- 🔗[링크](https://github.com/Jintonic92/projects/blob/main/credit_card_approval_prediction/Credit_Card_approval_model.ipynb)

### 모델에 영향을 미치는 feature 파악

![image](https://user-images.githubusercontent.com/86962114/162906709-a3f886ea-2248-4c2d-bf59-9eda244999ed.png)


- 상관관계를 보았을때 status와 큰 상관계수[ |0.2|로 설정]는 찾아보기 힘들었다.

# 모델링

### Random Forest Classifier

- 베이스라인 모델은 RandomForest 모델로 선정
    
![image](https://user-images.githubusercontent.com/86962114/162906751-a240cf34-1f2d-4438-b2f7-4568c9f10d38.png)
    
    - 결정 트리를 만들 때 무작위로 선택한 특성들을 활용
    - Bagging sampling 기법을 사용하여 샘플을 복원추출하여 과적합을 피할 수 있는 장점
- 결과
    
![image](https://user-images.githubusercontent.com/86962114/162906832-99aef4d2-59cf-433c-8ded-78b5d284c5e3.png)
    
    - Data의 불균형으로 인하여 과적합이 일어난 것 확인
    - Logistic Regression, Decision Tree, XGBoost에서 모두 비슷한 결과 확인
# 데이터 불균형 처리

1. **MinMaxScaler 사용**
    - 각 Feature 값을 일정한 범위 또는 규칙에 따르게 하기 위한 스케일링
2. **SMOT 기법 사용**
    - SMOTE(Synthetic Minority Over Sampling Techniques)은 비율이 낮은 분류의 데이털르 표본으로 더 많이 생성하는 방법
- **결과**
    
![image](https://user-images.githubusercontent.com/86962114/162909368-e9910422-4ce3-4a74-9314-4fcde08ce904.png)
    
    - 과적합 문제가 나아지면서 정확도가 낮아졌다.
    - **모델들의 총 결과**
    
![image](https://user-images.githubusercontent.com/86962114/162909334-01fdeee4-0368-41e5-99fa-4bd9d4f69576.png)
    
    - XGBoost 의 f1-score가 가장 높았다.
    

# 결론

- 가설 검증
    - Occupation type보다 total amount income의 영향도가 클 것이다.
     ⇒ 아쉽게도 Occupation type은 결측치가 너무 많아 feature selection에서 제외되었다. Total Amount income은 feature importance에서 항상 Top3안에 들은 유일한 Feature임으로 중요한 Feature인 것으로 사료
        
- 분석 한계점
    - ROC Curve, AUC 점수를 활용하지 못했다는 아쉬움
    : 특히 각 범주를 예측하는 기준이 되는 임계값의 위치에 따라 정밀도나 재현율이 달라지기 때문에 문제의 상황에 따라 적절한 임계값을 선택할 필요성이 있다. 이진 분류 문제에서 ROC curve와 AUC 점수를 잘 활용하면 좋은 결과를 만들어낼 수 있었을 것이다.
