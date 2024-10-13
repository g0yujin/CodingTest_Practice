def solution(nums):
    pocketmon = set(nums)
    
    if len(pocketmon) <= len(nums)//2:
        return len(pocketmon)
    else:
        return len(nums)//2