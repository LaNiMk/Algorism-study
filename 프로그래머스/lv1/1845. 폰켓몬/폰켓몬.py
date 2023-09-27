def solution(nums):
    num = set(nums)
    if len(num) <= len(nums)/2 :
        return len(num)
    else :
        return len(nums)/2