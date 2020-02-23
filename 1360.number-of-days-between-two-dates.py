class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        count = 0
        early = date1 if date1 < date2 else date2
        last = date1 if date1 > date2 else date2
        datesOfMonth = [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        year1, month1, day1 = [int(i) for i in early.split("-")]
        year2, month2, day2 = [int(i) for i in last.split("-")]
        startYear = year1 if month1 <= 2 else year1 + 1
        endYear = year2 if month2 > 2 else year2 - 1
        year = startYear
        while year <= endYear:
            if self.isLeapYear(year):
                count += 1
            year += 1
        if day2 < day1:
            month2 -= 1
            day2 += datesOfMonth[month2 % 12]
        count += day2 - day1
        if month2 < month1:
            year2 -= 1
            month2 += 12
        for i in range(month1, month2):
            count += datesOfMonth[i % 12]
        return count + (year2 - year1) * 365

    def isLeapYear(self, year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == "__main__":
    s = Solution()
    print(s.daysBetweenDates("2084-05-19", "1976-02-26"))
