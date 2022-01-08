import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vinit_utils',
    version='0.0.1',
    author='Vinit Payal',
    author_email='vinitpayal@gmail.com',
    description='Python packaging demo',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/vinitpayal/python-packaging-demo',
    project_urls = {
        "Bug Tracker": "https://github.com/vinitpayal/python-packaging-demo/issues"
    },
    license='MIT',
    packages=['vinit_utils']
)
