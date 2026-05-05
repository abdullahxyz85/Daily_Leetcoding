class Solution:
    def fizzBuzz(self, n: int):
        answer = []

        for i in range(1, n + 1):

            # Divisible by both 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")

            # Divisible by 3
            elif i % 3 == 0:
                answer.append("Fizz")

            # Divisible by 5
            elif i % 5 == 0:
                answer.append("Buzz")

            # Not divisible by 3 or 5
            else:
                answer.append(str(i))

        return answer