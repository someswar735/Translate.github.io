from formrecogniser import extract_text_from_document
from summarize import summarize_text
from translate import translate_text
from img2pdf import convert_image_to_pdf
from img2pdf import singleImg_pdf

import os
import fitz  # PyMuPDF
from pikepdf import Pdf

import PyPDF2
#----------------------------------------------------------------
#splitting
# Define the input PDF file and the output directory
input_filename = "test-2-split1.pdf"
output_directory = "output_pdfs"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Open the input PDF file
pdf_document = fitz.open(input_filename)

# Specify the page number to split (e.g., page 1)
page_number = 1

# Get the page you want to split
page_to_split = pdf_document[page_number - 1]  # Subtract 1 for 0-based indexing

# Get the dimensions of the page using the 'rect' attribute
page_rect = page_to_split.rect
page_width = page_rect.width
page_height = page_rect.height

# Calculate the height for each half (assuming a vertical split)
half_height = page_height / 2

# Calculate the coordinates for splitting the page
x1, y1, x2, y2 = page_rect

# Crop the top half of the page
top_half_rect = fitz.Rect(x1, y1, x2, y1 + half_height)
top_half_pixmap = page_to_split.get_pixmap(matrix=fitz.Matrix(1, 1), clip=top_half_rect)

# Crop the bottom half of the page
bottom_half_rect = fitz.Rect(x1, y1 + half_height, x2, y2)
bottom_half_pixmap = page_to_split.get_pixmap(matrix=fitz.Matrix(1, 1), clip=bottom_half_rect)

# Create two new PDF documents for the halves
new_document1 = fitz.open()
new_document2 = fitz.open()

# Create two new pages for the halves
new_page1 = new_document1.new_page(width=page_width, height=half_height)
new_page2 = new_document2.new_page(width=page_width, height=half_height)

# Insert the cropped top half into new_page1
new_page1.insert_image(top_half_rect, pixmap=top_half_pixmap)

# Insert the cropped bottom half into new_page2
new_page2.insert_image(bottom_half_rect, pixmap=bottom_half_pixmap)

# Save the new PDF documents with split pages
output_filename1 = os.path.join(output_directory, "output_page1.pdf")
output_filename2 = os.path.join(output_directory, "output_page2.pdf")

new_document1.save(output_filename1)
new_document2.save(output_filename2)

# Close the PDF documents
pdf_document.close()
new_document1.close()
new_document2.close()

print(f"[+] Split PDF pages saved to {output_filename1} and {output_filename2}")

#-------------------------------------------------------------------

if __name__ == "__main__":
    image_path = "./assets/cipam1.jpg"  # Replace with the path to your input image
    pdf_path = "multi_image.pdf"  # Replace with the desired output PDF file name
    
    convert_image_to_pdf(image_path, pdf_path)
    print("single image to pdf done", pdf_path)
#-------------------------------------------
#another
singleImg_pdf()
print("single image to pdf done")
#--------------------------------------------------------------------------------
input_file_path = "./img2pdf.pdf"
target_language = "te"
extracted_text = extract_text_from_document(
    input_file_path)
print("Extracted text:\n", extracted_text,'\n\n')
print("-----------------------------------\n\n")
summarized_text = summarize_text(extracted_text)
print("Summarized text:\n", summarized_text,'\n\n')
print("-----------------------------------\n\n")
translated_text = translate_text(summarized_text, target_language)
print("Translated text:\n", translated_text,'\n\n')
