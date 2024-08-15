import requests

# class CountryData to perform the extraction of data from the url
class CountryData:

    # constructor to declare the variables used to fetch the data 
    def __init__(self, url):
        self.url = url
        self.data = None
        self.api_fetch_data()
    
    
    # checking the status code of given URL 
    def api_status_code(self):
        response = requests.get(self.url)
        return response.status_code

    # Fetch JSON data from the given URL and store it in self.data
    def api_fetch_data(self):
        # if the status code is success then only fetch the data else print error
        status_code = self.api_status_code()
        if status_code == 200:
            try:
                response = requests.get(self.url)
                self.data = response.json()
            except requests.RequestException as e:
                print(f"Error fetching data: {e}")
                self.data = None
        else:
            self.data = None

    # method to Display countries, currencies, and their symbols
    def display_countries_currencies_symbols(self):
        if not self.data:
            print("No data available.")
            return
        # for loop to itterate over countries to get country names currency and symbols 
        for country in self.data:
            country_name = country.get('name', {}).get('common', 'Unknown')
            currencies = country.get('currencies', {})
            currency_info = ', '.join(f"{name}: {info.get('symbol', 'No symbol')}" for name, info in currencies.items())
            print(f"Country: {country_name}")
            print(f"Currencies: {currency_info}")
            print()
    
    # Display countries that use dollars as currency
    def display_countries_with_dollars(self):
        if not self.data:
            print("No data available.")
            return
        
        countries_with_dollars = []
        # for loop to itterate over countries having currency as dollar
        for country in self.data:
            currencies = country.get('currencies', {})
            if any('USD' in name for name in currencies):
                country_name = country.get('name', {}).get('common', 'Unknown')
                countries_with_dollars.append(country_name)
        
        if countries_with_dollars:
            print("Countries with dollars as currency:")
            for country in countries_with_dollars:
                print(country)
        else:
            print("No countries with dollars as currency.")
        print()

    # Display countries that use euros as currency
    def display_countries_with_euros(self):
        if not self.data:
            print("No data available.")
            return
        
        countries_with_euros = []
        # for loop to itterate over countries having currency as euros
        for country in self.data:
            currencies = country.get('currencies', {})
            if any('EUR' in name for name in currencies):
                country_name = country.get('name', {}).get('common', 'Unknown')
                countries_with_euros.append(country_name)
        
        if countries_with_euros:
            print("Countries with euros as currency:")
            for country in countries_with_euros:
                print(country)
        else:
            print("No countries with euros as currency.")
        print()

# Example usage
if __name__ == "__main__":
    url = "https://restcountries.com/v3.1/all"
    # object creaction 
    country_data = CountryData(url)
    # function call with the help od object 
    country_data.display_countries_currencies_symbols()
    country_data.display_countries_with_dollars()
    country_data.display_countries_with_euros()