from setuptools import setup

setup(
    name='aiohaofs',
    version='0.1.0',
    description='异步好分数(https://www.haofenshu.com/)爬虫',
    url="https://github.com/cloudw233/aiohaofs",
    author=["haoye_qwq","Yixiangzhilv"],
    author_email="cloudw233@outlook.com",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    keywords="API sdk spider",
    install_requires=["aiohttp", "mail_gw"],
    packages=["aiohfs"],
    project_urls={
        "Bug Reports": "https://github.com/cloudw233/aiohaofs/issues",
        "Source": "https://github.com/Danny-Yxzl/haofs",
    },
)
