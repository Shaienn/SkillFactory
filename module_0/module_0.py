#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали
        
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали        

def game_core_v3(number):
    '''
    Начальный диапазон поиска включает весь диапазон доступных значений. Проверяем больше или меньше загаданное
    число середины диапазона. На основе полученной информации уточняем нижнюю и верхнюю границы диапазона.
    
    Функция принимает загаданное число и возвращает число попыток
    '''
    count = 1
    max_range = 101
    min_range = 1
 
    while True:
        predict = min_range + ((max_range - min_range) // 2)
        count+=1
        
        if number == predict:
            break
        
        if (number < predict) and (max_range > predict):
            max_range = predict
        if (number > predict) and (min_range < predict):
            min_range = predict
    
    return(count) # выход из цикла, если угадали     
        

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)

