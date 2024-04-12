def Intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


if __name__ == "__main__":
    lst1 = [1, 3, 24, 78, 35, 55]
    lst2 = [12, 24, 35, 24, 88, 120, 155]
    print(Intersection(lst1, lst2))
