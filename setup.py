
import os
from setuptools import setup

setup(
  name = "cocotb-unitsim",
  packages=['unitsim'],
  package_dir = {'' : 'src'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("cocotb-unitsim provides a method for unit-testing testbench code that uses the cocotb API without using a simulator"),
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL", "Coverage", "cocotb"],
  url = "https://github.com/mballance/cocotb-unitsim",
  setup_requires=[
    'setuptools_scm',
  ],
  install_requires=[
    'cocotb',
  ],
)

