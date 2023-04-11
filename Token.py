import requests

url = "https://projects.skymetweather.com/WeatherAPI/api/MahavedhData?Type=hourlydata&date=2023-02-01"

payload='username=MHITMmb&password=Mah_IT%40022023&grant_type=password'

headers = {
  'Authorization': 'Bearer 39E515NvqbyvZjc_MUhvaRvO7qQTIejVGjzQNmQAuIzELFGc_nsZHKyBONeSu4ifAz1zQvdmqSTyO2JFOun065ReFFvn76CSa5pqhCir7iy9pz-RBzSQWJ9tIrj6OAOqpGRIGTvqkFAFP37X1CTUtr9QTtBoDOi6Zy4BkXMapwE3hseqV6BmdXUY8OzfIpujQJz6UjIQhLklbLezQtw-UZPZ5OG-ZQ-zPrNHNbhJKSAZ27cCSC19haS_db5P_lSoMmA80HwO6Y-v2tdAZwFsuQ',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
