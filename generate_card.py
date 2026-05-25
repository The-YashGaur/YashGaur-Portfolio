from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

# Create 1024x1024 black canvas
canvas = Image.new('RGB', (1024, 1024), (0, 0, 0))
draw = ImageDraw.Draw(canvas)

# 1. Add Person Image
try:
    person_img = Image.open('src/assets/images/IMG_4373.JPG')
    # Convert to grayscale/monochrome
    person_img = person_img.convert('L').convert('RGB')
    
    # Scale person to fit left side (around 512x768)
    # The original is a portrait
    aspect = person_img.width / person_img.height
    new_h = 768
    new_w = int(new_h * aspect)
    person_img = person_img.resize((new_w, new_h), Image.LANCZOS)
    
    # Add a cyan tint
    tint = Image.new('RGB', person_img.size, (0, 255, 220))
    person_img = Image.blend(person_img, tint, 0.2)
    
    # Paste on left side
    x_offset = (512 - new_w) // 2
    if x_offset < 0: x_offset = 0
    canvas.paste(person_img, (x_offset, 0))
except Exception as e:
    print("Error with person image:", e)

# 2. Draw vertical "YASH" text in center
try:
    # Try to use a default font if custom is missing
    font = ImageFont.load_default()
    # We will just draw a white rectangle as fallback if we can't get big font, 
    # but let's try to scale default font or draw manually.
    # Better: use ImageFont.truetype with a system font
    font_path = "/System/Library/Fonts/Helvetica.ttc"
    font = ImageFont.truetype(font_path, 120)
    
    y_pos = 50
    for char in "YASH":
        draw.text((420, y_pos), char, font=font, fill=(255, 255, 255))
        y_pos += 120
except Exception as e:
    print("Font error:", e)

# 3. Draw Badge at x=50, y=550 (bottom of the visible 75%)
# White rounded rectangle
draw.rounded_rectangle([30, 500, 400, 680], radius=20, fill=(255, 255, 255))
# Black pill inside
draw.rounded_rectangle([50, 600, 380, 650], radius=25, fill=(0, 0, 0))

try:
    font_bold = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    font_small = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    draw.text((60, 530), "YASH GAUR", font=font_bold, fill=(0, 0, 0))
    draw.text((90, 615), "FRONT END DEVELOPER", font=font_small, fill=(255, 255, 255))
except:
    pass

# 4. Draw YG logo on right side
try:
    font_logo = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
    draw.text((650, 350), "YG", font=font_logo, fill=(0, 255, 220))
    font_logo_text = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
    draw.text((780, 360), "Yash Gaur", font=font_logo_text, fill=(255, 255, 255))
    draw.text((780, 400), "Creative", font=font_logo_text, fill=(255, 255, 255))
except:
    pass

# Save the final image
canvas.save('src/assets/Lanyard/card lanyard.png')
canvas.save('public/models/card-texture.png')
print("Image generated successfully!")
