import cv2
import os
import sys
import numpy as np 

def sketch_image(image_path):
    """
    This function takes an image path, converts it to a lower-fidelity sketch, 
    and saves it in a fixed "output" directory, preserving the original file extension.

    Args:
        image_path (str): Path to the input image file.
    """

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce details with adaptive thresholding 
    adaptive_thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)


    # Randomly colorize some pixels
    num_pixels_to_colorize = int(0.4 * adaptive_thresh.size)  # Colorize 40% of pixels
    random_indices = np.random.choice(adaptive_thresh.size, num_pixels_to_colorize, replace=False)
    adaptive_thresh.reshape(-1)[random_indices] = np.random.randint(0, 256, size=num_pixels_to_colorize)


    # Extract filename and extension
    filename, file_extension = os.path.splitext(os.path.basename(image_path))

    # Create the "output" directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Create the output filepath in the "output" directory
    output_path = os.path.join(output_dir, filename + file_extension)

    # Save the sketch image
    cv2.imwrite(output_path, adaptive_thresh)

    print(f"Sketch image saved to: {output_path}")


# Get image paths from command line arguments
if len(sys.argv) > 1:
    image_paths = sys.argv[1:]  # Get all arguments after the script name
else:
    print("Please provide image paths as arguments.")
    sys.exit(1)

# Process each image
for image_path in image_paths:
    sketch_image(image_path) 
