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

class TestSecretGraphs( unittest.TestCase ):

    def testHelmGraphV1(self):     
        oracle_value = 11
        scriptName   = TEST_CONSTANTS._helm_script1
        _, tupleList, _, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupleList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHelmGraphV2(self):     
        oracle_value = 8
        scriptName   = TEST_CONSTANTS._helm_script2
        _, tupleList, _ , _= scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupleList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHelmGraphV3(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script3
        _, tupleList, _ , _= scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupleList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHelmGraphV4(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script3
        _, _, valid_taint_ls, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( valid_taint_ls  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV5(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script4
        _, tupList, _, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( tupList  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV6(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._helm_script4
        _, _, valid_taint_ls, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( valid_taint_ls  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV7(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._helm_script4 
        within_match, _, _, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual( len(within_match[0]) + len(within_match[1]) + len(within_match[2]) , oracle_value ,   TEST_CONSTANTS._common_error_string + str(oracle_value)  )                           

    def testHelmGraphV8(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._helm_script5
        _, _, valid_taint_ls, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual(oracle_value, len( valid_taint_ls  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHelmGraphV9(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._helm_script5 
        within_match, _, _, _ = scanner.scanSingleManifest(scriptName)
        self.assertEqual( len(within_match[0]) + len(within_match[1]) + len(within_match[2]) , oracle_value ,   TEST_CONSTANTS._common_error_string + str(oracle_value)  )                           


class TestHTTPGraphs( unittest.TestCase ):

    def testHTTPGraphV1(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._http_script1
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   


    def testHTTPGraphV2(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._http_script2
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHTTPGraphV3(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._http_script3
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHTTPGraphV4(self):     
        oracle_value = 11
        scriptName   = TEST_CONSTANTS._http_script4
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHTTPGraphV5(self):     
        oracle_value = 11
        scriptName   = TEST_CONSTANTS._http_script5
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHTTPGraphV6(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._http_script6
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   


    def testHTTPGraphV7(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._http_script7
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHTTPGraphV8(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._http_script8
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHTTPGraphV9(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._http_script9
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testHTTPGraphV10(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._http_script10 
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHTTPGraphV11(self):     
        oracle_value = 1 
        scriptName   = TEST_CONSTANTS._http_script11 # this script is a multi doc 
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testHTTPGraphV12(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._http_script12
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  


    def testHTTPGraphV13(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._http_script13 
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testHTTPGraphV14(self):     
        '''
        this one tests if empty lists for a HTTP_DICT is returned. If empty list, then HTTP declared but not used 
        '''
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._http_script14
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic[1]  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHTTPGraphV15(self):     
        '''
        this one tests if a list with one item for a HTTP_DICT is returned. If list with >= 1 item, then HTTP declared and used 
        '''
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._http_script1 
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic[1]  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHTTPGraphV16(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._http_script15 
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic   ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHTTPGraphV17(self):     
        '''
        this one tests if empty lists for a HTTP_DICT is returned. If empty list, then HTTP declared but not used 
        '''
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._http_script16 
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic[1]  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHTTPGraphV18(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._http_script16 
        res_dic      = scanner.scanForHTTP(scriptName) 
        self.assertEqual(oracle_value, len( res_dic  ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

if __name__ == '__main__':
    unittest.main()