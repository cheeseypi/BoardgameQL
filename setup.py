from setuptools import setup

with open("README.rst","r") as f:
    long_description = f.read()
with open("LICENSE","r") as f:
    my_license = f.read()
with open("requirements.txt","r") as f:
    packages = f.read().split('\n')

setup(name="BoardgameQL",
      python_requires=">=3",
      version="1.0.0",
      description="A graphQL server for easily building state-based online board games",
      long_description=long_description,
      long_description_content_type="text/-rst",
      license=my_license,
      author="Matt Doto",
      author_email="matt@mattdoto.com",
      url="https://github.com/cheeseypi/BoardgameQL",
      project_urls={
          'Source': 'https://github.com/cheeseypi/BoardgameQL'
      },
      install_requires=packages,
      packages=['boardgameql'])
