def removeDuplicate(lists):
    newlist = []
    seen = set()

    for item in lists:
        # print(item)
        if item not in seen:
            seen.add(item)
            newlist.append(item)

    return newlist


li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(removeDuplicate(li))
