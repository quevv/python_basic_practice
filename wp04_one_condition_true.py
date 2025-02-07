
def is_a_condition_true(conditions):
    if not conditions:
        return None
    return any(conditions)

print(is_a_condition_true([False, False, True]))