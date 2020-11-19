import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm

tqdm.pandas()

def geo_locator(user_location):
    
    # initialize geolocator
    geolocator = Nominatim(user_agent='Tweet_locator')

    if user_location is not None:
        try :
            # get location
            location = geolocator.geocode(user_location, language='en')
            # get coordinates
            location_exact = geolocator.reverse(
                        [location.latitude, location.longitude], language='en')
            # get country codes
            c_code = location_exact.raw['address']['country_code']

            return c_code

        except:
            return None

    else : 
        return None



result = pd.read_csv('full_gnd.csv')

# apply geo locator to user-location
loc = result['location'].progress_apply(geo_locator)
result['user-country_code'] = loc

result.to_csv('gnd_withloc.csv')
