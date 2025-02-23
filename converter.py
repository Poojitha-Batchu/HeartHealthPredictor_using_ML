from PIL import Image

# Open an image
img = Image.open('static/heart.png')  # Replace with your image path

# Convert and save as ICO
img.save("static/favicon.ico", format="ICO", sizes=[(10, 10)])  # You can change size
