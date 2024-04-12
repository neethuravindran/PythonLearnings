lists = [12, 24, 35, 70, 88, 120, 155]
lists = [x for (i, x) in enumerate(lists) if i not in (0, 4, 5)]
print(lists)
