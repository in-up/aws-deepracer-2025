import math


def reward_function(params):
    MAX_SPEED = 3.0
    LOWEST_REWARD = 1e-3

    # 트랙 이탈 시 즉시 패널티 반환
    if params["is_offtrack"] or not params["all_wheels_on_track"]:
        return LOWEST_REWARD

    # 기본 파라미터 정보
    track_w = params["track_width"]
    dist = params["distance_from_center"]
    steer = abs(params["steering_angle"])
    speed = params["speed"]
    progress = params["progress"]  # (0 - 100)
    steps = max(params["steps"], 1)

    # 중앙선 거리 비교
    max_dist = track_w * 0.5
    distance_factor = max(1e-3, 1 - (dist / max_dist) ** 2)  # (0 - 1)

    # 조향 및 속도 상호작용
    speed_norm = speed / MAX_SPEED  # (0 - 1)

    if steer < 5:           # Case 1 : 직선 구간
        speed_factor = speed_norm
    elif steer < 15:        # Case 2 : 곡선 구간
        speed_factor = speed_norm * 0.5
    else:                   # Case 3 : 유턴 구간
        speed_factor = speed_norm * 0.2

    # 진행률에 따른 목표 속도 보정 (waypoints 기반 계산, 수정 필요할 수도 있음)
    if 15 <= progress < 30:
        target_v = 1.2
    elif 52 <= progress < 75:
        target_v = 1.5
    else:
        target_v = 2.0

    # 목표 속도와 실제 속도 차이 기반 보상 적용
    speed_target_factor = math.exp(-((speed - target_v) ** 2) / (2 * 0.4 ** 2))

    # 진행도 대비
    progress_efficiency = (progress / steps) * 100

    # 보상값 계산
    reward = LOWEST_REWARD
    reward += 2.0 * distance_factor
    reward += 3.0 * speed_factor * speed_target_factor
    reward += 4.0 * progress_efficiency

    return float(reward)
