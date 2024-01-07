import cv2
import numpy as np

class UndergroundSafetySystem:
    def __init__(self):
        # Initialize sensors, processing modules, and variables
        pass

    def acquire_thermal_data(self):
        # Simulate acquiring thermal data from the camera (replace with actual implementation)
        return cv2.imread('OIP.jpg', cv2.IMREAD_GRAYSCALE)

    def preprocess_thermal_data(self, thermal_data):
        # Preprocessing steps for thermal data (if needed)
        return thermal_data

    def enhance_thermal_image(self, thermal_image):
        # Check if the image is not in the correct format for equalization
        if thermal_image.dtype != np.uint8:
            thermal_image = thermal_image.astype(np.uint8)

        # Apply histogram equalization to the thermal image
        enhanced_image = cv2.equalizeHist(thermal_image)

        return enhanced_image

    def visualize_data(self, original_image, enhanced_image):
        # Display the original, enhanced, and side-by-side images
        combined_image = np.hstack((original_image, enhanced_image))
        cv2.imshow('Original vs Enhanced Thermal Image', combined_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        # Main loop for real-time data processing and visualization
        original_thermal_data = self.acquire_thermal_data()
        preprocessed_thermal = self.preprocess_thermal_data(original_thermal_data)
        enhanced_thermal = self.enhance_thermal_image(preprocessed_thermal)
        self.visualize_data(original_thermal_data, enhanced_thermal)
        # Implement additional functionalities for system control, error handling, etc.

if __name__ == "__main__":
    # Initialize the Underground Safety System
    safety_system = UndergroundSafetySystem()

    # Run the safety system
    safety_system.run()
