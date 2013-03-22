from setuptools import setup

setup(name='PubNubPython27', version='1.0',
      description='OpenShift Python-2.7 Community Cartridge based application',
      author='Doron Sherman', author_email='doron@pubnub.com',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['greenlet', 'gevent',
                        #  'MySQL-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
