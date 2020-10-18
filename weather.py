import requests
def weatherReport():
    city=input('Enter city name : ')
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=imperial&appid=0941ecd2acfb0f26b09f7b3ddbb438cf")
    body=response.json()
    if(body["cod"]!='404'):
        print("**** This is the weather report in",body['name'],"****")
        print("        ",end="")
        print("City name :",body["name"])
        print("        ",end="")
        print("Minimun Temperature :",body['main']['temp_min'],"°F")
        print("        ",end="")
        print("Maximum Temperature :",body['main']['temp_max'],"°F")
        print("        ",end="")
        print("Humidity :",body["main"]["humidity"]) 
        print("        ",end="")
        print("Pressure :",body["main"]["pressure"]) 
        print("        ",end="")
        print("Description :",body['weather'][0]['description']) 
        print()   
    else:
        print("Please enter a valid city name")  
        weatherReport()                                                             