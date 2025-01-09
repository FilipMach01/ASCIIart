# ASCII Art Generator

This Python script converts images to ASCII art using the Pillow library.

## Features

- Converts JPEG images to ASCII art
- Resizes the image to fit within specified dimensions
- Saves the resulting ASCII art to a text file (optional)

## Usage

1. Install required dependencies:
```
pip install Pillow
```

2. Place your image file named "111.jpg" in the same directory as the script.

3. Run the script:

```
python ascii_art_generator.py
```
4. The script will display the ASCII art in the console.

5. Optionally, enter a filename when prompted to save the ASCII art to a text file.

## Configuration

- The script uses a fixed image size of 100x40 pixels for the output.
- You can modify the `new_width` variable in the `convert_image_to_ascii` function to change the width of the ASCII art.
- The aspect ratio of the resized image is set to 0.4 times the original height.

## How It Works

1. The script opens the specified image file using Pillow.
2. It defines a function `get_ascii_character` that converts pixel values to ASCII characters based on grayscale intensity.
3. The `convert_image_to_ascii` function resizes the image and converts each pixel to its corresponding ASCII character.
4. The resulting ASCII art is printed to the console and optionally saved to a text file.

## Limitations

- This script only works with JPEG images named "111.jpg".
- The ASCII art output may not look great on all systems due to font limitations.
- Large images will result in very long ASCII art strings.




