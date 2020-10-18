import requests
def coronaUpdates():
    country=input('Enter country name : ')
    response = requests.get("https://coronavirus-19-api.herokuapp.com/countries/"+country)
    body=response.json()
    if(response.status_code!=400):
        print("        ",end="")
        print("Total no of cases in",body['country'],":",body['cases'])
        print("        ",end="")
        print("Today cases :",body['todayCases'])
        print("        ",end="")
        print("Deaths :",body['deaths'])
        print("        ",end="")
        print("Today Deaths :",body['todayDeaths'])
        print("        ",end="")
        print("Recovered :",body['recovered'])
        print("        ",end="")
        print("Active :",body['active'])  
        2
    else:
        print("Please enter a valid country name")    
        coronaUpdates()                                                      