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

class TestIntegration( unittest.TestCase ):

    def testOutputColums(self):     
        oracle_value  = 11
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ) )
        _, cols       = df_all.shape 
        self.assertEqual(oracle_value, cols ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   



    def testOutputRows(self):     
        oracle_value  = 132 
        dirName       = TEST_CONSTANTS._sample_output_dir 
        content_as_ls = scanner.runScanner( dirName )
        df_all        = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ) )
        rows, _       = df_all.shape 
        self.assertEqual(oracle_value, rows ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   



    def testSampleOutput(self):     
        oracle_value    = 137
        dirName         = TEST_CONSTANTS._sample_output_dir 
        content_as_ls   = scanner.runScanner( dirName )
        df_all          = pd.DataFrame(  main.getCountFromAnalysis( content_as_ls ),  columns=constants.CSV_HEADER )
        self.assertEqual(oracle_value, sum( df_all[TEST_CONSTANTS._sample_df_field1].tolist() ) ,  TEST_CONSTANTS._common_error_string + str(oracle_value)  )   


if __name__ == '__main__':
    unittest.main()