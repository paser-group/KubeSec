import unittest 
import TEST_CONSTANTS 
import parser
import scanner 

class TestParsing( unittest.TestCase ):

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

if __name__ == '__main__':
    unittest.main()