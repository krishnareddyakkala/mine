'''
Consider Share prices for a N number of companies given for each month since year     

         1990 in a CSV file.  Format of the file is as below with first line as header.

 

Year,Month,Company A, Company B,Company C, .............Company N

1990, Jan, 10, 15, 20, , ..........,50

1990, Feb, 10, 15, 20, , ..........,50

.

.

.

.

2013, Sep, 50, 10, 15............500

 

a) List for each Company year and month in which the share price was highest.

b) Submit a unit test with sample data to support your solution.   

 

Send the code back the code in .txt (filename should be the <developer name>-<years of experience>).
'''

class ProcessCompanyShares(object):
    def __init__(self, input_file):
        self.input_file = input_file
        
    def open_csv(self):
        return open(self.input_file, 'r')
    
    def process(self):
        results = []
        for line_no, data in enumerate(self.open_csv()):
            col_list = [s.strip() for s in data.split(",")]            
            if line_no == 0:
                companies = col_list[2:]
                for company in companies:
                    results.append((company,0,0,0))
            else:
                prices = col_list[2:]
                for index, share_price in enumerate(prices):
                    if results[index][3] < share_price:
                        results[index] = (results[index][0], col_list[0], col_list[1], share_price)
        return results
    
if __name__ == "__main__":
    import sys
    company_shares = ProcessCompanyShares(sys.argv[1])
    print company_shares.process()