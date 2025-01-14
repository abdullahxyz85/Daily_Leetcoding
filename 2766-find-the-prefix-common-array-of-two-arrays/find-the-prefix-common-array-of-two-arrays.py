class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = []  # To store the prefix common array
        seen_A = set()  # To keep track of elements seen in A
        seen_B = set()  # To keep track of elements seen in B

        for i in range(n):
            seen_A.add(A[i])
            seen_B.add(B[i])

            # Count the common elements between seen_A and seen_B
            common_count = len(seen_A.intersection(seen_B))
            C.append(common_count)

        return C