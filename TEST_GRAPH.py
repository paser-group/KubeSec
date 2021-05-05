'''
Akond Rahman 
May 05, 2021
Testing for graph utilities 
'''

import unittest 
import TEST_CONSTANTS 
import parser
import graphtaint
import scanner

class TestGraphing( unittest.TestCase ):

    def testHelmGraphV1(self):     
        oracle_value = 11
        scriptName   = TEST_CONSTANTS._helm_script1
        _, tupleList, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupleList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHelmGraphV2(self):     
        oracle_value = 8
        scriptName   = TEST_CONSTANTS._helm_script2
        _, tupleList, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupleList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHelmGraphV3(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script3
        _, tupleList, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupleList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHelmGraphV4(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script3
        _, _, valid_taint_ls = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( valid_taint_ls  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV5(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script4
        _, tupList, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV6(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script4
        _, _, valid_taint_ls = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( valid_taint_ls  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV7(self):     
        oracle_value = TEST_CONSTANTS._none_kw 
        scriptName   = TEST_CONSTANTS._helm_script4 
        within_match, _, _ = scanner.scanSingleManifest(scriptName)
        self.assertTrue( within_match == None ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )                           

    def testHelmGraphV8(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._helm_script5
        _, _, valid_taint_ls = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( valid_taint_ls  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV9(self):     
        oracle_value = TEST_CONSTANTS._none_kw 
        scriptName   = TEST_CONSTANTS._helm_script5 
        within_match, _, _ = scanner.scanSingleManifest(scriptName)
        self.assertTrue( within_match == None ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )                           


if __name__ == '__main__':
    unittest.main()