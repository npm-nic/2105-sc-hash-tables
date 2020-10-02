def get_indices_of_item_weights(weights, length, limit):
    lookup = {}
    for index, value in enumerate(weights):
        diff = limit - value
        if diff in lookup:
            return (index, lookup[diff])
        else:
            lookup[value] = index
    return None

    # # ⬇️ SEE WHAT IS HAPPENING USING PRINT STATEMENTS ⬇️
    # lookup = {}
    # print(f'-----> w: {weights}, len: {length}, limit: {limit} <-----')
    # for index, value in enumerate(weights):
    #     print(f'-- lookup: {lookup} --')
    #     print(f'limit: {limit}, i: {index}, v: {value}')
    #     diff = limit - value
    #     print(f'diff = limit ({limit}) - value ({value}) = {diff}')
    #     if diff in lookup:
    #         print(f'diff ({diff}) found in lookup:')
    #         print(f'--> returned: ({index},{lookup[diff]})')
    #         return (index, lookup[diff])
    #     else:
    #         print(f'diff ({diff}) NOT found in lookup:')
    #         lookup[value] = index
    #         print(f'new lookup: {lookup}')

    # print(f'--> returned: None')
    # return None



''' How/Why did we do it this way? '''
# If we store each weight's list index as its value,
# --> we can then check to see if the hash table contains an entry for limit - weight.
# If it does
# --> then we've found the two items whose weights sum up to the limit!
# If it does not:
# --> add value and index to lookup table and keep looping