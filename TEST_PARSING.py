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
                    
    def testKeyPathLength(self):     
        oracle_value = 9 
        scriptName   = TEST_CONSTANTS._test_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        key_lis      = parser.keyMiner( yaml_as_dict, TEST_CONSTANTS._value_for_key )
        self.assertEqual(oracle_value, len(key_lis) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testKeyPath1(self):     
        oracle_value = 'spec'
        scriptName   = TEST_CONSTANTS._test_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        key_lis      = parser.keyMiner( yaml_as_dict, TEST_CONSTANTS._value_for_key )
        self.assertEqual(oracle_value, key_lis[0] ,  TEST_CONSTANTS._common_error_string + oracle_value  )   

    def testKeyPath2(self):     
        oracle_value = 'mountPath'
        scriptName   = TEST_CONSTANTS._test_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        key_lis      = parser.keyMiner( yaml_as_dict, TEST_CONSTANTS._value_for_key )
        self.assertEqual(oracle_value, key_lis[-2] ,  TEST_CONSTANTS._common_error_string + oracle_value  )         

    def testKeyCount(self):     
        oracle_value = 226 
        scriptName   = TEST_CONSTANTS._test_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        key_lis      = [] 
        parser.getKeyRecursively  ( yaml_as_dict, key_lis )
        self.assertEqual(oracle_value, len(key_lis) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )                     

    def testValueCount(self):     
        oracle_value = 151 
        scriptName   = TEST_CONSTANTS._test_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        key_lis      = list( parser.getValuesRecursively  ( yaml_as_dict ) )
        self.assertEqual(oracle_value, len(key_lis) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )                     

if __name__ == '__main__':
    unittest.main()
