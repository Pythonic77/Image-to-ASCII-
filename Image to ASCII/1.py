from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize image while keeping aspect ratio
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # Adjust height to look correct in text
    return image.resize((new_width, new_height))

# Convert image to grayscale
def grayify(image):
    return image.convert("L")

# Convert pixels to ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

# Main function
def image_to_ascii(path, width=100):
    try:
        image = Image.open(path)
    except:
        print("Failed to open image.")
        return

    image = resize_image(image, width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    img_width = image.width
    ascii_img = "\n".join([ascii_str[i:i + img_width] for i in range(0, len(ascii_str), img_width)])

    print(ascii_img)

    # Optional: Save to file
    with open("ascii_output.txt", "w") as f:
        f.write(ascii_img)

# Example usage
path = input("Enter image path (e.g., test.jpg): ")
image_to_ascii(path)
