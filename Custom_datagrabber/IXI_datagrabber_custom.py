from pathlib import Path
from junifer.api.decorators import register_datagrabber
from junifer.datagrabber import PatternDataGrabber

@register_datagrabber
class CustomIXIDataGrabber(PatternDataGrabber):
    def __init__(self, datadir: str | Path) -> None:
        types = ["T1w"]
        patterns = {
            "T1w": {
                "pattern": "{site}/{subject}/mri/m0wp1{subject}.nii.gz",
                "space": "native",  # Assuming native space for the T1w data
            }
        }
        replacements = ["site", "subject"]
        super().__init__(
            datadir=datadir,
            types=types,
            patterns=patterns,
            replacements=replacements,
        )
