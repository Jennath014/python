def nearly_equal(a, b):
    if abs(len(a) - len(b)) > 1:
        return False
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff += 1
    return diff <= 1

print(nearly_equal("cat", "cut"))
