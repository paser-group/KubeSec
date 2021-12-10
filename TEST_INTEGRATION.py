'''
Akond Rahman 
June 16, 2021 
Placeholder for integration test code 
'''

import unittest 
import TEST_CONSTANTS 
import main 
import scanner 
import pandas as pd 
import constants 

class TestSimpleIntegration( unittest.TestCase ):

    def testOutputColums(self):     
        oracle_value  = 22
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ) )
        _, cols       = df_all.shape 
        self.assertEqual(oracle_value, cols ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   



    def testOutputRows(self):     
        oracle_value  = 241 
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ) )
        rows, _       = df_all.shape 
        self.assertEqual(oracle_value, rows ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   



    def testSampleOutput(self):     
        oracle_value    = 214
        dirName         = TEST_CONSTANTS._sample_output_dir 
        content_as_ls   = scanner.runScanner( dirName )
        df_all          = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        self.assertEqual(oracle_value, sum( df_all[TEST_CONSTANTS._sample_df_field1].tolist() ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   



class TestIntegrationCount( unittest.TestCase ):

    def testWithinSecretCount1(self):     
        oracle_value  = 0
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        script_df     = df_all[df_all[TEST_CONSTANTS.df_yaml_path_field]== TEST_CONSTANTS._integ_fp_scrip1] 
        within_sec_cnt= script_df[TEST_CONSTANTS._sample_df_field2].tolist()[0]

        self.assertEqual(oracle_value, within_sec_cnt ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testWithinSecretCount2(self):     
        oracle_value  = 0
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        script_df     = df_all[df_all[TEST_CONSTANTS.df_yaml_path_field]== TEST_CONSTANTS._integ_fp_scrip2] 
        within_sec_cnt= script_df[TEST_CONSTANTS._sample_df_field2].tolist()[0]

        self.assertEqual(oracle_value, within_sec_cnt ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testWithinSecretCount3(self):     
        oracle_value  = 0
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        script_df     = df_all[df_all[TEST_CONSTANTS.df_yaml_path_field]== TEST_CONSTANTS._integ_fp_scrip3]  
        within_sec_cnt= script_df[TEST_CONSTANTS._sample_df_field2].tolist()[0]

        self.assertEqual(oracle_value, within_sec_cnt ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   


    def testWithinSecretCount4(self):     
        oracle_value  = 0
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        script_df     = df_all[df_all[TEST_CONSTANTS.df_yaml_path_field]== TEST_CONSTANTS._integ_fp_scrip4]   
        within_sec_cnt= script_df[TEST_CONSTANTS._sample_df_field2].tolist()[0]

        self.assertEqual(oracle_value, within_sec_cnt ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testWithinSecretCount5(self):     
        oracle_value  = 0
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        script_df     = df_all[df_all[TEST_CONSTANTS.df_yaml_path_field]== TEST_CONSTANTS._integ_fp_scrip5]   
        within_sec_cnt= script_df[TEST_CONSTANTS._sample_df_field2].tolist()[0]

        self.assertEqual(oracle_value, within_sec_cnt ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testWithinSecretCount6(self):     
        oracle_value  = 0
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        script_df     = df_all[df_all[TEST_CONSTANTS.df_yaml_path_field]== TEST_CONSTANTS._integ_fp_scrip6]   
        within_sec_cnt= script_df[TEST_CONSTANTS._sample_df_field2].tolist()[0]

        self.assertEqual(oracle_value, within_sec_cnt ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

    def testWithinSecretCount7(self):     
        oracle_value  = 0
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        script_df     = df_all[df_all[TEST_CONSTANTS.df_yaml_path_field]== TEST_CONSTANTS._integ_fp_scrip7]    
        within_sec_cnt= script_df[TEST_CONSTANTS._sample_df_field2].tolist()[0]

        self.assertEqual(oracle_value, within_sec_cnt ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   

if __name__ == '__main__':
    unittest.main()