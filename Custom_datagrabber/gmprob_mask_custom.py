from pathlib import Path

from junifer.data import register_mask

# this path is only an example, of course use the correct path
# on your system:
mask_path = "/home/hsreekri/Julearn_predictions/CAT12_IXI555_MNI152_TMP_GS_GMprob0.2_clean.nii.gz"

register_mask(name="GMProb_0.2_custom", mask_path=mask_path, space="MNI152NLin2009cAsym")