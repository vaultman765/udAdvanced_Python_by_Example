from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Enter the bill amount: "))
period = input("Enter the bill period (ex: June_2021): ")

name1 = input("Enter your name: ")
days_in_house1 = int(input(f"Enter the number of days {name1} stayed in house: "))

name2 = input("Enter flatmate's name: ")
days_in_house2 = int(input(f"Enter the number of days {name2} stayed in house: "))


bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} Pays: ", flatmate1.pays(bill, flatmate2))
print(f"{name2} Pays: ", flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill=bill)
