from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of our README file for PyPi
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Please make sure to cap all dependency versions, in order to avoid unwanted
# functional and integration breaks caused by external code updates.

general_requirements = [
    "black[jupyter]<23",
    "coverage<7",
    "dpath<3",
    "h5py>=3,<4",
    "linecheck<1",
    "microdf_python>=0.3.0,<1",
    "nptyping<2",
    "numexpr<3",
    "numpy>=1.11,<1.23",
    "pandas>=1.4.2,<2",
    "plotly>=5.6.0,<6",
    "policyengine_core>=2.1,<3",
    "psutil<6",
    "pytest",
    "requests>=2.27.1,<3",
    "sortedcontainers<3",
    "tqdm>=4.46.0,<5",
    "wheel<1",
    "yaml-changelog==0.3.0",
]

dev_requirements = [
    "furo<2023",
    "jupyter-book<1",
    "markupsafe==2.0.1",
    "pydata-sphinx-theme==0.13.1",
    "sphinx>=4.5.0,<5",
    "sphinx-argparse>=0.3.2,<1",
    "sphinx-math-dollar>=1.2.1,<2",
]

setup(
    name="policyengine-canada",
    version="0.83.0",
    author="PolicyEngine",
    author_email="hello@policyengine.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
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
    # Windows CI requires Python 3.9.
    python_requires=">=3.7",
    install_requires=general_requirements,
    packages=find_packages(),
    include_package_data=True,
)
