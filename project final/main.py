import requests, json



#convert -delay 100 -loop 0 *.png animated.gif

CITY ="lisboa"

response = requests.get("http://ipinfo.io/json")
if response.status_code == 200:
    data = response.json()
    CITY = data['city']

#https://openweathermap.org/current#min
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY ="f84870fb41304bd1f90b00a84349b0e2"
LANGUAGE ="pt"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric" +"&lang=pt"
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()

    main = data['main']

    visibility = data['visibility']

    temperature = main['temp']
    temp_min = main['temp_min']
    temp_max = main['temp_max']
    humidity = main['humidity']
    pressure = main['pressure']
    report = data['weather']




    print(f"{CITY:-^30}")
    print(f"Visiblidade: {visibility}")
    print(f"Temperatura: {temperature}")
    print(f"Temperatura Minima: {temp_min}")
    print(f"Temperatura Maxima: {temp_max}")
    print(f"Humidade: {humidity}")
    print(f"Pressão: {pressure}")
    print(f"Resumo: {report[0]['description']}")
    
    try:
        wind = data['wind']
        speed = wind['speed']
        deg   = wind['deg']
        print(f"Velocidade: {speed}")
        print(f"Direção: {deg}")
    except:
        print("Sem Vento")
    
    try:
        clouds = data['clouds']['all']
        print(f"Nuvens {clouds} ")
    except:
        print("Sem nuvens")
    
    try:
        rain  = data['rain']['1h']
        print(f"Chuva {rain} ")
    except:
        print("Sem chuva")
    

    
    
else:
   print("Erro ao pedir informação.")
   
#url = "https://www.google.com/search?q="+"weather"+city
#html = requests.get(url).text #.replace(" ","\n")
#f = open("save.json","w")
#f.write(str(response.json()))
#f.close()




