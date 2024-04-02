from cx_Freeze import setup, Executable
import sys
import os

# Application name, version, and entry script
app_name = "Trivio"
version = "1.0"
script = "main.py"  # Your main application script

# Define paths to resources
images_path = os.path.join(os.path.dirname(__file__), 'images')
audios_path = os.path.join(os.path.dirname(__file__), 'audio')

# Setup configuration
setup(
    name=app_name,
    version=version,
    description="Your Application Description",
    options={
        'build_exe': {
            'include_files': [
                (images_path, 'images'),
                (audios_path, 'audio'),
            ],
        }
    },
    executables=[Executable("main.py")]
)