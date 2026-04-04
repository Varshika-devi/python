from PIL import Image

def resize_image(input_path, output_path, size):
    img = Image.open(input_path)
    img = img.resize(size)
    img.save(output_path)
    print("Image resized!")

if __name__ == "__main__":
    resize_image("input.jpg", "output.jpg", (300, 300))
