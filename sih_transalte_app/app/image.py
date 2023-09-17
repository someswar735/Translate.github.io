from PIL import Image, ImageDraw, ImageFont

# Load the original image
original_image = Image.open('1.png')

# Create a drawing context
draw = ImageDraw.Draw(original_image)

# Define text and style parameters
translated_text = "murali"
font = ImageFont.load_default()
font_size = 100
text_color = (255, 255, 255)  # White

# Define the position for text overlay
position = (100, 100)

# Overlay the translated text onto the image
draw.text(position, translated_text, font=font, fill=text_color)

# Save the result
original_image.save('2.png')

# For PDFs, you would use a similar approach with PyPDF2 or a PDF library.
