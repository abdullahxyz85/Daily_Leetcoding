class ProductOfNumbers:
    def __init__(self):
        self.prefixProduct = [1]  # Initialize with 1 to handle division

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProduct = [1]  # Reset when encountering zero
        else:
            self.prefixProduct.append(self.prefixProduct[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefixProduct):  
            return 0  # If k exceeds range, zero was encountered
        return self.prefixProduct[-1] // self.prefixProduct[-k - 1]
