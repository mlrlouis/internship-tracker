import requests
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
API_KEY = os.getenv("FMP_API_KEY")

if not API_KEY:
        print("Warning: FMP_API_KEY not found! Please check your .env file!")

def get_company_symbol(name):
        url = f"https://financialmodelingprep.com/api/v3/profile/{symbol}?apikey={API_KEY}"

        try:
                response = requests.get(url)
                response.raise_for_status()

                data = response.json()

                if data:
                        profile = data[0]

                        company_data = {
                                'name': profile.get('companyName'),
                                'description': profile.get('description'),
                                'industry': profile.get('industry'),
                                'country': profile.get('country'),
                                'logo_url': profile.get('image'),
                                'website': profile.get('website'),
                                'employee_number': str(profile.get('fullTimeEmployees', 'N/A')),
                                'revenue': str(profile.get('mktCap', 'N/A'))
                        }
                        return company_data
                else:
                        return None
        except requests.exceptions.RequestException as e:
                print(f"Error fetching profile: {e}")
                return None