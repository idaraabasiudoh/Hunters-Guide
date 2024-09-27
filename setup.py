from setuptools import setup

APP = ['main.py']  # Change 'main.py' to the actual script you want to run
DATA_FILES = ['cover_letter_standards.txt', 'refining.txt', 'refining_2.txt']
OPTIONS = {
    'argv_emulation': True,

    'includes': ['pkg_resources', 'pkg_resources.py2_warn'],  # Fix the pkg_resources issue
    'resources': DATA_FILES,  # Include your text files
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)