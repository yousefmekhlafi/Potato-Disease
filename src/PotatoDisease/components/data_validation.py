import os
from PIL import Image


class ImageDataValidator:
    def __init__(self, config):
        self.image_dir = config.image_dir
        self.labels = config.labels
        self.batch_size = config.batch_size
        self.findings_output_file = config.findings_output_file
        self.findings = []

    def check_corrupted_images(self):
        corrupted_images = []
        for label in self.labels:
            label_dir = os.path.join(self.image_dir, label)
            image_files = os.listdir(label_dir)
            for i in range(0, len(image_files), self.batch_size):
                batch = image_files[i:i + self.batch_size]
                for image_file in batch:
                    image_path = os.path.join(label_dir, image_file)
                    try:
                        img = Image.open(image_path)
                        img.verify()
                    except (IOError, SyntaxError) as e:
                        corrupted_images.append(image_path)

        if corrupted_images:
            self.findings.append(f"Corrupted Images: {len(corrupted_images)} found.")
        else:
            self.findings.append("No corrupted images found.")

    def check_image_dimensions(self, target_size=(224, 224)):
        for label in self.labels:
            label_dir = os.path.join(self.image_dir, label)
            image_files = os.listdir(label_dir)
            for i in range(0, len(image_files), self.batch_size):
                batch = image_files[i:i + self.batch_size]
                for image_file in batch:
                    image_path = os.path.join(label_dir, image_file)
                    img = Image.open(image_path)
                    if img.size != target_size:
                        self.findings.append(f"Image {image_file} in class {label} has dimensions {img.size}, expected {target_size}.")

    def save_findings(self):
        with open(self.findings_output_file, 'w') as f:
            for finding in self.findings:
                f.write(finding + '\n')

    def validate(self):
        self.check_corrupted_images()
        self.check_image_dimensions()
        self.save_findings()