import random
import cv2
import albumentations as A
import numpy as np
import os 

dir_list = os.listdir('images/')

for img in dir_list:

     path = "images/" + img
     image = cv2.imread(path)

     numero = random.randint(1,10)
     prob = 1
     if 6 > numero > 3:
          prob = 0.6
     elif numero >=6:
          prob = 0.3

     transform = A.SomeOf([
          A.HorizontalFlip(p=prob),
          A.CLAHE(p=prob),
          A.ChromaticAberration(
               primary_distortion_limit=0.05,
               secondary_distortion_limit=0.1,
               mode='green_purple',
               interpolation=cv2.INTER_LINEAR,
               p=prob
          ),
          A.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.05,p=prob),
          A.Downscale(
               scale_range=(0.5, 0.75),
               interpolation_pair={'downscale': cv2.INTER_NEAREST, 'upscale': cv2.INTER_LINEAR},
               p=prob
          ),
          A.Emboss(alpha=(0.2, 0.5), strength=(0.2, 0.7),p=prob),
          A.Equalize(p=prob),
          A.GaussNoise(p=prob),
          A.HueSaturationValue(
               hue_shift_limit=5,
               sat_shift_limit=30,
               val_shift_limit=20,
               p=prob
          ),
          A.ISONoise(color_shift=(0.01, 0.05), intensity=(0.1, 0.5),p=prob),
          A.ImageCompression(quality_range=(50, 90),p=prob),
          A.Morphological(scale=(2, 3), operation='dilation',p=prob),
          A.PlanckianJitter(
               mode="blackbody",
               sampling_method="gaussian",
               p=prob
          ),
          A.Posterize(num_bits=3,p=prob),
          A.RGBShift(
               r_shift_limit=10,  
               g_shift_limit=10, 
               b_shift_limit=10,  
               p=prob
          ),
          A.RandomBrightnessContrast(p=prob),
          A.RandomGamma(gamma_limit=(50, 150),p=prob),
          A.RandomToneCurve(scale=0.1, per_channel=False,p=prob),
          A.RingingOvershoot(p=prob),
          A.Sharpen(
               alpha=(0.2, 0.5),
               lightness=(0.5, 1.0),
               p=prob
          )
     ], n=numero, replace=False, p=1.0)

     random.seed(1492)
     augmented_image = transform(image=image)['image']
     new_path = "changed_images/new_" + img
     cv2.imwrite(new_path, augmented_image)