import unittest 
import TEST_CONSTANTS 
import parser
import scanner 

class TestScanning( unittest.TestCase ):

    def testSecret1(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml1
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret2(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml2
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret3(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml3
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret4(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml4
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret5(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._secret_yaml5
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret6(self):     
        oracle_value = 0 
        scriptName   = TEST_CONSTANTS._secret_yaml6
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret7(self):     
        oracle_value = 5
        scriptName   = TEST_CONSTANTS._secret_yaml7
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        holder       = [] 
        for _, v_ in secret_dict.items():
            holder = holder + v_[0] + v_[1]
        self.assertEqual(oracle_value, len(holder) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret8(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml8
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        holder       = [] 
        for _, v_ in secret_dict.items():
            holder = holder + v_[0] + v_[1]
        self.assertEqual(oracle_value, len(holder) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret9(self):     
        oracle_value = 0 
        scriptName   = TEST_CONSTANTS._secret_yaml9
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret10(self):     
        oracle_value = 0 
        scriptName   = TEST_CONSTANTS._secret_yaml10
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret11(self):     
        oracle_value = 2 
        scriptName   = TEST_CONSTANTS._cert_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret12(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._rsa_key_yaml
        yaml_as_dict = parser.loadYAML( scriptName )
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

class TestFalsePositives( unittest.TestCase ):

    def testSecret1(self):     
        oracle_value = TEST_CONSTANTS._none_kw
        scriptName   = TEST_CONSTANTS._fp_script1
        within_match_, _, _  = scanner.scanSingleManifest( scriptName )
        self.assertTrue( within_match_ == None ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script1
        _, templ_match , _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_match) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret3(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._fp_script2
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret4(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script2
        _, templ_match , _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_match) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret5(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._fp_script3
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret6(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script3
        _, _ , taint_map_ls  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(taint_map_ls) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret7(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script4
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret8(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script4
        _, templ_matches , _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret9(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._fp_script5
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret10(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script5
        _, _ , taint_map_ls  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(taint_map_ls) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret11(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script6
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret12(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script6
        _, template_matches , _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(template_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret13(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script7 
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )          

    def testSecret14(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script8 
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )          

    def testSecret15(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script9
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret16(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script9
        _, template_matches , _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(template_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret17(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script10
        yaml_as_dict = parser.loadYAML( scriptName ) 
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret18(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script10 
        _, _ , taint_map_lis  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(taint_map_lis) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret19(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script10 
        _, templ_matches , _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret20(self):     
        oracle_value = TEST_CONSTANTS._none_kw 
        scriptName   = TEST_CONSTANTS._fp_script10 
        within , _ , _  = scanner.scanSingleManifest( scriptName )
        self.assertTrue( within == None ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

if __name__ == '__main__':
    unittest.main()