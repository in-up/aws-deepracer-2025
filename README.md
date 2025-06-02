## 2025 AWS DeepRacer Reward Function
2025 AWS DeepRacer 출전 보상 함수를 다루는 리포지토리입니다.

## 학습 환경 (Training Environment)
- **레이스 타입(Race type)**: Time trial  
- **환경 시뮬레이션(Environment simulation)**: re:Invent 2018 – Counterclockwise  
- **센서(Sensor)**: Lidar, Stereo camera  
- **액션 스페이스 타입(Action space type)**: Continuous  
  - 속도(Speed): [0.8, 2.2] m/s  
  - 조향 각도(Steering angle): [−30, 30] °  
- **프레임워크(Framework)**: TensorFlow  
- **강화 학습 알고리즘(Reinforcement Learning Algorithm)**: PPO (Proximal Policy Optimization)  
- **학습 시간**: 120 mins

## 하이퍼파라미터 (Hyperparameters)

| 하이퍼파라미터                                          | 값        |
| ------------------------------------------------------ | -------- |
| Gradient descent batch size                            | 64       |
| Entropy                                                | 0.008    |
| Discount factor                                        | 0.999    |
| Loss type                                              | Huber    |
| Learning rate                                          | 0.0003   |
| Number of experience episodes between each policy update | 20       |
| Number of epochs                                       | 10       |



> - **Gradient descent batch size(배치 크기)**: 한 번의 그래디언트 업데이트에 사용되는 샘플 수를 의미한다.
> - **Entropy(엔트로피 계수)**: 정책의 탐험(exploration)을 유지하기 위해 추가되는 엔트로피 보너스 계수
> - **Discount factor(감가율, γ)**: 미래 보상에 대한 현재 가치 비중을 결정한다.
> - **Loss type(손실 함수 유형)**: Huber 손실 함수를 사용하여 급격한 오차 변화에 탄력적으로 대응한다.
> - **Learning rate(학습률)**: 네트워크 가중치 업데이트 시 적용되는 학습 속도를 의미한다.
> - **Number of experience episodes between each policy update(정책 업데이트 간 경험 에피소드 수)**: 정책을 갱신하기 전까지 누적되는 에피소드 수
> - **Number of epochs(에폭 수)**: 한 번의 정책 업데이트에서 동일 데이터로 학습하는 반복 횟수


### 실행 결과 (Results)
3랩 시뮬레이션 평가 결과는 다음과 같다.
| Trial | Time (MM:SS.mmm) | Trial results (% track completed) | Status       | Off-track | Off-track penalty | Crashes |
|:-----:|:----------------:|:---------------------------------:|:-------------:|:---------:|:-----------------:|:-------:|
|   1   |     00:12.888    |               100%                | Lap complete |     0     |        --         |    0    |
|   2   |     00:12.629    |               100%                | Lap complete |     0     |        --         |    0    |
|   3   |     00:12.858    |               100%                | Lap complete |     0     |        --         |    0    |

---
### 성과 (Achievement)
- 2025 경기대학교 **AWS DeepRacer League 준우승(2위)**