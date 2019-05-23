from setuptools import setup
  
requires = []

setup(
    name='opsfw',
    scripts=['bin/trickleFiles.py'],
    use_scm_version={'version_scheme': 'post-release'},
    setup_requires=['setuptools_scm'],
    packages=['opsfw'],
    license='GPL',
    author='WOM',
    author_email='wom@lsst.org',
    description='opsforwarder description',
    install_requires=requires,
)

