import setuptools

setuptools.setup(
   name='py_general_utils',
   version='1.2.2.2',
   description='some useful and general utilities in pure python',
   author='Hesam Rasouli',
   author_email='hesam.rasouli1@gmail.com',
   install_requires=['aiohttp', 'mako', 'httpx'],
   packages=setuptools.find_packages()
)
