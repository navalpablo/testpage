import os
import nibabel as nib
import numpy as np

# Load the atlas file
atlas = nib.load('data/atlas.nii.gz')
atlas_data = atlas.get_fdata()

# Create output directory
output_dir = 'data/individual_regions'
os.makedirs(output_dir, exist_ok=True)

# Load region labels
region_labels = {}
with open('data/region_labels.txt', 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) == 3:
            index, short_name, full_name = parts
            region_labels[int(index)] = full_name

# Create individual NIfTI files for each region
for index, full_name in region_labels.items():
    region_data = np.zeros_like(atlas_data)
    region_data[atlas_data == index] = 1
    
    region_nifti = nib.Nifti1Image(region_data, atlas.affine, atlas.header)
    
    filename = f"{index:02d}_{full_name.replace(' ', '_')}.nii.gz"
    nib.save(region_nifti, os.path.join(output_dir, filename))

print("Individual region NIfTI files have been created in the 'data/individual_regions' directory.")