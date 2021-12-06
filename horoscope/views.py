from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

zodiac_dict = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
               "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
               "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
               "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
               "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
               "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
               "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
               "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
               "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
               "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
               "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
               "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
               }

zodiac_day = {1: {tuple(range(1, 21)): "capricorn", tuple(range(21, 32)): "aquarius"},
              2: {tuple(range(1, 20)): "aquarius", tuple(range(20, 29)): "pisces"},
              3: {tuple(range(1, 21)): "pisces", tuple(range(21, 32)): "aries"},
              4: {tuple(range(1, 21)): "aries", tuple(range(21, 31)): "taurus"},
              5: {tuple(range(1, 22)): "taurus", tuple(range(22, 32)): "gemini"},
              6: {tuple(range(1, 22)): "gemini", tuple(range(22, 31)): "cancer"},
              7: {tuple(range(1, 23)): "cancer", tuple(range(23, 32)): "leo"},
              8: {tuple(range(1, 22)): "leo", tuple(range(22, 32)): "virgo"},
              9: {tuple(range(1, 24)): "virgo", tuple(range(24, 31)): "libra"},
              10: {tuple(range(1, 24)): "libra", tuple(range(24, 32)): "scorpio"},
              11: {tuple(range(1, 23)): "scorpio", tuple(range(23, 31)): "sagittarius"},
              12: {tuple(range(1, 23)): "sagittarius", tuple(range(23, 32)): "capricorn"}
              }

types_dict = {'fire': ["aries", "leo", "sagittarius"],
              'earth': ["taurus", "virgo", "capricorn"],
              'air': ["gemini", "libra", "aquarius"],
              'water': ["cancer", "scorpio", "pisces"]}


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


def type_window(request):
    types = list(types_dict)
    context = {
        'types': types
    }
    return render(request, 'horoscope/type_window.html', context=context)


def type_element(request, element):
    description_element = types_dict.get(element, None)
    context = {
        'description_element': description_element,
        'element': element
    }
    return render(request, 'horoscope/type_element.html', context=context)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'sign_name': description.split()[0],
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Зодиака под порядковым номером - {sign_zodiac} не существует')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month: int, day: int):
    if 0 < month < 13:
        date_month = zodiac_day[month]
        for i in date_month:
            if day in i:
                name_zodiac = zodiac_day[month][i]
                redirect_url = reverse('horoscope-name', args=[name_zodiac])
                return HttpResponseRedirect(redirect_url)
        return HttpResponseNotFound(
            f'Дня с порядковым номером {day} в этом месяце под порядковым номером {month} не существует')
    else:
        return HttpResponseNotFound(f'Месяца с порядковым номером {month} не существует')
