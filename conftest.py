import datetime

import allure
import pytest

from utils.create_driver import create_driver


@pytest.fixture(scope="function")
def driver(request):
    app_activity = request.node.get_closest_marker("app_activity")
    if app_activity:
        driver = create_driver(app_activity.args[0])
    else:
        driver = create_driver()

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call' and result.failed:
        if 'driver' in item.fixturenames and call.excinfo is not None:
            browser = item.funcargs['driver']
            allure.attach(
                browser.get_screenshot_as_png(),
                name=f'screenshot_{datetime.datetime.now()}',
                attachment_type=allure.attachment_type.PNG
            )
