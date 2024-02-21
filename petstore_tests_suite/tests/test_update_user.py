import allure

from petstore_tests_suite.utils.user_api.create import create
from petstore_tests_suite.utils.user_api.update import update
from petstore_tests_suite.utils.user_api.get_user_by_username import (
    get_user_by_username,
)


@allure.epic('User API')
@allure.story('Update user')
@allure.title('Update user')
@allure.feature('Update user API')
@allure.label('microservice', 'API')
@allure.label('owner', 'Alexander Osipkin')
@allure.tag('regress', 'API', 'normal')
@allure.severity('normal')
def test_update_user():
    user_data = create()
    update_user_data = update(username=user_data['username'])
    get_user_by_username(username=update_user_data['username'])
