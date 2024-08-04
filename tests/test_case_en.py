import pytest
import allure

@allure.feature('Form Validation')
@allure.story('Field: Number Input')
class TestFormValidation:

    # Positive tests
    @allure.title('Check natural numbers without the "additional condition" checkbox')
    @pytest.mark.priority(1)  # High priority
    @pytest.mark.parametrize("value", [20, 21, 30, 49, 50])
    def test_natural_numbers_without_checkbox(self, value):
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check'"):
            expected_result = f"Value '{value}' is expected to be a natural number within the range of 20 to 50 inclusive. The check result should be successful."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check floating-point numbers with the additional condition checkbox')
    @pytest.mark.priority(1)  # High priority
    @pytest.mark.parametrize("value", [20.1, 21.5, 30.8, 49.9, 50.0])
    def test_floating_point_numbers_with_checkbox(self, value):
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check' with the checkbox selected"):
            expected_result = f"Value '{value}' is expected to be a floating-point number within the range of 20 to 50 inclusive. The check result should be successful."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    # Negative tests
    @allure.title('Check integer numbers with the additional condition checkbox')
    @pytest.mark.priority(2)  # Medium priority
    def test_integer_numbers_with_checkbox(self):
        value = 20
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check' with the checkbox selected"):
            expected_result = f"Value '{value}' is expected to be an integer, but with the additional condition checkbox selected, it should be a floating-point number. The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check numbers below the minimum boundary')
    @pytest.mark.priority(2)  # Medium priority
    def test_numbers_below_minimum(self):
        value = 19
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check'"):
            expected_result = f"Value '{value}' is expected to be below the minimum boundary (20). The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check numbers above the maximum boundary')
    @pytest.mark.priority(2)  # Medium priority
    def test_numbers_above_maximum(self):
        value = 51
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check'"):
            expected_result = f"Value '{value}' is expected to be above the maximum boundary (50). The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check negative numbers')
    @pytest.mark.priority(2)  # Medium priority
    def test_negative_numbers(self):
        value = -10
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check'"):
            expected_result = f"Value '{value}' is expected to be a negative number. The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check zero value')
    @pytest.mark.priority(2)  # Medium priority
    def test_zero_value(self):
        value = 0
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check'"):
            expected_result = f"Value '{value}' is expected to be zero, which is not allowed in this context. The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check floating-point number below minimum boundary with checkbox')
    @pytest.mark.priority(2)  # Medium priority
    def test_floating_point_below_minimum(self):
        value = 19.9
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check' with the checkbox selected"):
            expected_result = f"Value '{value}' is expected to be a floating-point number but below the minimum boundary (20). The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check floating-point number with dot and comma')
    @pytest.mark.priority(3)  # Low priority
    @pytest.mark.parametrize("value", ["20.5", "20,5"])
    def test_floating_point_with_dot_and_comma(self, value):
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check' with the checkbox selected"):
            expected_result = f"Value '{value}' is expected to be a floating-point number with a dot. If a comma is used, the check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check string input')
    @pytest.mark.priority(3)  # Low priority
    def test_string_input(self):
        value = "abc"
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check'"):
            expected_result = f"Value '{value}' is expected to be a string and cannot be accepted as a numerical value. The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check empty field')
    @pytest.mark.priority(3)  # Low priority
    def test_empty_field(self):
        value = ""
        with allure.step(f"Leave the 'Number' field empty and click 'Check'"):
            expected_result = "An empty value in the 'Number' field is expected to be rejected, and the check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check number with excessive digits')
    @pytest.mark.priority(3)  # Low priority
    def test_excessive_digits(self):
        value = "1000000"
        with allure.step(f"Enter value '{value}' in the 'Number' field and click 'Check'"):
            expected_result = "Value '{value}' is expected to contain too many digits. The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)

    @allure.title('Check field character limit')
    @pytest.mark.priority(3)  # Low priority
    def test_field_character_limit(self):
        value = "1" * 100
        with allure.step(f"Enter a very long value in the 'Number' field and click 'Check'"):
            expected_result = "Value '{value}' is expected to exceed the allowed character limit. The check result should be erroneous."
            allure.attach(body=expected_result, name="Expected Result", attachment_type=allure.attachment_type.TEXT)
