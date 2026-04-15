import os
import cv2
import numpy as np
from torch.utils.data import Dataset

class UnderwaterImageDataset(Dataset):
    """
    A custom dataset for loading underwater images.
    """

    def __init__(self, image_dir, transform=None):
        """
        Args:
            image_dir (str): Directory with all the images.
            transform (callable, optional): Optional transform to be applied on an image.
        """
        self.image_dir = image_dir
        self.image_files = os.listdir(image_dir)
        self.transform = transform

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_name = os.path.join(self.image_dir, self.image_files[idx])
        image = cv2.imread(img_name)
        if self.transform:
            image = self.transform(image)
        return image


class DatasetBuilder:
    """
    A class for building the dataset and loading images with preprocessing steps.
    """
    
    def __init__(self, dataset: UnderwaterImageDataset):
        self.dataset = dataset

    def load_images(self):
        """ Load and preprocess the images """
        images = []
        for img in self.dataset:
            images.append(img)
        return np.array(images)