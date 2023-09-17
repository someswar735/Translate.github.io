import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def singleImg_pdf():
    image_1 = Image.open(r'./assets/cipam1.jpg')
    im_1 = image_1.convert('RGB')
    im_1.save(r'C:\Users\PRINC\sih_transalte_app\app\assets\img2pdf.pdf')

singleImg_pdf()
#-----------------------------------------------------------
#another model

def convert_image_to_pdf(image_path, pdf_path):
    # Open the image using Pillow
    img = Image.open(image_path)
    
    # Create the full path to the PDF file in the specified directory
    output_directory = r"C:\Users\PRINC\sih_transalte_app\app\assets"
    pdf_file_name = pdf_path
    pdf_path = os.path.join(output_directory, pdf_file_name)
    
    # Create a PDF file
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # Draw the image on the PDF
    c.drawImage(image_path, 0, 0, width, height)
    
    # Save the PDF
    c.save()

if __name__ == "__main__":
    image_path = "./assets/cipam1.jpg"  # Replace with the path to your input image
    pdf_path = "another_model.pdf"  # Replace with the desired output PDF file name
    
    convert_image_to_pdf(image_path, pdf_path)
#---------------------------------------------------------------
 #another multiple images model   
def convert_images_to_pdf(image_paths, output_directory, pdf_file_name):
    # Create the full path to the output PDF file
    pdf_path = os.path.join(output_directory, pdf_file_name)
    
    # Create a PDF file
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    for image_path in image_paths:
        # Open the image using Pillow
        img = Image.open(image_path)
        
        # Calculate the aspect ratio to fit the image within the PDF page
        aspect_ratio = img.width / img.height
        new_width = width
        new_height = int(width / aspect_ratio)
        
        # Add a page to the PDF
        c.setPageSize((new_width, new_height))
        c.showPage()
        
        # Draw the image on the PDF page
        c.drawImage(image_path, 0, 0, new_width, new_height)
    
    # Save the PDF
    c.save()

if __name__ == "__main__":
    image_paths = ["./assets/cipam1.jpg", "./assets/cipam2.jpg", "./assets/cipam3.jpg", "./assets/cipam4.jpg", "./assets/cipam5.jpg", "./assets/cipam6.png", "./assets/cipam7.png", "./assets/cipam8.jpg"]  # Replace with the paths to your input images
    output_directory = r"C:\Users\PRINC\sih_transalte_app\app\assets"
    pdf_file_name = "another_model_multiple.pdf"
    
    convert_images_to_pdf(image_paths, output_directory, pdf_file_name)
#---------------------------------------------------
#for multiple images
def multipleImg_pdf():
    image_1 = Image.open(r'./assets/cipam1.jpg')
    image_2 = Image.open(r'./assets/cipam2.jpg')
    image_3 = Image.open(r'./assets/cipam3.jpg')
    image_4 = Image.open(r'./assets/cipam4.jpg')

    im_1 = image_1.convert('RGB')
    im_2 = image_2.convert('RGB')
    im_3 = image_3.convert('RGB')
    im_4 = image_4.convert('RGB')

    image_list = [im_2, im_3, im_4]

    im_1.save(r'C:\Users\PRINC\sih_transalte_app\app\assets\image2pdf_multiple.pdf', save_all=True, append_images=image_list)

multipleImg_pdf()