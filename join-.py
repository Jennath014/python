def join_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + "-" + join_recursive(lst[1:])

print(join_recursive(["a", "b", "c"]))
