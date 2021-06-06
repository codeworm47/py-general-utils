import setuptools

setuptools.setup(
   name='py_general_utils',
   version='1.0.0.3',
   description='some useful and general utilities in pure python',
   author='Hesam Rasouli',
   author_email='hesam.rasouli1@gmail.com',
   install_requires=['aiohttp', 'json-get'],
   packages=setuptools.find_packages()
)
