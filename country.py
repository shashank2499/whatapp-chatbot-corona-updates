import requests
import json
def countrycheck(country):
    api_request=requests.get("https://corona.lmao.ninja/v2/countries")
    api=json.loads(api_request.content)
    result=""
    for i in range(0,183):
        if country.lower()==api[i]["country"].lower():
            result="Country: "+str(api[i]["country"])+" "
            result+="Confirmed Cases: "+str(api[i]["cases"])+" Deaths: "+str(api[i]["deaths"])+" Recovered: "+str(api[i]["recovered"])
    if result=="":
        result="not"
    return str(result)

