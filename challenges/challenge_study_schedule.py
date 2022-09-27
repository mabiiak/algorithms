def study_schedule(permanence_period, target_time):
    count = 0

    if not target_time:
        return None

    for entrance, exit in permanence_period:
        if type(entrance) is not int or type(exit) is not int:
            return None
        
        if entrance <= target_time <= exit:
            count += 1

    return count
        
