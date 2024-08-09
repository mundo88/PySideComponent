class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)
print(dateWithDash)