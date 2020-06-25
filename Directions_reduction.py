def dirReduc(arr):
    opposites = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }

    i = 0
    while i < len(arr)-1:
        if arr[i] == opposites[arr[i+1]]:
            print(arr[i], arr[i+1])
            del arr[i+1], arr[i]
            i -= 1
        else:
            i += 1
        if i < 0: i = 0
    return arr

