import yfinance as yf
from tracker.models import Company

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
                        'employee_count': str(info.get('fullTimeEmployees', 'N/A')),
                        'revenue': str(info.get('totalRevenue', 'N/A'))
                }
                
                return company_data
        
        except Exception as e:
                print(f"Error fetching data for {symbol}: {e}")
                return None

def save_company_to_db(symbol):
        data = get_company_profile(symbol)

        if data:
                try:
                        company, created = Company.objects.update_or_create(
                                name = data['name'],
                                defaults = {
                                        'description': data['description'],
                                        'industry': data['industry'],
                                        'country': data['country'],
                                        'website': data['website'],
                                        'employee_count': data['employee_count'],
                                        'revenue': data['revenue']
                                }
                        )

                        if created:
                                print(f"New company created: {company.name}")
                        else:
                                print(f"Company updated: {company.name}")
                        
                        return company
                except Exception as e:
                        print(f"Error saving to DB: {e}")
                        return None
        else:
                print(f"No data found for {symbol}")
                return None
                

# Testting        
# if __name__ == "__main__":
#         search_name = "AMZN"
#         print(f"Testing data for fetch: {search_name}")

#         details = get_company_profile(search_name)

#         if details:
#                 print("\nData found:\n")
#                 for key, value in details.items():
#                         print(f"{key}: {value}")
#         else:
#                 print("Nothing found! Check if you used a valid ticker.")