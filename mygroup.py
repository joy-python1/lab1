import statistics

groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5],
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4],
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5],
    },
    {
        "name": "Ирина",
        "surname": "Краснова",
        "exams": ["Линейная алгебра", "ЭЭиС", "ИС"],
        "marks": [5, 3, 4],
    },
    {
        "name": "Сергей",
        "surname": "Александров",
        "exams": ["КТП", "ОБЖ", "ЭЭиС"],
        "marks": [3, 3, 4],
    },
    {
        "name": "Анна",
        "surname": "Москвина",
        "exams": ["АиГ", "Информатика", "ИС"],
        "marks": [4, 5, 4],
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


def filter_by_avg(average_mark):
    return [student for student in groupmates if statistics.mean(student["marks"]) > average_mark]


def get_students_by_avg(average_mark):
    return print_students(filter_by_avg(average_mark))


get_students_by_avg(int(input("Введите среднее значение оценки: ")))
