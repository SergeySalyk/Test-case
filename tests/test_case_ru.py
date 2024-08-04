import pytest
import allure

@allure.feature('Валидация формы')
@allure.story('Поле: Ввод числа')
class TestFormValidation:

    # Позитивные тесты
    @allure.title('Проверка натуральных чисел без чекбокса "дополнительного условия"')
    @pytest.mark.priority(1)  # Высокий приоритет
    @pytest.mark.parametrize("value", [20, 21, 30, 49, 50])
    def test_natural_numbers_without_checkbox(self, value):
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является натуральным числом и попадает в диапазон от 20 до 50 включительно. Результат проверки должен быть успешным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка вещественных чисел с чекбоксом дополнительного условия')
    @pytest.mark.priority(1)  # Высокий приоритет
    @pytest.mark.parametrize("value", [20.1, 21.5, 30.8, 49.9, 50.0])
    def test_floating_point_numbers_with_checkbox(self, value):
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить' с установленным чекбоксом"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является вещественным числом и попадает в диапазон от 20 до 50 включительно. Результат проверки должен быть успешным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    # Негативные тесты
    @allure.title('Проверка целых чисел с чекбоксом дополнительного условия')
    @pytest.mark.priority(2)  # Средний приоритет
    def test_integer_numbers_with_checkbox(self):
        value = 20
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить' с установленным чекбоксом"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является целым числом, но при установленном чекбоксе дополнительного условия оно должно быть вещественным. Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка чисел ниже минимальной границы')
    @pytest.mark.priority(2)  # Средний приоритет
    def test_numbers_below_minimum(self):
        value = 19
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' ниже минимальной границы (20). Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка чисел выше максимальной границы')
    @pytest.mark.priority(2)  # Средний приоритет
    def test_numbers_above_maximum(self):
        value = 51
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' выше максимальной границы (50). Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка отрицательных чисел')
    @pytest.mark.priority(2)  # Средний приоритет
    def test_negative_numbers(self):
        value = -10
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является отрицательным числом. Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка значения ноль')
    @pytest.mark.priority(2)  # Средний приоритет
    def test_zero_value(self):
        value = 0
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является нулем, что недопустимо в данном контексте. Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка вещественного числа ниже минимальной границы с чекбоксом')
    @pytest.mark.priority(2)  # Средний приоритет
    def test_floating_point_below_minimum(self):
        value = 19.9
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить' с установленным чекбоксом"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является вещественным числом, но ниже минимальной границы (20). Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка вещественного числа с точкой и запятой')
    @pytest.mark.priority(3)  # Низкий приоритет
    @pytest.mark.parametrize("value", ["20.5", "20,5"])
    def test_floating_point_with_dot_and_comma(self, value):
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить' с установленным чекбоксом"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является вещественным числом с точкой. Если запятая используется, результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка ввода строки')
    @pytest.mark.priority(3)  # Низкий приоритет
    def test_string_input(self):
        value = "abc"
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = f"Ожидается, что значение '{value}' является строкой и не может быть принято как числовое значение. Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка пустого поля')
    @pytest.mark.priority(3)  # Низкий приоритет
    def test_empty_field(self):
        value = ""
        with allure.step(f"Оставьте поле 'Число' пустым и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = "Ожидается, что пустое значение в поле 'Число' не будет принято и результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка числа с чрезмерным количеством цифр')
    @pytest.mark.priority(3)  # Низкий приоритет
    def test_excessive_digits(self):
        value = "1000000"
        with allure.step(f"Введите значение '{value}' в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = "Ожидается, что значение '{value}' содержит слишком много цифр. Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверка предела символов в поле')
    @pytest.mark.priority(3)  # Низкий приоритет
    def test_field_character_limit(self):
        value = "1" * 100
        with allure.step(f"Введите очень длинное значение в поле 'Число' и нажмите 'Проверить'"):
            # Описание ожидаемого результата
            expected_result = "Ожидается, что значение '{value}' превышает допустимый предел символов. Результат проверки должен быть ошибочным."
            allure.attach(body=expected_result, name="Ожидаемый результат", attachment_type=allure.attachment_type.TEXT)
