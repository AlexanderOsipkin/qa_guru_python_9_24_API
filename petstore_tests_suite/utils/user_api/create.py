import allure
import requests
import json

from petstore_tests_suite.utils import allure_attach
from pydantic import ValidationError
from petstore_tests_suite.basemodels.user import user_create


def create(api_url, headers):
    with allure.step('Создаем пользователя'):
        method = 'POST'
        endpoint = '/v2/user/'
        try:
            with allure.step('Собираем полезную нагрузку'):
                create_user_request = user_create.CreateUserRequest.parse_raw(
                    user_create.input_json
                ).json()
                allure_attach.request_body(create_user_request)
                user_data = json.loads(user_create.input_json)

            with allure.step(
                f'Отправить {method} запрос на {endpoint} для создания пользователя'
            ):
                response = requests.request(
                    method=method,
                    url=f'{api_url}{endpoint}',
                    headers=headers,
                    data=create_user_request,
                )
                create_user_response_json = response.json()
                allure_attach.response_body(create_user_response_json)

            with allure.step('Проверяем, что API возвращает 200 код ответа'):
                allure_attach.response_code(str(response.status_code))

                assert response.status_code == 200, (
                    f'User creation error. Response code: {response.status_code}.'
                    f'Response body: {response.json()}'
                )

            with allure.step('Валидация типов данных полученного тела ответа'):
                try:
                    user_create.CreateUserResponse(
                        code=create_user_response_json['code'],
                        type=create_user_response_json['type'],
                        message=create_user_response_json['message'],
                    )

                except ValidationError as e:
                    with allure.step(f'Валидация типов данных не прошла, ошибка: {e}'):
                        raise Exception(
                            f'Валидация типов данных не прошла, ошибка: {e}'
                        )

            return user_data

        except requests.ConnectionError as e:
            with allure.step(f'API connection error: {e}'):
                raise Exception(f'API connection error: {e}')
