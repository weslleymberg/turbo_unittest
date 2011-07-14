from setuptools import setup, find_packages

version = '0.1.0'
readme = open('README.rst').read()

setup(name='turbo_unittest',
      version=version,
      description='Flexibility for testers!',
      long_description=readme,
      classifiers=[
          'Development Status :: 1 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ],
      keywords='turbo unittest setup test flexibility',
      author='Weslleymberg Lisboa',
      author_email='weslleym.lisboa@gmail.com',
      url='https://github.com/weslleymberg/turbo_unittest',
      license='MIT License',
      packages=find_packages()
      )
