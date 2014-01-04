from setuptools import setup, find_packages

requires = [
    "setuptools>=0.7",
    "blockdiag",
    "deform",
    "colander",
    "webhelpers2",
]


tests_require = [
]

setup(name="rebecca.form.blockdiag",
      packages=find_packages(),
      namespace_packages=["rebecca", "rebecca.form"],
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          "testing": tests_require,
      },
)
