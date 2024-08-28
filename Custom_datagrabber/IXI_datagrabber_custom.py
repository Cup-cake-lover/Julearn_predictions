from pathlib import Path
from junifer.api.decorators import register_datagrabber
from junifer.datagrabber import PatternDataGrabber

@register_datagrabber
class CustomIXIDataGrabber(PatternDataGrabber):
    def __init__(self, datadir: str | Path) -> None:
        types = ["VBM_GM"]
        patterns = {
            "VBM_GM": {
                "pattern": "{site}/{subject}/mri/m0wp1{subject}.nii.gz",
                "space": "MNI152NLin2009cAsym",  # Assuming native space for the T1w data
            }
        }
        replacements = ["site", "subject"]
        super().__init__(
            datadir=datadir,
            types=types,
            patterns=patterns,
            replacements=replacements,
        )
