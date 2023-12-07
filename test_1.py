from TestPage import OperationHelper, TestSearchLocator
import yaml
import logging
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test 1 - Star')
    test_page = OperationHelper(browser, testdata['address'])
    test_page.go_to_site()
    test_page.filling_field(testdata['failed_login'], TestSearchLocator.LOCATOR_LOGIN_FIELD)
    test_page.filling_field(testdata['failed_passwd'], TestSearchLocator.LOCATOR_PASS_FIELD)
    test_page.click_button('Login', TestSearchLocator.LOCATOR_LOGIN_BTN)
    assert test_page.get_error_text() == '401'
    logging.info('Test 1 - Finish')


def test_step2(browser):
    logging.info('Test 2 - Star')
    test_page = OperationHelper(browser, testdata['address'])
    test_page.go_to_site()
    test_page.filling_field(testdata['login'], TestSearchLocator.LOCATOR_LOGIN_FIELD)
    test_page.filling_field(testdata['passwd'], TestSearchLocator.LOCATOR_PASS_FIELD)
    test_page.click_button('Login', TestSearchLocator.LOCATOR_LOGIN_BTN)
    assert test_page.get_text_blog() == 'Blog'
    logging.info('Test 2 - Finish')


def test_step3(browser):
    logging.info('Test 3 - Star')
    test_page = OperationHelper(browser, testdata['address'])
    test_page.go_to_site()
    test_page.filling_field(testdata['login'], TestSearchLocator.LOCATOR_LOGIN_FIELD)
    test_page.filling_field(testdata['passwd'], TestSearchLocator.LOCATOR_PASS_FIELD)
    test_page.click_button('Login', TestSearchLocator.LOCATOR_LOGIN_BTN)
    test_page.click_button('Create post', TestSearchLocator.LOCATOR_CREATE_NEW_BLOG_BTN)
    test_page.filling_field(testdata['title_new_post'], TestSearchLocator.LOCATOR_NEW_TITLE)
    test_page.filling_field(testdata['description_new_post'], TestSearchLocator.LOCATOR_NEW_DESCRIPTION)
    test_page.filling_field(testdata['content_new_post'], TestSearchLocator.LOCATOR_NEW_CONTENT)
    test_page.filling_field(testdata['date_created'], TestSearchLocator.LOCATOR_DATE_CREATE_POST)
    test_page.click_button('Save', TestSearchLocator.LOCATOR_SAVE_BTN)
    time.sleep(2)
    assert test_page.get_title_new_post() == testdata['title_new_post']
    logging.info('Test 3 - Finish')


def test_step4(browser):
    logging.info('Test 4 - Star')
    test_page = OperationHelper(browser, testdata['address'])
    test_page.go_to_site()
    test_page.filling_field(testdata['login'], TestSearchLocator.LOCATOR_LOGIN_FIELD)
    test_page.filling_field(testdata['passwd'], TestSearchLocator.LOCATOR_PASS_FIELD)
    test_page.click_button('Login', TestSearchLocator.LOCATOR_LOGIN_BTN)
    test_page.click_button('Contact', TestSearchLocator.LOCATOR_CONTACT_BTN)
    time.sleep(2)
    assert test_page.get_title_contact_us() == 'Contact us!'
    logging.info('Test 4 - Finish')


def test_step5(browser):
    logging.info('Test 5 - Star')
    test_page = OperationHelper(browser, testdata['address'])
    test_page.go_to_site()
    test_page.filling_field(testdata['login'], TestSearchLocator.LOCATOR_LOGIN_FIELD)
    test_page.filling_field(testdata['passwd'], TestSearchLocator.LOCATOR_PASS_FIELD)
    test_page.click_button('Login', TestSearchLocator.LOCATOR_LOGIN_BTN)
    test_page.click_button('Contact', TestSearchLocator.LOCATOR_CONTACT_BTN)
    time.sleep(2)
    test_page.filling_field(testdata['your_name_new'], TestSearchLocator.LOCATOR_NAME_CONTACT_FIELD)
    test_page.filling_field(testdata['email_new'], TestSearchLocator.LOCATOR_EMAIL_CONTACT_FIELD)
    test_page.filling_field(testdata['content_new_contact'], TestSearchLocator.LOCATOR_CONTENT_CONTACT_FIELD)
    test_page.click_button('CONTACT US', TestSearchLocator.LOCATOR_CONTACT_US_BTN)
    time.sleep(2)
    assert test_page.get_alert_message() == testdata['message_alert']
    logging.info('Test 5 - Finish')
