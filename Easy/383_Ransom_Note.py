class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ran = {}
        freq_mag = {}

        for let in ransomNote:
            if let in freq_ran:
                freq_ran[let] += 1
            else:
                freq_ran[let] = 1

        for let in magazine:
            if let in freq_mag:
                freq_mag[let] += 1
            else:
                freq_mag[let] = 1

        for key, value in freq_ran.items():
            if key in freq_mag:
                if freq_mag[key] >= value:
                    continue
                else:
                    return False
            else:
                return False

        return True
