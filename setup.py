from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in open_civic_backend/__init__.py
from open_civic_backend import __version__ as version

setup(
	name="open_civic_backend",
	version=version,
	description="Frappe app to build civic backends",
	author="zerodha",
	author_email="abhinav.raut@zerodha.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
