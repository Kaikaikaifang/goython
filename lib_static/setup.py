from Cython.Build import cythonize
from setuptools import Extension, setup

# 拓展模块
setup(ext_modules=cythonize(
    [
        Extension(
            name="go_add",
            sources=["external.pyx"],
            extra_objects=['library.a'] # 必须包含 extra_objects 项，否则编译的动态库将找不到对应的库文件
        )
    ],
    language_level=3,
), )
