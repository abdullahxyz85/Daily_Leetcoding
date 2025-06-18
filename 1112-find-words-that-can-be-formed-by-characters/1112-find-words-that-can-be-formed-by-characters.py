class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Step 1: Create a dictionary to count characters in chars
        chars_dict = {}
        for ch in chars:
            if ch in chars_dict:
                chars_dict[ch] += 1
            else:
                chars_dict[ch] = 1

        total_length = 0

        # Step 2: Go through each word in the list
        for word in words:
            word_dict = {}
            for ch in word:
                if ch in word_dict:
                    word_dict[ch] += 1
                else:
                    word_dict[ch] = 1

            # Step 3: Check if the word can be made using chars
            can_make = True
            for ch in word:
                if ch not in chars_dict or word_dict[ch] > chars_dict[ch]:
                    can_make = False
                    break

            # Step 4: If word can be formed, add its length
            if can_make:
                total_length += len(word)

        return total_length
