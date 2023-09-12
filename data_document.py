
import os
from fpdf import FPDF

# Folder where the PDF file will be saved
data_document_save = "data_document_save"

# Check if the folder exists, if not, create it.
if not os.path.exists(data_document_save):
    os.makedirs(data_document_save)

# Ask the user for the data of the document to be created and save it in a list to later create the PDF file
def complete_data():

    data_document = ["Names", "Surname", "Number_document", "Date_birth", "Address", "City", "Country", "Father_name/surname", 
                    "Mother_name/surname", "expirate_date"]  
    data_document_input = {}

    for index in range(len(data_document)):
        data = input("Enter your " + data_document[index] + ": ")
        data_document_input[data_document[index]] = data
    
    return data_document_input

# Create a PDF file with the data entered by the user and save it in the specified folder
def create_pdf(data_document_input):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, value in data_document_input.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align="C")

    name_file = "data_document_" + data_document_input["Names"] + "_" + data_document_input["Surname"] + ".pdf"
    pdf_file_path = os.path.join(data_document_save, name_file)
    pdf.output(pdf_file_path)

    return pdf_file_path, name_file

# MAIN
data_document_input = complete_data()
pdf_file_path, name_file = create_pdf(data_document_input)

print(f"{name_file} saved to: {pdf_file_path}")

os.startfile(pdf_file_path)




