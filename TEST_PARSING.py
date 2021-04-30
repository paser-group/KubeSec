'''
Akond Rahman 
April 30, 2022 
Test Utilities for Parsing 
'''

import unittest 
import TEST_CONSTANTS 
import parser

class TestParsing( unittest.TestCase ):

    def testKeyExtraction(self):     
        oracle_value = 4 
        scriptName   = TEST_CONSTANTS._test_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        self.assertEqual(oracle_value, len(yaml_as_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   
                    



if __name__ == '__main__':
    unittest.main()
