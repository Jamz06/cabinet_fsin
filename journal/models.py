
from django.db import models

# Create your models here.


class Schedule(models.Model):
    '''
    Класс рассписания
    '''


class Card(models.Model):
    ''' 
    Клас таксофонной карты
    '''
    # Номер карты 8 знаков
    card_number = models.CharField('Номер карты', max_length=8, primary_key=True) 

    fam = models.CharField('Фамилия')
    name = models.CharField('Имя')
    otch = models.CharField('Отчество')

    #Кол-во разрешенных номеров. Макс 99
    granted_num_count = models.IntegerField(max_length=2)

    schedule = models.OneToOneField(Schedule)

    block = models.BooleanField("Блокирована?")

class GrantedNum(models.Model):
    '''
    Класс разрешенного номера. относится один ко многим к таблице Card
    '''
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    number = models.CharField(max_length=18)

    fam = models.CharField('Фамилия')
    name = models.CharField('Имя')
    otch = models.CharField('Отчество')

    RELATION = (
        ('1', 'Муж'),
        ('2', 'Жена'),
        ('3', 'Бабушка'),
        ('4', 'Дед'),
        ('5', 'Брат'),
        ('6', 'Сестра'),
        ('7', 'Отец'),
        ('8', 'Мать'),
        ('9', 'Дочь'),
        ('10', 'Сын'),
        ('11', 'Знакомый(ая)'),
        ('12', 'Адвокат'),
        ('13', 'Другое'),
    )

    relation = models.IntegerField(max_length=2, choices=RELATION)


