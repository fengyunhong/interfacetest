import os

from UnittestCase.test_case01 import TestCase01
from UnittestCase.test_case02 import TestCase02
from UnittestCase.test_case03 import TestCase03
import unittest
import sys
# case_01=unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# 执行多个case 的第一种方法   9-13行
# case_02=unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case_03=unittest.TestLoader().loadTestsFromTestCase(TestCase03)
# suite = unittest.TestSuite([case_01,case_02,case_03])
# unittest.TextTestRunner().run(suite)


#执行多个case的第二种方法
case_path=os.path.dirname(os.getcwd())
print(case_path)
discover = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)