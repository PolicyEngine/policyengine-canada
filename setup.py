from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of our README file for PyPi
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Core requirements with refined version constraints
general_requirements = [
    "policyengine_core>=3.23.6",
    "black[jupyter]",
    "coverage<7",
    "dpath<3",
    "h5py>=3,<4",
    "linecheck<1",
    "microdf_python>=1.2.1",
    "nptyping<2",
    "numexpr<3",
    "pandas>=2.2.0",
    "plotly>=5.6.0,<6",
    "pytest",
    "requests>=2.27.1,<3",
    "sortedcontainers<3",
    "tqdm>=4.46.0,<5",
    "wheel<1",
    "yaml-changelog==0.3.0",
]

dev_requirements = [
    "furo",
    "jupyter-book",
    "markupsafe",
    "pydata-sphinx-theme",
    "sphinx",
    "sphinx-argparse",
    "sphinx-math-dollar",
]

setup(
    name="policyengine-canada",
    version="0.96.3",
    author="PolicyEngine",
    author_email="hello@policyengine.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
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
    python_requires=">=3.10",
    install_requires=general_requirements,
    packages=find_packages(),
    include_package_data=True,
)
