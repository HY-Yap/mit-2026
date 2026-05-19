#Helper functions to calculate and return results for workout targets

def arith_seq(start, target, common_diff): # return a list of tuples in the form (week, target)
    current = start
    result = []
    week = 1
    while current < target:
        current = start + (week-1) * common_diff #AP formula for nth term
        result.append((week, current))
        week += 1
    result[-1] = (week-1, target)
    return result

print(arith_seq(1, 11, 3))