# Пример с одной переменной
team1_num = 5
team1_str = "В команде Мастера кода участников: %d !" % team1_num
print(team1_str)

# Пример с двумя переменными
team1_num = 5
team2_num = 6
teams_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(teams_str)

# Пример с переменной score_2
score_2 = 42
score_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(score_str)

# Пример с переменной team1_time
team1_time = 18015.2
time_str = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(time_str)

# Пример с двумя переменными score_1 и score_2
score_1 = 40
score_2 = 42
tasks_str = f"Команды решили {score_1} и {score_2} задач."
print(tasks_str)

# Пример с переменными challenge_result, tasks_total и time_avg
challenge_result = "победа команды Мастера кода!"
tasks_total = 82
time_avg = 350.4
result_str = f"Результат битвы: {challenge_result}\nСегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(result_str)