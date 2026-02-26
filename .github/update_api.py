import os
import re


def main():
    # First, find the current package version number from pyproject.toml
    with open("pyproject.toml", "r") as f:
        content = f.read()
    version = re.search(r'version = "(.+?)"', content).group(1)
    # Then, clone the https://github.com/policyengine/policyengine-api repo using the GitHub CLI
    pat = os.environ["GITHUB_TOKEN"]
    os.system(
        f"git clone https://nikhilwoodruff:{pat}@github.com/policyengine/policyengine-api"
    )
    # Then, cd inside and run gcp/bump_country_package.py --country policyengine-uk --version {version}
    os.system(
        f"cd policyengine-api && python gcp/bump_country_package.py --country policyengine-canada --version {version}"
    )


if __name__ == "__main__":
    main()
