import os
from fpdf import FPDF

# Ask the user for the data of the document to be created and save it in a list to later create the pdf file
def complete_data():
    data_document = ["Names", "Surname", "Number_document", "Date_birth", "Address", "City", "Country", "Father_name/surname", 
                 "Mother_name/surname", "expirate_date"]  
    data_document_input = []
    for index in range(len(data_document)):
        data = input("Enter your " + data_document[index] + ": ")
        data_document_input.append(data_document[index] + ": " + data)
    
    return data_document_input

# Create a pdf file with the data entered by the user and open it with the default pdf viewer
def create_pdf(data_document_input):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=12)

    for index in range(len(data_document_input)):
        pdf.cell(200, 10, txt=data_document_input[index], ln=index, align="C")

    pdf.output("simple_demo.pdf")


# MAIN

data_document_input = complete_data()

create_pdf(data_document_input)

os.system("simple_demo.pdf")