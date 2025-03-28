
from PIL import Image, ImageDraw, ImageFont

# Load the uploaded image
img = Image.open("images/picinpic.jpg")
draw = ImageDraw.Draw(img)

# Define text properties
text = "Hello, World!"
font = ImageFont.truetype("arial.ttf", 50)  # Adjust font size as needed
text_color = (255, 0, 0)  # Red for visibility
x, y = 50, 50  # Position on the image

# Draw text on the image
draw.text((x, y), text, font=font, fill=text_color)

# Show the image
img.show()

# Save the modified image
img.save("images/picinpic.jpg")