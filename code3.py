import cv2
import numpy as np

# Function to apply a simple enhancement (Adaptive Gamma Correction)
def apply_image_enhancement(image):
    # Adaptive Gamma Correction
    gamma = 1.5
    look_up_table = np.array([((i / 255.0) ** (1.0 / gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")
    corrected_image = cv2.LUT(image, look_up_table)
    return corrected_image

# Main function to process the image
def main():
    # Load the image
    image_path = 'OIP.jpg'
    original_image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if original_image is None:
        print("Could not read the image. Please check the file path.")
        return

    # Apply image enhancement
    enhanced_image = apply_image_enhancement(original_image)

    # Display the original and enhanced images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Enhanced Image', enhanced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Execute the main function
if __name__ == "__main__":
    main()
