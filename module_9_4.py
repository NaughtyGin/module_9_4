from random import choice  # для метода __call__


# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)


# Замыкание:
def get_advanced_writer(file_name):
    if isinstance(file_name, str) and file_name[-4:] == ".txt":
        file_ = open(file_name, 'w', encoding='utf-8')  # Обнуление файла при повторных запусках кода
        file_.close()

        def write_everything(*data_set):
            for i in data_set:
                with open(file_name, 'a+', encoding='utf-8') as file:
                    file.write(f'{i}\n')
        return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# write((3, 4, 5))
# write(6, 7, 8)


# Метод __call__:
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
