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
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        self.assertEqual(oracle_value, len(yaml_as_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   
                    
    def testKeyPathLength(self):     
        oracle_value = 9 
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        key_lis      = parser.keyMiner( yaml_as_dict, TEST_CONSTANTS._value_for_key )
        self.assertEqual(oracle_value, len(key_lis) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testKeyPath1(self):     
        oracle_value = TEST_CONSTANTS._spec_kw 
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        key_lis      = parser.keyMiner( yaml_as_dict, TEST_CONSTANTS._value_for_key )
        self.assertEqual(oracle_value, key_lis[0] ,  TEST_CONSTANTS._common_error_string + oracle_value  )   

    def testKeyPath2(self):     
        oracle_value = TEST_CONSTANTS._mount_path_kw 
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        key_lis      = parser.keyMiner( yaml_as_dict, TEST_CONSTANTS._value_for_key )
        self.assertEqual(oracle_value, key_lis[-2] ,  TEST_CONSTANTS._common_error_string + oracle_value  )         

    def testKeyCount(self):     
        oracle_value = 226 
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        key_lis      = [] 
        parser.getKeyRecursively  ( yaml_as_dict, key_lis )
        self.assertEqual(oracle_value, len(key_lis) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )                     

    def testValueCount(self):     
        oracle_value = 151 
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        key_lis      = list( parser.getValuesRecursively  ( yaml_as_dict ) )
        self.assertEqual(oracle_value, len(key_lis) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )    

    def testK8SYAMLValidity1(self):     
        self.assertTrue( parser.checkIfValidK8SYaml(TEST_CONSTANTS._valid_test_yaml) , TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._true_kw )

    def testK8SYAMLValidity2(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml1), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )
    
    def testK8SYAMLValidity3(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml2), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )

    def testK8SYAMLValidity4(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml3), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )

    def testK8SYAMLValidity5(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml4), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )

    def testK8SYAMLValidity6(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml5 ), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )

    def testK8SYAMLValidity7(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml6 ), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )
    
    def testK8SYAMLValidity8(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml7 ), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )

    def testK8SYAMLValidity9(self):     
        self.assertFalse( parser.checkIfValidK8SYaml(TEST_CONSTANTS._invalid_test_yaml8 ), TEST_CONSTANTS._common_error_string + TEST_CONSTANTS._false_kw )

    def testValueFromKey1(self):     
        oracle_value = 53
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_list    = []
        parser.getValsFromKey(yaml_as_dict, TEST_CONSTANTS._name_kw , temp_list  )
        self.assertEqual(oracle_value, len(temp_list) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )    

    def testValueFromKey2(self):     
        oracle_value = 15
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_list    = []
        parser.getValsFromKey(yaml_as_dict, TEST_CONSTANTS._mount_path_kw , temp_list  )
        self.assertEqual(oracle_value, len(temp_list) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )    

    def testValueFromKey3(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_list    = []
        parser.getValsFromKey(yaml_as_dict, TEST_CONSTANTS._privilege_kw  , temp_list  )
        self.assertEqual(oracle_value, len(temp_list) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  
              
    def testValueFromKey4(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_list    = []
        parser.getValsFromKey(yaml_as_dict, TEST_CONSTANTS._delay_kw , temp_list  )
        self.assertEqual(oracle_value, len(temp_list) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testValueFromKey5(self):     
        oracle_value = 10
        scriptName   = TEST_CONSTANTS._test_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        temp_list    = []
        parser.getValsFromKey(yaml_as_dict, TEST_CONSTANTS._key_kw , temp_list  )
        self.assertEqual(oracle_value, len(temp_list) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  


class TestParseMultidocs( unittest.TestCase ):

    def testMultidocV1(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS.multi_doc_script1
        dict_as_list = parser.loadMultiYAML( scriptName )
        self.assertEqual(oracle_value, len(dict_as_list) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testMultidocV2(self):     
        oracle_value = 6
        scriptName   = TEST_CONSTANTS.multi_doc_script2
        dict_as_list = parser.loadMultiYAML( scriptName )
        self.assertEqual(oracle_value, len(dict_as_list) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testMultidoc2SingleDic(self):     
        oracle_value = 24
        scriptName   = TEST_CONSTANTS.multi_doc_script2
        dict_as_list = parser.loadMultiYAML( scriptName )
        single_dict  = parser.getSingleDict4MultiDocs( dict_as_list )
        # print(single_dict.keys())
        self.assertEqual(oracle_value, len(list(  single_dict.keys()) ),  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

if __name__ == '__main__':
    unittest.main()
