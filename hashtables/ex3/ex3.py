def intersection(arrays):
    # # This is was my first pass ⬇️
    # dictionary = {}
    # result = []

    # for array in arrays:
    #     for num in array:
    #         if num not in dictionary:
    #             dictionary[num] = 1
    #         else:
    #             dictionary[num] += 1

    # for key in dictionary:
    #     if dictionary[key] == len(arrays):
    #         result.append(key)

    # return result

    # # Much Better ⬇️
    base_cache = {}

    # get shortest
    shortest = []
    if len(arrays) > 0:
        shortest = arrays[0]
    for _, v in enumerate(arrays):
        if len(v) < len(shortest):
            shortest = v

    # populate base cache, based on the shortest number list
    for num in shortest:
        base_cache[num] = None

    # find repeating numbers
    for _, v in enumerate(arrays):
        if v is not shortest:
            new_cache = {}
            for num in v:
                if num in base_cache:
                    new_cache[num] = None
            
            base_cache = new_cache
            
    result = list(base_cache.keys())

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(100, 200)) + [1, 2, 3])
    arrays.append(list(range(200, 300)) + [1, 2, 3])
    arrays.append(list(range(300, 4000)) + [1, 2, 3])

    print(intersection(arrays))
