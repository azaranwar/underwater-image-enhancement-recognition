import cv2
import os
import numpy as np

class BatchEnhancer:
    def __init__(self, enhancer):
        # Initialize with an image enhancer object.
        self.enhancer = enhancer

    def enhance_image(self, image_path):
        # Enhance a single image and save it.
        image = cv2.imread(image_path)
        enhanced_image = self.enhancer.enhance(image)
        enhanced_image_path = image_path.replace('.jpg', '_enhanced.jpg').replace('.png', '_enhanced.png')
        cv2.imwrite(enhanced_image_path, enhanced_image)
        return enhanced_image_path

    def enhance_directory(self, dir_path):
        # Enhance all images in a directory.
        enhanced_images = []
        for filename in os.listdir(dir_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(dir_path, filename)
                enhanced_image_path = self.enhance_image(image_path)
                enhanced_images.append(enhanced_image_path)
        return enhanced_images
