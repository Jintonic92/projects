
# **Heartbeat Predicting Model**

# **프로젝트 개요:**

- **프로젝트 발표 링크**: 🔗[링크](https://drive.google.com/file/d/1wEOWgdYFZ2FlBOzrhFG3_5lW_qhbrchW/view?usp=sharing)
- **프로젝트 목표**:  심장박동수를 가장 잘 예측하는 모델 구축
    - **Wapeul 기업 협업 프로젝트**
    - 비접촉 Radar 데이터를 접촉(ECG)데이터와 비교 학습하여 레이더 데이터만 가지고 HR(Heart Rate)을 정확하게 예측하는 모델 구축
    - **성능 측정법** : MSE, MAE, Error rate
    ![image](https://user-images.githubusercontent.com/86962114/163170683-f7751a58-2889-410e-b50d-6440ce19af78.png)
    
- **프로젝트 기간**: 2021.12.27 - 2022.01.19 [총 23일]
- **사용된 데이터**
    - 기업에서 제공한 11개의 7명의 자세별[sit, lie, sleep] 생체반응 데이터
    ![image](https://user-images.githubusercontent.com/86962114/163170706-eef76c93-f1e1-4c39-802a-01eeb6fb6986.png)
    
    - **FFT :**  신호 데이터를 기존 시간의 관점에서 주파수 관점으로 변환시킨 것
        
        ![image](https://user-images.githubusercontent.com/86962114/163170746-770967ba-da78-404e-aafa-4207b508d313.png)
        
        - (a) 시간에 따른 데이터를 (b) 주기에 따른 데이터로 변환시키는 것      
        - FFT size가 클수록, 주파수 해상도는 증가한다. 윈도우가 늘어나기에 해상도는 더 정확해 진다.     
    - **가설** : 자세에 기반하여 만들어진 모델들의 예측 성능이 좋을 것이다

# **프로젝트 내용**

### Classifying data

![image](https://user-images.githubusercontent.com/86962114/163170785-8d60f3ea-adc4-4717-8ec3-6e8139ed1e63.png)

- 프로젝트는 5개의 데이터가 사용되었다.
    - sleep(les_sleep_1), sit(chc_sit_5), lie0.5(ksj_lie_5), lie1.0(kdu_lie_1), four(앞 4개의 데이터 통합)
- 데이터 선택 이유
    - 11개의 data 중 (A) sleep과 (B) sit 데이터는 각각 1개이기 때문에 사용
    - (B)와 (C)는 Lie 0.5 데이터이다. 둘의 분포가 비슷하여 데이터 수가 더 많은 (C) 사용
    - (E)-(J) 데이터 분포에는 큰 차이가 없어 데이터가 가장 많은 (E) 사용
    - 그리고 앞서 선택한 4개의 대표 데이터를 합친 통합 데이터 사용

### 모델에 영향을 미치는 feature 파악

![image](https://user-images.githubusercontent.com/86962114/163170874-17161a68-2396-465d-873e-62270660da61.png)

- 상관관계를 보았을때 status와 큰 상관계수[ |0.2|로 설정]는 오른쪽 표에서 확인
- 512fft = bin0의 상관계수가 1 ⇒ 제거

# 모델링

## Deep Learning Models

- **Base NN model**
    
    ![image](https://user-images.githubusercontent.com/86962114/163170958-9887e372-c96a-4688-8579-633fac91a5c6.png)
    
    - Kernal Initializer를 Random normal(mean=0.0, stddev=0.05)로 설정하여 정규분포 초기화
    - ReLu = 양의 값이 입력되면 그 값을 그대로 출력, 음의 값은 0으로 변환해주는 activation func
- **Hyper Parameter tuned Model**
    
    ![image](https://user-images.githubusercontent.com/86962114/163170987-052a2146-1e68-4554-bbaf-cdbd3b8cbf7a.png)
    
    - Hyperband를 사용하기 위해 model builder를 정의
        - 은닉층의 node 수 : 32-512까지 32개씩 증가하면서 탐색
        - 학습률 learning rate: 0.1, 0.001, 0.001의 지점을 탐색
- **Result**
    
    ![image](https://user-images.githubusercontent.com/86962114/163171001-3cfe72de-3ae5-4ab3-b1ec-60aa12e6a298.png)
    
    1. 총 5개의 데이터를 base, hypertuned 2개의 모델로 훈련 결과 10개를 나타낸 표
    2. NNB Four 모델의 경우 mse, mae, error rate 모두 높은 것을 알 수 있다. 이는 다양한 자세의 데이터가 있다 보니 predict이 어렵기 때문
    3. Lie 1.0 데이터가 많아, 이를 활용하고자 했지만 의외로 mse, mae 모두 높아 조금 아쉬운 결과가 나왔다.
    4. Lie 0.5 데이터의 mse가 가장 낮게 나왔다. 이는 Lie 0.5 데이터 수가 가장 적기 때문

## Machine Learning Models

- Base Random Forest Model
    
    ![image](https://user-images.githubusercontent.com/86962114/163171040-53e0e992-8396-4ef4-bb19-7ff4448bda79.png)
    
    - Random Forest Regressor vs Classifier
        - Classifier는 class로 분류된 labeling된 데이터에 적합
        - Regressor는 class로 분류되기 어려운 연속적인 결과|숫자에 적합
- Hyperparamter tuned Model
    - Grid search vs Randomized Search
        - Randomized Search는 검증하려는 하이퍼파라미터 값 범위를 지정해주면 무작위로 값을 지정해 그 조합 모두 검증
        - 일반적으로 Randomized Search가 더 좋은 하이퍼파라미터를 찾아준다
    
    ![image](https://user-images.githubusercontent.com/86962114/163171129-ebbe8c04-caed-4a19-834d-e0148c023550.png)
    
- **결과**
    
    ![image](https://user-images.githubusercontent.com/86962114/163171152-8f6acf0d-667b-4f86-a29e-a5e91f6b386c.png)
    
    1. 랜덤포레스트 경우 mse, mae, error rate 모두 nn 모델의 것보다 월등하게 좋은 점수가 나왔다. 과적합의 위험이 있어 보여 추후 test 데이터에서 확인 필요
    2. Tuning으로 인해 좋아진 결과가 미미할 정도의 수준으로 Base 모델의 성능이 매우 좋다. 

# 데이터 전처리

### 이상치 제거

- IQR를 이용한 이상치 제거 전/후
    
    ![image](https://user-images.githubusercontent.com/86962114/163171200-200f800a-e6eb-49ad-b7c8-a0b717d40c95.png)
    

### Log Transform

- 비대칭 분포형태를 정규분포 형태로 바꿔주기 위하여 target을 제외하고 log1p 적용

    ![image](https://user-images.githubusercontent.com/86962114/163171244-aa16cb64-be50-47ea-84ea-b6481c5fef0d.png)


### Scaling

- 정규화를 위하여 MinMax Scaler를 적용

    ![image](https://user-images.githubusercontent.com/86962114/163171273-283c7194-0fff-4c36-9f92-c31fb7d97389.png)


# 모델링(2) 결과

![image](https://user-images.githubusercontent.com/86962114/163171293-67d1a036-816a-4c10-ae4c-8d7988efc5b8.png)

- 전처리한 데이터를 사용한 후의 전체 모델 성능 비교
    - 순위는 MSE 기반으로 선정
    - ML 모델들이 Top 20 상위권

# Best Model로 Test

- 자세를 기반으로 한 모델이 자신과 동일한 자세 데이터에 대한 예측을 잘할 것이다라는 가설 입증 위하여
    - Sleep Model : 다른 데이터가 없어 sit 데이터로 test
    - Sit Model : 다른 데이터가 없어 sleep 데이터로 test
    - Lie 0.5 Model : 다른 Lie 0.5 데이터로 test
    - Lie 1.0 Model : 다른 Lie 1.0 데이터로 test
- 자세를 기반으로 모델을 구축했기에, 통합 Model에서 가장 성능이 좋은 Model을 선택해서 자세별 data를 test
    - ML Best Model : sleep, sit, Lie 0.5, Lie 1.0를 Test
    - DL Best Model : sleep, sit, Lie 0.5, Lie 1.0를 Test
- **결과**
    
    ![image](https://user-images.githubusercontent.com/86962114/163171344-a5a7ab05-29de-4a08-9e52-54d45219e445.png)    
    ![image](https://user-images.githubusercontent.com/86962114/163171386-b602c4c5-384a-4c80-aa87-ea84140b4df2.png)

    ![image](https://user-images.githubusercontent.com/86962114/163171426-0d2ef0cb-dca2-4eba-9285-0073319a55a5.png)
    ![image](https://user-images.githubusercontent.com/86962114/163171450-21845c82-3c68-4f06-80ca-57c94baae7b0.png)


# 결론

- 자세 기반의 모델들은 동일 자세의 Data를 넣는 것이 가장 좋은 성능을 보여주었다.
- 총 40개의 모델 중에서 2개를 제외하고 모든 모델들은 전처리를 한 후에 성능이 향상되었다.
- Hypertuned 모델이 Base 모델보다 항상 더 나은 결과를 보여주지는 않는다.
- 한계점
    - 다양한 모델의 부재
    - 총 11개의 데이터에 대한 test 부재
