
## PPO / SAC 차이

1. **액션 공간(Action Space) 지원 범위**

   * **PPO**: 이산(Discrete)·연속(Continuous) 액션 공간 모두 지원 가능합니다.
   * **SAC**: 현재 AWS DeepRacer 콘솔에서는 **연속** 액션 공간만 지원합니다. ([Amazon Web Services, Inc.][1], [AWS 문서][2])

2. **학습 방식(On-policy vs Off-policy)**

   * **PPO (On-policy)**: 매 학습 반복마다 **현재(policy)로부터 수집된 데이터만** 사용하여 정책을 업데이트합니다. 이로 인해 안정적인 학습 결과를 얻는 대신, 더 많은 샘플(데이터)이 필요해 **샘플 비효율적**일 수 있습니다.
   * **SAC (Off-policy)**: 이전에 수집된 경험을 **재활용**할 수 있어 **샘플 효율성**이 뛰어나고, 빠른 학습 속도를 보입니다. 다만 학습 초기나 하이퍼파라미터 설정에 따라 PPO보다 **불안정**해질 수 있습니다. ([Amazon Web Services, Inc.][1])

3. **탐험(Exploration) 방식과 엔트로피(Entropy) 처리**

   * **PPO**: 정책이 너무 일찍 수렴하지 않도록 **엔트로피 정규화(entropy regularization)** 를 사용해 탐험을 장려합니다.
   * **SAC**: 최대 엔트로피(maximum entropy) 원칙을 적용하여, **보상의 기대값뿐 아니라 정책의 불확실성(엔트로피)을 동시에 최대화**하도록 설계되어 있어, 비유저널된 행동(unpromising behavior)은 자연스럽게 포기하며 더 효율적으로 탐험합니다.
   * SAC의 탐험 강도는 **alpha 하이퍼파라미터**로 조정 가능합니다 (0.0\~1.0 사이). ([AWS 문서][3])

4. **샘플 효율성 vs 안정성**

   * **PPO**: 안정적인 업데이트(Trust Region 기반의 클리핑 기법)를 통해 정책이 급격히 변하는 것을 막아 **일관된 성능**을 제공합니다. 다만, **더 많은 학습 에피소드**가 필요합니다.
   * **SAC**: off-policy 특성 덕분에 **적은 샘플로도** 빠르게 성능을 끌어올릴 수 있지만, 학습 중 정책이 크게 흔들리거나(variance) 하이퍼파라미터에 민감할 수 있습니다. ([Amazon Web Services, Inc.][1])

---

**요약하자면**,

* **빠른 수렴과 샘플 효율성**을 원하신다면, **연속 액션 공간**에서 **SAC**를 선택해 보세요.
* **높은 안정성**과 **이산/연속 액션 지원**이 필요하다면 **PPO**가 더 적합합니다.
* 궁극적으로는 **트랙 환경**, **컴퓨팅 리소스**, **허용 가능한 학습 시간**에 따라 두 알고리즘을 직접 실험해 보시는 것을 권장드립니다.

[1]: https://aws.amazon.com/blogs/machine-learning/using-the-aws-deepracer-new-soft-actor-critic-algorithm-with-continuous-action-spaces "Using the AWS DeepRacer new Soft Actor Critic algorithm with ..."
[2]: https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-get-started-training-model.html "Train your first AWS DeepRacer model"
[3]: https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-how-it-works-reinforcement-learning-algorithm.html "AWS DeepRacer training algorithms"