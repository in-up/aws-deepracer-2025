import math

def reward_function(params):
    all_on         = params['all_wheels_on_track']
    steering_abs   = abs(params['steering_angle'])
    speed          = params['speed']
    progress       = params['progress']
    steps          = params['steps']
    track_width    = params['track_width']
    dist_center    = params['distance_from_center']
    waypoints      = params['waypoints']
    closest_idx    = params['closest_waypoints']
    heading        = params['heading']

    # 트랙 이탈 즉시 감점
    if not all_on:
        return 1e-3
    # 기본 보상
    reward = 1.0

    # 중앙선과의 거리 측정
    markers = [0.10 * track_width, 0.25 * track_width, 0.50 * track_width]
    if   dist_center <= markers[0]:
        reward += 1.0
    elif dist_center <= markers[1]:
        reward += 0.5
    elif dist_center <= markers[2]:
        reward += 0.1
    else:
        reward *= 0.5

    # 예상 방향성과 현재 방향성 차이 비교
    next_wp  = waypoints[closest_idx[1]]
    prev_wp  = waypoints[closest_idx[0]]
    track_dir = math.degrees(math.atan2(next_wp[1]-prev_wp[1],
                                        next_wp[0]-prev_wp[0]))
    diff = abs(track_dir - heading)
    if diff > 180:
        diff = 360 - diff
    if diff < 10:
        reward += 1.0
    elif diff < 20:
        reward += 0.5
    else:
        reward *= 0.5

    # 속도 및 조향 분석
    STRAIGHT_TH = 5.0

    STRAIGHT_FAST = 2.0   # 2.0 - 2.2
    STRAIGHT_MID  = 1.5
    STRAIGHT_SLOW = 1.0

    CORNER_MAX    = 1.7
    CORNER_MID    = 1.0

    if steering_abs < STRAIGHT_TH:           # 직선
        if speed >= STRAIGHT_FAST:
            reward += 1.2
        elif speed >= STRAIGHT_MID:
            reward += 0.8
        elif speed >= STRAIGHT_SLOW:
            reward += 0.3
        else:
            reward *= 0.7                    # 느린 직선
    else:                                    # 코너
        if CORNER_MID <= speed <= CORNER_MAX:
            reward += 0.7
        elif speed < CORNER_MID:
            reward += 0.3
        else:
            reward *= 0.6                    # 코너 과속

    # 진행률 및 완주
    if steps > 0 and steps % 50 == 0:
        reward += progress * 0.02

    if progress >= 99.5:                     # 완주 시 보상 보너스
        reward += 30.0

    return float(max(reward, 1e-3))


