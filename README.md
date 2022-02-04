## 2021 머신러닝 모델을 이용한 비행기 만족도 예측 API 구축 프로젝트
데이터 파이프라인 구축 프로젝트: LGBM, XGB, CAT 모델을 성능을 비교하여 가장 성능이 좋은 모델을 사용하여 비행기 만족도 예측 API 배포
### 데이터
Airline Passenger Satisfaction

항공사 만족도 설문이 포함되어 있는 데이터
- 위드코로나 시작하면 늘어날 해외여행 증가를 위한 비행기 만족도에 영향을 미칠 요소를 파악하고, 예측 모델을 만들기 위해 사용

train shape: (103904, 25) test shape:  (25976, 25)

target: Satisfaction

### 내용
데이터 postgrSQL에 저장

비행기 만족도 예측 모델 구현: LGBM, XGB, CAT 모델을 성능을 비교

- LGBMClassifier: precison 0.95, recall 0.97, f1-score 0.96, accuracy0.95

API 제작 및 Heroku로 배포  
- https://poanpo.herokuapp.com/
호화
### 한계 및 보완점
- heroku는 Region 이수로 API가 로딩속도가 느리기에 AWS EC2로 배포해보기
- 모델의 결과가 모두 동일하므로 정보의 누수가 있었는지 확인 및 보완
- 해외 데이터만 다루었기에 한국데이터도 추가하여 보완
___
