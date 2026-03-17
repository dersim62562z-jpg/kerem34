import requests

def hava_durumu_getir(sehir, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": sehir,
        "appid": api_key,
        "lang": "tr",
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        veri = response.json()
        print(f"\n{sehir.title()} için hava durumu:")
        print(f"Sıcaklık: {veri['main']['temp']}°C")
        print(f"Durum: {veri['weather'][0]['description']}")
        print(f"Nem: %{veri['main']['humidity']}")
        print(f"Rüzgar Hızı: {veri['wind']['speed']} m/s")
    except requests.exceptions.RequestException as e:
        print("İstek sırasında hata oluştu:", e)
    except KeyError:
        print("Şehir bulunamadı veya API cevabı beklenmedik.")

def main():
    api_key = "09e582fd92990258625bab40b2c43de0 " # Buraya kendi API anahtarınızı girin!
    sehir = input("Hava durumunu öğrenmek istediğiniz şehir: ")
    hava_durumu_getir(sehir, api_key)

if __name__ == "__main__":
    main()