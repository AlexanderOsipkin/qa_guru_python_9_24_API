import allure

from petstore_tests_suite.utils.user_api.create import create
from petstore_tests_suite.utils.user_api.get_user_by_username import (
    get_user_by_username,
)


@allure.epic('User API')
@allure.story('Get user')
@allure.title('Get user')
@allure.feature('Get user API')
@allure.label('microservice', 'API')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'API', 'normal')
@allure.severity('normal')
def test_get_user_by_username():
    username = create()
    get_user_by_username(username=username['username'])
