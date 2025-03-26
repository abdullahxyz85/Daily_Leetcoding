class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        str_num = ""

        for num in nums:
            str_num += str(num)

        for i in str_num:
            answer.append(int(i))
        return answer