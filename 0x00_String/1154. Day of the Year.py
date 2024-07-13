class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # function to ckeck leap year
        def is_leap_year(year):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

        if is_leap_year(year):
            days_in_month[1] = 29
            
        days = sum(days_in_month[:month - 1]) + day
        return days