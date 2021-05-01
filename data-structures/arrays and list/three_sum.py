def three_sum( nums : []) -> [] :
    ret_list = []
    nums.sort()
    for i in range(0,len(nums) -2 ):
        left,right = i+1 , len(nums)-1
        while left < right :
            if nums[i] + nums[left] + nums[right] < 0 :
                left = left + 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right = right - 1
            elif nums[i] + nums[left] + nums[right] == 0 :
                if not ret_list.__contains__([nums[i], nums[left], nums[right]]) :
                    ret_list.append([nums[i], nums[left], nums[right]])
                left = left + 1

    return ret_list


print(three_sum([-1,0,1,2,-1,-4]))