class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = {}
        count = 0

        # Generate all pairs (a, b) and store their products
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  
                product = nums[i] * nums[j]
                
                # If the product already exists in the map, count valid tuples
                if product in product_map:
                    count += len(product_map[product]) * 8  # Each previous pair contributes 8 valid tuples
                    product_map[product].append((nums[i], nums[j]))
                else:
                    product_map[product] = [(nums[i], nums[j])]
        
        return count

