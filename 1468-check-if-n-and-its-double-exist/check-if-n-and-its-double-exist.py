# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         # for i in range(len(arr)):
        #     for j in range(len(arr)):  
        #         if i != j and (arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]): 
        #             return True
        # return False
        
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict={}

        for i in range (len(arr)):
            n=arr[i]
            if n*2 in dict or n/2 in dict:
                return True
            else:
                dict[n]=i
        return False
