## 2021 머신러닝 모델을 이용한 비행기 만족도 예측 API 구축 프로젝트
데이터 파이프라인 구축 프로젝트

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
___
