import mock
import unittest
from share_companies import ProcessCompanyShares


class TestProcessCompanyShares(unittest.TestCase):
    def setUp(self):
        self.input_file = open('company_shares.csv')
        
    
    @mock.patch('share_companies.ProcessCompanyShares.open_csv')
    def test_process(self, mock_open_csv):
        return_val = ['Year,Month,Company A,Company B,Company C,Company D',
                        '1990,Jan,10,20,40,50',
                        '1990,Feb,50,10,60,30',
                        '1990,Mar,30,15,20,47',
                        '1991,Sep,30,15,24,58',
                        '1991,Oct,25,10,21,30',
                        '1992,Apr,45,25,25,74'
                        ]
        company_shares = ProcessCompanyShares(self.input_file)
        mock_open_csv.return_value = return_val
        results = company_shares.process()
        self.assertEqual(results, [('Company A', '1990', 'Feb', '50'), ('Company B', '1992', 'Apr', '25'), ('Company C', '1990', 'Feb', '60'), ('Company D', '1992', 'Apr', '74')])
        
    
    @mock.patch('share_companies.ProcessCompanyShares.open_csv')
    def test_process_with_spaces(self, mock_open_csv):
        return_val = ['Year, Month , Company A  , Company B  , Company C , Company D  ',
                        '1990, Jan ,10, 20, 40, 50',
                        '1990 , Feb ,50, 10, 60, 30',
                        '1990 , Mar ,30, 15, 20, 47',
                        '1991 , Sep ,30, 15, 24, 58',
                        '1991 , Oct ,25, 10, 21, 30',
                        '1992 , Apr  , 45 , 25 , 25 , 74'
                        ]
        company_shares = ProcessCompanyShares(self.input_file)
        mock_open_csv.return_value = return_val
        results = company_shares.process()
        self.assertEqual(results, [('Company A', '1990', 'Feb', '50'), ('Company B', '1992', 'Apr', '25'), ('Company C', '1990', 'Feb', '60'), ('Company D', '1992', 'Apr', '74')])
    