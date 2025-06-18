class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = {}
        for ch in chars:
            if ch in chars_dict:
                chars_dict[ch] += 1
            else:
                chars_dict[ch] = 1

        total_length = 0

        for word in words:
            word_dict = {}
            for ch in word:
                if ch in word_dict:
                    word_dict[ch] += 1
                else:
                    word_dict[ch] = 1

            can_make = True
            for ch in word:
                if ch not in chars_dict or word_dict[ch] > chars_dict[ch]:
                    can_make = False
                    break

            if can_make:
                total_length += len(word)

        return total_length
