# Time conversion functions for running

def time_to_seconds(minutes, seconds): #converts minutes and seconds into seconds
    result = seconds + minutes*60
    return result


def seconds_to_time(seconds): #converts seconds to minutes and seconds. Returns in the format "mm:ss"
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds}"




#SnS functions to calculate and return results for workout targets

#arithmetic progressions

def incr_arith_seq(start, target, common_diff): # return a list of targets, used for pushups and situps
    current = start
    result = []
    week = 1
    while current < target:
        current = start + (week-1) * common_diff #AP formula for nth term
        result.append(current)
        week += 1
    result[-1] = (target)
    return result


def decr_arith_seq(start, target, common_diff): # return a list of targets, used for running
    common_diff = -common_diff #assuming that the user inputs a positive value
    current = start
    result = []
    week = 1
    while current > target:
        current = start + (week-1) * common_diff #AP formula for nth term
        result.append(current)
        week += 1
    result[-1] = (target)
    return result



# geometric progressions

def incr_geo_seq(start, target, common_ratio): #return a list of targets, used for pushups and situps
    if start == 0:
        start = 1
    current = start
    result = []
    week = 1
    while current < target:
        current = start * (common_ratio ** (week - 1)) #GP formula for nth term
        result.append(int(current//1))
        week += 1
    result[-1] = (target)
    return result

def decr_geo_seq(start, target, common_ratio): #return a list of targets, used for running
    if start == 0:
        start = 1
    current = start
    result = []
    week = 1
    while current > target:
        current = start * (common_ratio ** (week - 1)) #GP formula for nth term
        result.append(int(current//1))
        week += 1
    result[-1] = (target)
    return result


#tests

# print(incr_arith_seq(2, 21, 5))
# print(decr_arith_seq(700, 502, 21))
# print(incr_geo_seq(0, 21, 1.2))
# print(decr_geo_seq(1002, 670, 0.9))