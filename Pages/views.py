from django.shortcuts import render

def weather_view(request):
    from bs4 import BeautifulSoup
    import requests

    cities = {'abastumani': 'აბასთუმანი', 'akhaltsikhe': 'ახალციხე', 'batumi': 'ბათუმი', 'bakuriani': 'ბაკურიანი',
              'bolnisi': 'ბოლნისი',
              'borjomi': 'ბორჯომი', 'gonio': "გონიო", 'gori': 'გორი', 'gudauri': 'გუდაური', 'gurjaani': 'გურჯაანი',
              'davit-gareji': 'დავით-გარეჯი',
              'zestafoni': 'ზესტაფონი', 'zugdidi': 'ზუგდიდი', 'tbilisi': 'თბილისი', 'telavi': 'თელავი',
              'tianeti': 'თიანეთი', 'lagodekhi': 'lagodekhi', 'lanchkhuti': 'ლანჩხუთი', 'manglisi': 'მანგლისი',
              'marneuli': 'მარნეული', 'mestia': 'მესტია', 'mtskheta': 'მცხეთა', 'ozurgeti': 'ოზურგეთი',
              'omalo': 'ომალო', 'oni': 'ონი', 'rustavi': 'რუსთავი',
              'sagarejo': 'საგარეჯო', 'samtredia': 'სამტრედია', 'sachkhere': 'საჩხერე', 'senaki': 'სენაკი',
              'sioni': 'სიონი', 'signagi': 'სიღნაღი', 'sukhumi': 'სოხუმი',
              'surami': 'სურამი', 'ureki': 'ურეკი', 'ushguli': 'უშგული', 'poti': 'ფოთი', 'kobuleti': 'ქობულეთი',
              'shatili': 'შატილი', 'shekvetili': 'შეკვეთილი',
              'shovi': 'შოვი', 'chokhatauri': 'ჩოხატაური', 'tskhinvali': 'ცხინვალი', 'tsinandali': 'წინანდალი',
              'tskneti': 'წყნეთი', 'chiatura': 'ჭიათურა',
              'kharagauli': 'ხარაგაული', 'khashuri': 'ხაშური', 'khobi': 'ხობი', 'kutaisi': 'ქუთაისი'}

    tempriture_array = []
    city_array = []
    day_array = []
    time_array = []
    image_url_array = []
    weather_description_array = []
    icons_array = []
    weather_data = []

    for key, value in cities.items():
        url_tbilisi = requests.get('https://amindi.ge/city/{}/{}'.format(key, value))
        soup_tbilisi = BeautifulSoup(url_tbilisi.content, 'html.parser')
        tempriture = soup_tbilisi.find('div', id='test').get_text()
        city = soup_tbilisi.find('div', class_='current_city').get_text()
        find_time = soup_tbilisi.find_all('div', class_='current_time')
        time_info = [date.get_text() for date in find_time]
        day = time_info[0]
        time = time_info[1]
        weather_description = soup_tbilisi.find('div', class_='current_phrase left').get_text()[7:]
        find_image_url = soup_tbilisi.find('div', class_='current_icon left')
        image_url = ""
        for icon in find_image_url:
            image_url += icon.get('src')
            icons_array.append(image_url)
        tempriture_array.append(tempriture)
        city_array.append(city)
        day_array.append(day)
        time_array.append(time)
        image_url_array.append(image_url)
        weather_description_array.append(weather_description)

    for  i in range(len(city_array)):
        weather_cities = {
            'city':city_array[i],
            'tempriture':tempriture_array[i],
            'description':weather_description_array[i],
            'icon': icons_array[i]
        }

        weather_data.append(weather_cities)

    return render(request, 'weather.html', {'weather_info':weather_data})
