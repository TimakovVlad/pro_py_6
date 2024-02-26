from unittest import TestCase
import main, main_2, main_3


class TestMain(TestCase):
    def test_prepods_in(self):
        self.assertEqual(len(main.res), 6)
        self.assertEqual(main.res[0], ['Антон', 'Евгений', 'Максим'])
        self.assertEqual(main.res[1], ['Александр', 'Евгений', 'Елена', 'Кирилл', 'Максим', 'Олег', 'Роман'])

class TestMain_2(TestCase):
    def test_durations(self):
        self.assertEqual(len(main_2.res), 4)
        self.assertEqual(main_2.res[0], 12)
        self.assertEqual(main_2.res[1], 14)
        self.assertEqual(main_2.res[2], 20)
        self.assertEqual(main_2.res[3], 20)

class TestMain_3(TestCase):
    def test_same_name(self):
        self.assertGreater(len(main_3.all_same), 3)
        self.assertEqual(main_3.all_same['Java-разработчик с нуля'], ['Иван Бочаров', 'Иван Маркитан', 'Максим Батырев', 'Максим Воронцов', 'Сергей Индюков', 'Сергей Сердюк'])
        self.assertEqual(main_3.all_same['Fullstack-разработчик на Python'], ['Александр Бардин', 'Александр Иванов', 'Александр Ульянцев', 'Александр Шлейко', 'Евгений Шек', 'Евгений Шмаргунов'])