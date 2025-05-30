import math

def reward_function(params):
    MAX_SPEED      = 3.0
    MIN_SPEED      = 0.5
    LOWEST_REWARD  = 1e-3

    # 트랙 이탈 즉시 패널티
    if params["is_offtrack"] or not params["all_wheels_on_track"]:
        return LOWEST_REWARD

    # 파라미터
    track_w  = params["track_width"]
    dist     = params["distance_from_center"]
    steer    = abs(params["steering_angle"])
    speed    = params["speed"]
    progress = params["progress"]
    steps    = max(params["steps"], 1)

    # 중앙선 대비 거리 보상
    max_dist = 0.5 * track_w
    distance_factor = max(1e-3, 1 - (dist / max_dist) ** 2)

    # 조향 및 속도 상호작용
    speed_norm = max(0.0, (speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED))  # (0 - 1)

    if steer < 5:          # 직선
        speed_factor = speed_norm
    elif steer < 15:       # 곡선
        speed_factor = speed_norm * 0.5
    else:                  # 유턴
        speed_factor = speed_norm * 0.2

    # 구간별 목표 속도 (progress 기반)
    if 15 <= progress < 30:
        target_v = 1.2
    elif 52 <= progress < 75:
        target_v = 1.5
    else:
        target_v = 2.0

    speed_target_factor = math.exp(-((speed - target_v) ** 2) / (2 * 0.4 ** 2))

    # 진행도 대비 보상
    progress_eff = (progress / steps) / 1.0           # (0 - 1)
    progress_eff = min(progress_eff, 1.0)              # 상한 클리핑

    # 최종 보상
    reward  = LOWEST_REWARD
    reward += 2.0 * distance_factor
    reward += 3.0 * speed_factor * speed_target_factor
    reward += 4.0 * progress_eff

    return float(reward)
