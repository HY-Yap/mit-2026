# planner.py

# -----------------------------
# Time conversion helpers
# -----------------------------

def time_to_seconds(minutes, seconds):
    """
    Convert minutes and seconds into total seconds.
    Example: 14 min 30 sec -> 870 seconds
    """
    result = seconds + minutes*60
    return result


def seconds_to_time(total_seconds):
    """
    Convert total seconds into a MM:SS string.
    Example: 870 -> '14:30'
    """
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes}:{seconds}"


# -----------------------------
# Sequence generation functions
# -----------------------------

def generate_arithmetic_sequence(start, target, weeks):
    """
    Generate an arithmetic sequence from start to target over a given number of weeks.
    Used for push-ups and sit-ups.
    """
    pass


def generate_decreasing_geometric_sequence(start, target, weeks):
    """
    Generate a decreasing geometric sequence from start to target over a given number of weeks.
    Used for 2.4 km run timing.
    """
    pass


# -----------------------------
# Realism / difficulty checks
# -----------------------------

def check_rep_progression(start, target, weeks):
    """
    Check whether the weekly increase for push-ups or sit-ups is realistic.
    Returns a warning or evaluation message.
    """
    pass


def check_running_progression(start_seconds, target_seconds, weeks):
    """
    Check whether the required weekly improvement for running is realistic.
    Returns a warning or evaluation message.
    """
    pass


# -----------------------------
# Main planner function
# -----------------------------

def generate_training_plan(
    current_pushups,
    target_pushups,
    current_situps,
    target_situps,
    current_run_seconds,
    target_run_seconds,
    weeks
):
    """
    Generate the full IPPT training plan.

    Returns:
    - weekly push-up targets
    - weekly sit-up targets
    - weekly 2.4 km timing targets
    - realism checks
    """
    pass
