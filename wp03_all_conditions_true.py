

def are_all_conditions_true(conditions):
    if not conditions:
        return None
    return all(conditions)

print(are_all_conditions_true([]))