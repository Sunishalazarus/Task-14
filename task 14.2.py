#Q2. Visit the given URL and write a python program #

import requests

class BreweryList:
    def __init__(self, url):  
         # Initialize the class with the provided URL      
        self.url = url
        self.response = requests.get(url)
   
    def isConnected(self):
         # To Check if the connection to the URL is successful (HTTP status code 200)
        if self.response.status_code == 200:
            return True
        return False

    def fetchData(self):
        try:
             # To Check if the connection is successful and return the JSON data
            if self.isConnected():
                return self.response.json()
            raise Exception()
        except:
            print("It is not connected")
            return None
        
    def getBreweriesInStates(self, target_states):
        data = self.fetchData()
        if data and isinstance(data, list):
            breweries_by_state = {state: [] for state in target_states}
            for brewery in data:
                if 'state' in brewery and brewery['state'] in target_states and 'name' in brewery:
                    breweries_by_state[brewery['state']].append(brewery['name'])
            return breweries_by_state
        else:
            print("It is not connected to brewery data")

    def getBreweriesCountByState(self, target_states):
        data = self.fetchData()
        if data and isinstance(data, list):
            breweries_count_by_state = {state: 0 for state in target_states}
            for brewery in data:
                if 'state' in brewery and brewery['state'] in target_states:
                    breweries_count_by_state[brewery['state']] += 1
            return breweries_count_by_state
        else:
            print("It is not connected to brewery data")

    def getBreweryTypesByCity(self, target_states):
        brewery_types_by_city = {}
        data = self.fetchData()

        if data and isinstance(data, list):
            for brewery in data:
                if 'state' in brewery and brewery['state'] in target_states:
                    state = brewery['state']
                    city = brewery['city']
                    brewery_type = brewery['brewery_type']
                    if state not in brewery_types_by_city:
                        brewery_types_by_city[state] = {}
                    if city not in brewery_types_by_city[state]:
                        brewery_types_by_city[state][city] = {}
                    if brewery_type not in brewery_types_by_city[state][city]:
                        brewery_types_by_city[state][city][brewery_type] = 0
                    brewery_types_by_city[state][city][brewery_type] += 1

        return brewery_types_by_city
    
    def getBreweriesWithWebsites(self, target_states):
        breweries_with_websites = {}
        data = self.fetchData()

        if data and isinstance(data, list):
            for brewery in data:
                if 'state' in brewery and brewery['state'] in target_states and 'website_url' in brewery:
                    state = brewery['state']
                    city = brewery['city']
                    if state not in breweries_with_websites:
                        breweries_with_websites[state] = {}
                    if city not in breweries_with_websites[state]:
                        breweries_with_websites[state][city] = []
                    breweries_with_websites[state][city].append(brewery['name'])

        return breweries_with_websites


brewery_url = "https://api.openbrewerydb.org/breweries"
breweryObj = BreweryList(brewery_url)

# List of states to filter breweries
target_states = ["Alaska", "Maine", "New York"]

# Fetching and printing the names of breweries in the specified states
breweries_in_states = breweryObj.getBreweriesInStates(target_states)
for state, breweries in breweries_in_states.items():
    print(f"\nBreweries in {state}:")
    for brewery in breweries:
        print(brewery)

# Fetching and printing the count of breweries in each specified state
breweries_count_by_state = breweryObj.getBreweriesInStates(target_states)
for state, count in breweries_count_by_state.items():
    print(f"\n{state}: {count} breweries")
    
# Count the number of types of breweries in individual cities of the specified states
brewery_types_by_city = breweryObj.getBreweryTypesByCity(target_states)

# Print the count of types of breweries in each city of the specified states
for state, city_types in brewery_types_by_city.items():
    print(f"\n{state}:")
    for city, types_count in city_types.items():
        print(f"  {city}: {types_count} types of breweries")

# Count and list how many breweries have websites in the specified states
breweries_with_websites = breweryObj.getBreweriesWithWebsites(target_states)
print("\nBreweries with Websites:")
print(breweries_with_websites)

#Output- Breweries in Alaska: ; Breweries in Maine: ; Breweries in New York: 12 Gates Brewing Company, 16 Stone Brewpub;     Alaska: [] breweries;  Maine: [] breweries; New York: ['12 Gates Brewing Company', '16 Stone Brewpub'] breweries;    New York:  Williamsville: {'brewpub': 1} types of breweries,  Holland Patent: {'brewpub': 1} types of breweries;     Breweries with Websites:{'New York': {'Williamsville': ['12 Gates Brewing Company'], 'Holland Patent': ['16 Stone Brewpub']}}