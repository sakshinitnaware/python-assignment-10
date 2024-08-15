import requests
from collections import defaultdict 

# URL given in the task
URL = "https://api.openbrewerydb.org/v1/breweries"

# checking the status code of given URL
def api_status_code():
        response = requests.get(URL)
        return response.status_code

# Fetch breweries for a given state.
def get_breweries_by_state(state):
    # assigning return code of the method api_status_code() 
    status_code = api_status_code()
    # if the status code is success then only fetch the data else print error
    if status_code == 200:
            try:
                response = requests.get(f"{URL}?by_state={state}")
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"Error fetching data: {e}")
    else:
        print("Error fetching data")

# List brewery names by states.
def list_breweries_by_state(states):
    # defining empty list for breweries by states
    breweries_by_state = {}
    # for loop to itterate over states to get the names of brewery
    for state in states:
        breweries = get_breweries_by_state(state)
        breweries_by_state[state] = [brewery['name'] for brewery in breweries]
    return breweries_by_state

# Count breweries in each state.
def count_breweries_by_state(states):
    # defining empty list to count breweries by states
    count_by_state = {}
    # for loop to itterate over states to get the count of breweries in states
    for state in states:
        breweries = get_breweries_by_state(state)
        count_by_state[state] = len(breweries)
    return count_by_state

# Count the number of types of breweries in individual cities.
def count_breweries_by_city(states):
    city_breweries = defaultdict(lambda: defaultdict(int))
    # for loop to itterate over states to get the count of breweries in cities of the states of Alaska, Maine and New York
    for state in states:
        breweries = get_breweries_by_state(state)
        for brewery in breweries:
            city = brewery.get('city', 'Unknown')
            brewery_type = brewery.get('brewery_type', 'Unknown')
            city_breweries[city][brewery_type] += 1
    return city_breweries

# Count and list how many breweries have websites in the states.
def count_breweries_with_websites(states):
    website_count_by_state = defaultdict(int)
    # for loop to itterate over states to get the count of breweries with websites.
    for state in states:
        breweries = get_breweries_by_state(state)
        for brewery in breweries:
            if brewery.get('website_url'):
                website_count_by_state[state] += 1
    return website_count_by_state


def brewery():
    states = ["Alaska", "Maine", "New York"]
    
    # List the names of all breweries in the states
    breweries_by_state = list_breweries_by_state(states)
    for state, breweries in breweries_by_state.items():
        print(f"\nBreweries in {state}:")
        for brewery in breweries:
            print(f" - {brewery}")
    
    # Count the number of breweries in each state
    brewery_counts = count_breweries_by_state(states)
    print("\nNumber of breweries by state:")
    for state, count in brewery_counts.items():
        print(f"{state}: {count}")
    
    # Count the number of types of breweries in individual cities
    city_breweries = count_breweries_by_city(states)
    print("\nNumber of types of breweries in each city:")
    for city, types in city_breweries.items():
        print(f"\nCity: {city}")
        for brewery_type, count in types.items():
            print(f"  - {brewery_type}: {count}")
    
    # Count and list how many breweries have websites
    website_counts = count_breweries_with_websites(states)
    print("\nNumber of breweries with websites by state:")
    for state, count in website_counts.items():
        print(f"{state}: {count}")

if __name__ == "__main__":
    brewery()
