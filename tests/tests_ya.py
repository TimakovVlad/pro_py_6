from unittest import TestCase
import Ya

class TestsYa(TestCase):
    def test_create_folder_in_ya(self):
        try:
            self.assertEqual(Ya.create_folder_in_ya(Ya.TOKEN_YA).status_code, 201) # Папка создана
        except AssertionError:
            try:
                self.assertEqual(Ya.create_folder_in_ya(Ya.TOKEN_YA).status_code, 409) # Папка уже существует
            except AssertionError:
                if Ya.create_folder_in_ya(Ya.TOKEN_YA).status_code == 401:
                    self.fail('Токен не действителен!')
