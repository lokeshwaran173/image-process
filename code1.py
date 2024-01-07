# Example of Adaptive Gamma Correction for image enhancement
import cv2
import numpy as np

def adaptive_gamma_correction(image):
    # Applying gamma correction to enhance the image
    gamma = 1.5  # You can adjust this value based on the requirement
    look_up_table = np.array([((i / 255.0) ** (1.0 / gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")
    corrected_image = cv2.LUT(image, look_up_table)
    return corrected_image

# Example usage
if __name__ == "__main__":
    # Load an example thermal image (replace 'thermal_image.jpg' with your image path)
    img_path = 'OIP.jpg'
    thermal_img = cv2.imread(img_path)

    # Apply Adaptive Gamma Correction
    enhanced_img = adaptive_gamma_correction(thermal_img)

    # Display original and enhanced images (OpenCV window)
    cv2.imshow('Original Image', thermal_img)
    cv2.imshow('Enhanced Image', enhanced_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
