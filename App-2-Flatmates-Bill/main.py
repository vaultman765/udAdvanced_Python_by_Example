import webbrowser
from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total
    amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lived in the flat and pays
    a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Created a Pdf file that contains data about the flatmates
    such as their names, due amount, and period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = "$"+str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = "$"+str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Image
        pdf.image("files/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount for flatmates
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)


amount = float(input("Enter the bill amount: "))
period = input("Enter the bill period (ex: June 2021): ")

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
