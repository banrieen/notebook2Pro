""" Package flaskr
# By wheel
"""

from setuptools import setup
setup(
    name="ChePiao",
    version="v 0.1",
    author="haiyuan",
    author_email="banrieen@163.com",
    py_modules=['ChePiao'],
    packages=["flaskr"],
    include_package_data=True,
    license="Mozilla",
    description="Demo",
    keywords="chepiao flask",
    python_requires='>=3',
    install_requires=['Flask', 'request'],
    requires=['Flask','request',],
    data_files=['flaskr/static/style.css',
                'flaskr/templates/base.html',
                'flaskr/templates/auth/login.html',
                'flaskr/templates/auth/register.html',
                'flaskr/templates/blog/create.html',
                'flaskr/templates/blog/index.html',
                'flaskr/templates/blog/update.html',
                'flaskr/schema.sql'] 
)
