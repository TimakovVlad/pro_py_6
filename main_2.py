# Коллекция данных. Словари.
# Наводим порядок: упорядочиваем курсы по продолжительности

courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
mentors = [
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]

courses_list = []
for course, mentor, duration in zip(courses, mentors, durations):
	course_dict = {"title":course, "mentors":mentor, "duration":duration}
	courses_list.append(course_dict)

durations_dict = {}

for id, item in enumerate(courses_list):
	key = item["duration"]
	if key not in durations_dict:
		durations_dict[key] = [id]
	else:
		durations_dict[key].append(id)

durations_dict = dict(sorted(durations_dict.items()))

res = []
for key, value in durations_dict.items():
	if len(value) > 1:
		for i in value:
			print(f'{courses_list[i]["title"]} - {durations[i]} месяцев')
			res.append(durations[i])
	else:
		print(f'{courses_list[value[0]]["title"]} - {durations[value[0]]} месяцев')
		res.append(durations[value[0]])