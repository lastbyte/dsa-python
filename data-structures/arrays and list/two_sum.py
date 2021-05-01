
def get_key(obj):
    return obj["val"]

def two_sum(arr, target):
    num_pos = []
    for idx, val in enumerate(arr):
        num_pos.append({"val" : val, "idx" : idx})

    num_pos.sort(key=get_key)

    left,right = 0, len(arr)-1

    while left < right  and left < len(arr) and right >= 0:
        if num_pos[left]["val"] + num_pos[right]["val"] == target :
            return [num_pos[left]["idx"], num_pos[right]["idx"]]
            left += 1
        elif num_pos[left]["val"] + num_pos[right]["val"] < target:
            left += 1
        else :
            right -= 1
    return sums

print(two_sum([2,7,11,15], 9))
print(two_sum([3,3], 6))