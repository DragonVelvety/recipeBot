import os
from docx2pdf import convert

def convert_docx_to_pdf(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            docx_file = os.path.join(directory, filename)
            pdf_file = os.path.join(directory, filename[:-5] + ".pdf")
            convert(docx_file, pdf_file)

convert_docx_to_pdf("D:\\Documents\\recipeBot\\Recipes")
