import allure

from petstore_tests_suite.utils.user_api.create import create
from petstore_tests_suite.utils.user_api.get_user_by_username import (
    get_user_by_username,
)
from petstore_tests_suite.utils.user_api.create_user_with_input_array import (
    create_user_with_input_array,
)
from petstore_tests_suite.utils.user_api.create_user_with_input_list import (
    create_user_with_input_list,
)


@allure.epic('User API')
@allure.story('Create user')
class TestCreateUser:
    @allure.title('Create one user')
    @allure.feature('User create API')
    @allure.label('microservice', 'API')
    @allure.label('owner', 'Alexander Osipkin')
    @allure.tag('smoke', 'regress', 'API', 'critical')
    @allure.severity('critical')
    def test_create_user(self):
        username = create()
        get_user_by_username(username=username['username'])

    @allure.title('Create many users with input array')
    @allure.feature('Create user with array API')
    @allure.label('microservice', 'API')
    @allure.label('owner', 'Alexander Osipkin')
    @allure.tag('regress', 'API', 'critical')
    @allure.severity('critical')
    def test_create_user_with_input_array(self):
        username = create_user_with_input_array()
        get_user_by_username(username=username[0]['username'])
        get_user_by_username(username=username[1]['username'])

    @allure.title('Create many users with input list')
    @allure.feature('Create user with list API')
    @allure.label('microservice', 'API')
    @allure.label('owner', 'Alexander Osipkin')
    @allure.tag('regress', 'API', 'critical')
    @allure.severity('critical')
    def test_create_user_with_input_list(self):
        username = create_user_with_input_list()
        get_user_by_username(username=username[0]['username'])
        get_user_by_username(username=username[1]['username'])
