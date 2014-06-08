from setuptools import setup

setup(name='zippackages',
      version='0.1',
      description='Cheap tricks for importing a zip file of packages',
      url='http://github.com/tr00st/zippackages',
      author='James Cheese',
      author_email='trust@tr00st.co.uk',
      license='MIT',
      packages=['zippackages'],
      zip_safe=False,
      include_package_data=True)
