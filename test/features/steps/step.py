from behave import given, when, then
import requests
import json


@given('a url')
def step_impl(context):
    path = '1/'
    context.url = context.base_url + path


@when('you visit the site')
def get_request(context):
    context.response = requests.get(context.url)


@then('you should get a status code of 200')
def check_status_code(context):
    assert context.response.status_code == 200

