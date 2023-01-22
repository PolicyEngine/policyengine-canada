from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of our README file for PyPi
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Please make sure to cap all dependency versions, in order to avoid unwanted
# functional and integration breaks caused by external code updates.

general_requirements = [
    "pytest>=4,<6",
    "numpy>=1.11,<1.23",
    "black[jupyter]<23",
    "linecheck<1",
    "yaml-changelog==0.3.0",
    "coverage<7",
    "sortedcontainers<3",
    "numexpr<3",
    "dpath<3",
    "nptyping<2",
    "psutil<6",
    "wheel<1",
    "h5py>=3,<4",
    "microdf_python>=0.3.0,<1",
    "tqdm>=4.46.0,<5",
    "requests>=2.27.1,<3",
    "pandas>=1.4.2,<2",
    "policyengine_core>=1.11.4,<2",
    "plotly>=5.6.0,<6",
]

dev_requirements = [
    "jupyter-book<1",
    "furo<2023",
    "markupsafe==2.0.1",
    "sphinx>=4.5.0,<5",
    "sphinx-argparse>=0.3.2,<1",
    "sphinx-math-dollar>=1.2.1,<2",
]

setup(
    name="policyengine-canada",
    version="0.23.0",
    author="PolicyEngine",
    author_email="hello@policyengine.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    description="Microsimulation model for Canada's tax-benefit system.",
    keywords="tax benefit microsimulation framework",
    license="https://www.fsf.org/licensing/licenses/agpl-3.0.html",
    license_files=("LICENSE",),
    url="https://github.com/policyengine/policyengine-canada",
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "dev": dev_requirements,
    },
    install_requires=general_requirements,
    packages=find_packages(),
    include_package_data=True,
)
