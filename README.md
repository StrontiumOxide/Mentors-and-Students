# Домашние задание к лекции "Объекты и классы. Инкапсуляция, наследование и полиморфизм"
## Задание №1. Наследование
В этом задании были созданы от родительского класса Mentor два дочерних пустых класса: Lecturer и Reviewer.
## Задание №2. Атрибуты и взаимодействия классов
В этом задании была добавлена возможность студентам оценивать лекции, проводимые лекторами, а эксперты могут только давать оценки студентам. Так же было добавлено условие, чтобы оценка была в диапозоне от 0 до 10, иначе возвращать ошибку.
## Задание №3. Полиморфизм и магические методы
Для этого задания было принято решение для классов создать отдельный файл cls.py. Все операции производить в файле main.py. Была произведена перегрузка магического метода __str__ у всех классов. Для расчёта средней оценки по всем предметам была реализована отдельная функция average_grade. Была написана простая программа, которая выставляет случайные оценки двум лекторам студентами и студентам экспертом. Реализовано сравнение лекторов и студентов между средними оценками соответственно.
## Задание №4. Полевые испытания
В этом коммите экземпляры классов хранятся в списках. Вложенные циклы созданы для того чтобы добавить студентов, лекторов, экспертов на курсы и добавления оценок соответстующим классам. Были реализованы две функции. Первая для расчёта средней оценки по домашнему заданию среди студентов предалах одного курса, вторая для расчёта средней оценки по лекциям среди лекторов в пределах одного курса.