from django.shortcuts import render
import datetime
today = datetime.date.today()
def info (requsts):
    dict ={
        'title': 'Info',
        'Text': 'Этот cайт для просмотра новостей и другой разной информации'
    }
    return render(requsts, 'page1.html', context=dict)
def info1 (requests):
    dict ={
        'title': 'Info1',
        'Text': 'Правила использувание сайта нельзя под новостями писать внимательно читайте, что запрещено писать в комментариях:\n'
                ' - Оскорбление наций и стран \n '
                '- Оскорбление человека \n'
                '- Разводить политосрач, быть инициатором этого '
    }
    return render(requests, 'page2.html', context=dict)
def info2 (requests):
    dict ={
        'title': 'Info2',
        'Text': f'Первый бан будет длится 24 часа \n'
                'Второй бан будет длится 7 дней \n'
                'Третий бан будет длится 30 дней'
                f'\nВремя: {today}'
    }
    return render(requests, 'page3.html', context=dict)