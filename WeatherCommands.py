#https://github.com/csparpa/pyowm

import pyowm
owm = pyowm.OWM('665d0497ac66c8c8cfd2178807d07f57')

commandlist = [['+wn', 'get current weather. Accepts zip codes (US only) or places (format: city,country)']]

def help():
    output = ""
    for entry in commandlist:
          output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output

def current_weather_z(zip, country='us', unit='fahrenheit'):
    zip = zip.strip()
    
    observation = owm.weather_at_zip_code(zip,country)
    w = observation.get_weather()
    
    temperature = w.get_temperature(unit)
    status = w.get_status()
    location = observation.get_location()
    name = location.get_name() + ', ' + location.get_country()
    
    out = '''
    Showing information for: **%s**!
The temperature right now is: **%s**°F
The weather status is: **%s**
Today's low is **%s**°F and the high for today is going to be **%s**°F :smile:
	''' % (name,temperature['temp'],status,temperature['temp_min'],temperature['temp_max'])
    return out

def current_weather_p(location):
    
    location = location.lower().strip().split(',')
    city,country = location[0],location[1]
    
    observation = owm.weather_at_place('%s,%s' % (city,country))
    w = observation.get_weather()
    
    location = observation.get_location()
    name = location.get_name() + ', ' + location.get_country()
    
    if location.get_country().lower() == 'us':
        unit = 'fahrenheit'
        temperature = w.get_temperature(unit)
        status = w.get_status()
        
        out = '''
    Showing information for: **%s**!
The temperature right now is: **%s**°F
The weather status is: **%s**
Today's low is **%s**°F and the high for today is going to be **%s**°F :smile:
	''' % (name,temperature['temp'],status,temperature['temp_min'],temperature['temp_max'])
        
        
    else:
        unit = 'celsius'
        temperature = w.get_temperature(unit)
        status = w.get_status()
        
        out = '''
    Showing information for: **%s**!
The temperature right now is: **%s**°C
The weather status is: **%s**
Today's low is **%s**°C and the high for today is going to be **%s**°C :smile:
	''' % (name,temperature['temp'],status,temperature['temp_min'],temperature['temp_max'])
        
    return out