from setuptools import find_packages, setup

setup(
    name="jdeskew",
    description="Document Image Skew Estimation using Adaptive Radial Projection",
    author="Luan Pham",
    author_email="phamquiluan@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy", "opencv-python"],
    extra_requires={"dev": ["black", "pytest", "coverage"]},
)
