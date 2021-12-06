from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

todo_week_day = {'monday': 'Список дел на понедельник', 'tuesday': 'Список дел на вторник',
                 'wednesday': 'Список дел на вторник', 'thursday': 'Список дел на четверг',
                 'friday': 'Список дел на пятницу', 'saturday': 'Список дел на субботу',
                 'sunday': 'Список дел на воскресенье'}

def get_todo_week_every_day_by_number(request, sign_day: int):
    days = list(todo_week_day)
    if sign_day > len(days):
        return HttpResponseNotFound(f'Неверный номер дня - {sign_day}')
    name_day = days[sign_day - 1]
    redirect_url = reverse('week-name', args=[name_day])
    return HttpResponseRedirect(redirect_url)


def todo_week_every_day(requests, sign_day: str):
    description = todo_week_day.get(sign_day, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Такого дня недели, как {sign_day} не существует')


