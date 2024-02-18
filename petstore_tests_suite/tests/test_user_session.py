import allure

from petstore_tests_suite.utils.user_api.create import create
from petstore_tests_suite.utils.user_api.login import login
from petstore_tests_suite.utils.user_api.logout import logout


@allure.epic('User API')
@allure.story('Session')
class TestUserSession:
    @allure.title('User login')
    @allure.feature('Authentication API')
    @allure.label('microservice', 'API')
    @allure.label('owner', 'Alexander Osipkin')
    @allure.tag('smoke', 'regress', 'API', 'critical')
    @allure.severity('critical')
    def test_user_login(self, api_url, headers):
        user_data = create(api_url, headers)
        login(
            api_url,
            headers,
            username=user_data['username'],
            password=user_data['password'],
        )

    @allure.title('User logout')
    @allure.feature('User logout API')
    @allure.label('microservice', 'API')
    @allure.label('owner', 'Alexander Osipkin')
    @allure.tag('smoke', 'regress', 'API', 'critical')
    @allure.severity('critical')
    def test_user_logout(self, api_url, headers):
        logout(api_url, headers)
