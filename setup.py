from setuptools import setup

setup(name = 'vcf_venn',
  version = '0.1.0',
  author = 'Simon Gladman',
  author_email = 'simon.gladman@monash.edu',
  description = 'a program for comparing Variant Call Format files',
  packages = [
    'vcf_venn',
  ],
  package_data={'vcf_venn': ['data/*']},
  entry_points={
          'console_scripts': ['vcf_venn = vcf_venn.vcf_venn:main']
  },
  long_description=open('README').read(),
  classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT',
        'Operating System :: POSIX',
        'Programming Language :: Python',
  ],  
)