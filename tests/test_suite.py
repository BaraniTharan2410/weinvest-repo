import unittest
from tests.testA.rebalance_tests import RebalanceTests
from tests.testC.tab_test import TabTests


#get test from all the classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(RebalanceTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TabTests)

#create test suite combining all the testcases
smoke_test = unittest.TestSuite([tc1, tc3])
unittest.TextTestRunner(verbosity=2).run(smoke_test)