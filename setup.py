from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Core requirements
REQUIRED = [
    "deepface>=0.0.79",
    "opencv-python>=4.7.0",
    "numpy>=1.21.0",
    "pandas>=1.3.0",
]

# Optional platform-specific requirements
EXTRAS = {
    "web": [
        "Flask>=2.0.0",
        "Flask-SocketIO>=5.0.0",
    ],
    "mobile": [
        "kivy>=2.1.0",
    ],
    "desktop": [
        "customtkinter>=5.1.2",
    ],
}

# Add 'all' option that includes all platform dependencies
EXTRAS["all"] = [pkg for platform in EXTRAS.values() for pkg in platform]

setup(
    name="krezy",
    version="1.0.0",
    author="Aakif Mudel",
    author_email="aakifmudel@gmail.com",
    description="A powerful cross-platform emotion detection library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itsaakif/krezy",
    project_urls={
        "Bug Tracker": "https://github.com/itsaakif/krezy/issues",
        "Documentation": "https://krezy.readthedocs.io/",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    entry_points={
        "console_scripts": [
            "krezy-web=krezy.web.app:main[web]",
            "krezy-mobile=krezy.mobile.app:main[mobile]",
            "krezy-desktop=krezy.desktop.app:main[desktop]",
        ],
    },
)
