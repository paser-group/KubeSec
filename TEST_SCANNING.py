import unittest 
import TEST_CONSTANTS 
import parser
import scanner 
import constants 

class TestScanning( unittest.TestCase ):

    def testSecret1(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml1
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret2(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml2
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret3(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml3
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret4(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml4
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret5(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._secret_yaml5
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret6(self):     
        oracle_value = 0 
        scriptName   = TEST_CONSTANTS._secret_yaml6
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )      

    def testSecret7(self):     
        oracle_value = 5
        scriptName   = TEST_CONSTANTS._secret_yaml7
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        holder       = [] 
        for _, v_ in secret_dict.items():
            holder = holder + v_[0] + v_[1]
        self.assertEqual(oracle_value, len(holder) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret8(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._secret_yaml8
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        holder       = [] 
        for _, v_ in secret_dict.items():
            holder = holder + v_[0] + v_[1]
        self.assertEqual(oracle_value, len(holder) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret9(self):     
        oracle_value = 0 
        scriptName   = TEST_CONSTANTS._secret_yaml9
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret10(self):     
        oracle_value = 0 
        scriptName   = TEST_CONSTANTS._secret_yaml10
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret11(self):     
        oracle_value = 2 
        scriptName   = TEST_CONSTANTS._cert_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret12(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._rsa_key_yaml
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        secret_dict  = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual(oracle_value, len(secret_dict) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              
    def testSecret13(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS.special_secret_1
        within, _, _, _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual(oracle_value, len(within[0]) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret14(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS.special_secret_1
        within, _, _, _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual(oracle_value, len(within[1]) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )               

    def testSecret15(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.special_secret_1
        within, _, _, _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual(oracle_value, len(within[2]) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )              

    def testSecret16(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS.special_secret_1
        within, _, _, _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual(oracle_value, len(within[0])  + len(within[1]) + len(within[2]) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )    


class TestFalsePositives( unittest.TestCase ):

    def testSecret1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script1
        within_match_, _, _ , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( len(within_match_[0]) + len(within_match_[1]) + len(within_match_[2]), 0,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script1
        _, templ_match , _ , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_match) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret3(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._fp_script2
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret4(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script2
        _, templ_match , _ , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_match) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret5(self):     
        oracle_value = 3
        scriptName   = TEST_CONSTANTS._fp_script3
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret6(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script3
        _, _ , taint_map_ls , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(taint_map_ls) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret7(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script4
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret8(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script4
        _, templ_matches , _ , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret9(self):     
        oracle_value = 4
        scriptName   = TEST_CONSTANTS._fp_script5
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret10(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script5
        _, _ , taint_map_ls , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(taint_map_ls) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret11(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script6
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret12(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script6
        _, template_matches , _, _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(template_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret13(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script7 
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )          

    def testSecret14(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script8 
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )          

    def testSecret15(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script9
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret16(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script9
        _, template_matches , _ , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(template_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret17(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._fp_script10
        dict_as_list = parser.loadMultiYAML( scriptName )
        yaml_as_dict = parser.getSingleDict4MultiDocs( dict_as_list )        
        initial_secret_dict = scanner.scanForSecrets( yaml_as_dict )
        self.assertEqual( oracle_value,  len(initial_secret_dict) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret18(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script10 
        _, _ , taint_map_lis , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(taint_map_lis) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret19(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script10 
        _, templ_matches , _ , _ = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len(templ_matches) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testSecret20(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._fp_script10 
        within_match_ , _ , _, _  = scanner.scanSingleManifest( scriptName )
        self.assertEqual( len(within_match_[0]) + len(within_match_[1]) + len(within_match_[2]), 0,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )  


class TestOverPrivilegedContainers( unittest.TestCase ):

    def testPrivilege1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._privi_scrip1 
        _, _, _, privi_dict = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len( privi_dict ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPrivilege2(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._privi_scrip2
        _, _, _, privi_dict = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len( privi_dict ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPrivilege3(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._privi_scrip3
        _, _, _, privi_dict = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len( privi_dict ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPrivilege4(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._privi_scrip4
        _, _, _, privi_dict = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len( privi_dict ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPrivilege5(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._privi_scrip5
        _, _, _, privi_dict = scanner.scanSingleManifest( scriptName )
        self.assertEqual( oracle_value,  len( privi_dict ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPrivilegeForMultiDoc(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.multi_doc_script1
        _, _, _, privi_dict = scanner.scanSingleManifest( scriptName )
        # print( privi_dict )
        self.assertEqual( oracle_value,  len( privi_dict ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )          


class TestMissingSecuContext( unittest.TestCase ):

    def testMissing1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._no_secu_cont_yaml1
        res_dic = scanner.scanForMissingSecurityContext( scriptName )
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testMissing2(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_secucont_no_yaml 
        res_dic = scanner.scanForMissingSecurityContext( scriptName )
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testAbsence1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._no_secu_cont_yaml2
        res_dic = scanner.scanForMissingSecurityContext( scriptName )
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testAbsence2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.secu_cont_fp_yaml 
        res_dic = scanner.scanForMissingSecurityContext( scriptName )
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPresent3(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_secucont_no_yaml 
        res_dic = scanner.scanForMissingSecurityContext( scriptName )
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testPresent4(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._no_secu_cont_yaml1
        res_dic = scanner.scanForMissingSecurityContext( scriptName )
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testMissingSecuForMultiDoc(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.multi_doc_script2
        res_dic = scanner.scanForMissingSecurityContext( scriptName )
        # print(res_dic)
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )                                


class TestDefaultNamespace( unittest.TestCase ):

    def testPresent1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml1 
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPresent2(self):     
        oracle_value = constants.DEPLOYMENT_KW 
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml1 
        res_dic = scanner.scanForDefaultNamespace( scriptName )
        self.assertEqual( oracle_value,   res_dic[1][0] ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPresent3(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml2
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testPresent4(self):     
        oracle_value = constants.POD_KW  
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml2 
        res_dic = scanner.scanForDefaultNamespace( scriptName )
        self.assertEqual( oracle_value,   res_dic[1][0] ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testMissing1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml3
        res_dic = scanner.scanForDefaultNamespace( scriptName )
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testMissing2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml3
        res_dic = scanner.scanForDefaultNamespace( scriptName )
        self.assertEqual( oracle_value,  len( res_dic[1] ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  


    def testTaintPresence1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml4 
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testTaintPresence2(self):     
        oracle_value = 2
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml4 
        res_dic = scanner.scanForDefaultNamespace( scriptName )
        self.assertEqual( oracle_value,  len( res_dic[1][0] ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testTaintPresence3(self):     
        oracle_value = TEST_CONSTANTS.test_sink_nspace_yam 
        scriptName   = TEST_CONSTANTS._dflt_nspace_yaml4 
        res_dic = scanner.scanForDefaultNamespace( scriptName )
        self.assertEqual( oracle_value,   res_dic[1][0][0] ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

    def testNamespaceAbsence1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_nspace_yaml_1 
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )          

    def testNamespaceAbsence2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_nspace_yaml_2
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )                  

    def testNamespaceAbsence3(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_nspace_yaml_3
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )    

    def testPresent5(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_nspace_yaml
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )           

    def testPresent6(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_nspace_default
        res_dic = scanner.scanForDefaultNamespace( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )  

        

class TestResourceLimits( unittest.TestCase ):

    def testAbsent1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.reso_yaml1
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.reso_yaml3 
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent3(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.reso_yaml4 
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testPresent1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_allow_privilege
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent4(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml1 
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent5(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml2
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent6(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml3
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )             
    def testAbsent7(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml4
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent8(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml5
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent9(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml6
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )             

    def testAbsent10(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml7
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  )             
    def testAbsent11(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml8
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent12(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml9
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent13(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_no_reso_yaml10 
        res_dic = scanner.scanForResourceLimits( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 


class TestMissingRollingUpdate( unittest.TestCase ):

    def testAbsent1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml1 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml2 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent3(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml3 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent4(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml4
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent5(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml4
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 


    def testAbsent6(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml5 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 


    def testAbsent7(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml6 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAbsent8(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml6 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testPresent1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml7  
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testPresent2(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml7 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic[1] ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testPresent3(self):     
        oracle_value = constants.DEPLOYMENT_KW 
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml7 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  res_dic[1][0]  ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testPresent4(self):     
        oracle_value = constants.DEPLOYMENT_KW 
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml8 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  res_dic[1][0]  ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 
    def testPresent5(self):     
        oracle_value = constants.DEPLOYMENT_KW 
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml9 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  res_dic[1][0]  ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 
    def testPresent6(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml9 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic[1] ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 
    def testPresent7(self):     
        oracle_value = constants.DEPLOYMENT_KW 
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml10 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  res_dic[1][0]  ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 
    def testPresent8(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml10 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 
    def testPresent9(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml11 
        res_dic = scanner.scanForRollingUpdates( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

class TestMissingNetPolicy( unittest.TestCase ):

    def testAbsent1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.net_policy_yaml 
        res_dic = scanner.scanForMissingNetworkPolicy( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 
class TestHostIssues( unittest.TestCase ):

    def testHostPIDPresenceV1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_host_ipc_yaml 
        res_dic      = scanner.scanForTruePID( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHostPIDPresenceV2(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_host_net_yaml
        res_dic      = scanner.scanForTruePID( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHostPIDAbsence(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.net_policy_yaml 
        res_dic      = scanner.scanForTruePID( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testDockerSockPresence(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_docker_sock_yaml
        res_dic      = scanner.scanDockerSock( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testDockerSockAbsence(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.net_policy_yaml 
        res_dic      = scanner.scanDockerSock( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHostNetworkPresenceV1(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_host_net_yaml
        res_dic      = scanner.scanForHostNetwork( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHostNetworkAbsence(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.net_policy_yaml 
        res_dic      = scanner.scanForHostNetwork( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testCAPSYSPresence(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_cap_sys_yaml
        res_dic      = scanner.scanForCAPSYS( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testCAPSYSAbsence(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.net_policy_yaml 
        res_dic      = scanner.scanForCAPSYS( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 
    def testHostAliasPresence(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_cap_sys_yaml
        res_dic      = scanner.scanForHostAliases( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHostAliasAbsence(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.net_policy_yaml 
        res_dic      = scanner.scanForHostAliases( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testHostNetworkPresenceV2(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_host_net_yaml2 
        res_dic      = scanner.scanForHostNetwork( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAllowPrivilegePresence(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_allow_privilege 
        res_dic      = scanner.scanAllowPrivileges( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAllowPrivilegeAbsence(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.net_policy_yaml 
        res_dic      = scanner.scanAllowPrivileges( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testAnotherDockerSock(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.another_dockersock 
        res_dic      = scanner.scanDockerSock( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testCAPSYSMODULE(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.cap_module_script
        res_dic      = scanner.scanForCAPMODULE( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 


class TestSecCompIssues( unittest.TestCase ):

    def testUnconfinedSecComp(self):     
        oracle_value = 1
        scriptName   = TEST_CONSTANTS.tp_seccomp_unconf
        res_dic      = scanner.scanForUnconfinedSeccomp( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testNeutralSecComp1(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_seccomp_unconf
        res_dic      = scanner.scanForUnconfinedSeccomp( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testNeutralSecComp2(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.fp_rolling_yaml7
        res_dic      = scanner.scanForUnconfinedSeccomp( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 

    def testNeutralSecComp3(self):     
        oracle_value = 0
        scriptName   = TEST_CONSTANTS.tp_host_net_yaml
        res_dic      = scanner.scanForUnconfinedSeccomp( scriptName ) 
        self.assertEqual( oracle_value,  len( res_dic ) ,    TEST_CONSTANTS._common_error_string + str(oracle_value)  ) 


if __name__ == '__main__':
    unittest.main()