class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_altitude = 0
        highest_altitude = 0

        for i in range(len(gain)):
            current_altitude = current_altitude + gain[i]

            if current_altitude > highest_altitude:
                highest_altitude = current_altitude

        return highest_altitude