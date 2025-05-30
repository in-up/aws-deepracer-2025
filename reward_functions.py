## https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-examples.html

def reward_function(params):

    if params["all_wheels_on_track"] and params["steps"] > 0:
        reward = ((params["progress"] / params["steps"]) * 100) + (params["speed"]**2)
    else:
        reward = 0.01
        
    return float(reward)
