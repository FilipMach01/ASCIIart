from PIL import Image

def main():
    image = Image.open("111.jpg")
    new_width = 100

    # get_ascii_character
    def get_ascii_character(pixel):
        # Convert pixel values to grayscale
        gray_value = (pixel[0] + pixel[1] + pixel[2]) // 3

        # Define ASCII characters
        ascii_chars = "@#*%$&+-:. "

        # Get the ASCII character based on the grayscale value
        ascii_character = ascii_chars[gray_value // 25]

        return ascii_character

    # Convert the image to ASCII art
    def convert_image_to_ascii(image, new_width):
        ascii_image = ""
        image_width, image_height = image.size

        # Calculate the aspect ratio of the new image
        aspect_ratio = new_width / image_width

        # Resize the image to the new width and calculate the new height
        new_height = int(image_height * aspect_ratio * 0.4)

        # Resize the image
        resized_image = image.resize((new_width, new_height)).load()
        for y in range(new_height):
            for x in range(new_width):
                pixel = resized_image[x, y]
                ascii_image += get_ascii_character(pixel)
            ascii_image += "\n"
        return ascii_image



    #Convert the image to ASCII art
    ascii_image = convert_image_to_ascii(image, new_width)

    # Print result to console
    print("\nHere is your ASCII art:\n")
    print(ascii_image)

    # Optionally save the result to a text file
    output_file = input("Enter a filename to save the ASCII art (or press Enter to skip saving): ")
    if output_file:
        with open(output_file, 'w') as f:
            f.write(ascii_image)
        print(f"ASCII art saved to {output_file}")


if __name__ == '__main__':
    main()
