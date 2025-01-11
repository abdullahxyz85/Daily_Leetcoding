class Solution:
    def dayOfYear(self, date: str) -> int:
       
        # Extract year, month, and day from the date string
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        
        # Days in each month for a non-leap year
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29  # Adjust February days for a leap year
        
        # Calculate the day number of the year
        day_of_year = 0
        for i in range(month - 1):
            day_of_year += days_in_month[i]
        day_of_year += day
        
        return day_of_year
