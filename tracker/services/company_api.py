import yfinance as yf

def get_company_symbol(name):
       return name

def get_company_profile(symbol):

        try:
                ticker = yf.Ticker(symbol)
                info = ticker.info

                if 'symbol' not in info and 'shortName' not in info:
                        return None

                company_data = {
                        'name': info.get('longName') or info.get('shortName'),
                        'description': info.get('longBusinessSummary'),
                        'industry': info.get('industry'),
                        'country': info.get('country'),
                        'website': info.get('website'),
                        'employee_number': str(info.get('fullTimeEmployees', 'N/A')),
                        'revenue': str(info.get('totalRevenue', 'N/A'))
                }
                
                return company_data
        
        except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
                return None

# Testting        
if __name__ == "__main__":
        search_name = "AMZN"
        print(f"Testing data for fetch: {search_name}")

        details = get_company_profile(search_name)

        if details:
                print("\nData found:\n")
                for key, value in details.items():
                        print(f"{key}: {value}")
        else:
                print("Nothing found! Check if you used a valid ticker.")