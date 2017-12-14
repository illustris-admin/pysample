# pysample

Project folder structure is as follows:
bin
src
  .gitattributes
  .python-version
  README.md
  requirements.txt
  setup.py
dist

Packaging the project into an egg file is accomplished with the command below:
## python setup.py bdist_egg

The egg file will be found within the dist folder

Submitting into spark would be:
## spark-submit --py-files filename.egg src/sparkversion.py