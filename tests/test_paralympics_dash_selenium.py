import time

import requests
from dash.testing.application_runners import import_app


def test_server_live(dash_duo):
    """
    GIVEN the app is running
    WHEN a HTTP request to the home page is made
    THEN the HTTP response status code should be 200
    """
    # Create the app
    app = import_app(app_file="paralympics_dash.paralympics_dash")

    # Start the app in a server
    dash_duo.start_server(app)

    # Delay to wait for the page to load
    time.sleep(2)

    print(f'server url {dash_duo.server_url}')
    response = requests.get("http://127.0.0.1:8050/")
    assert response.status_code == 200


def test_home_h1textequals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the page title should be
    """
    # Create the app
    app = import_app(app_file="paralympics_dash.paralympics_dash")

    # Start the app in a server
    dash_duo.start_server(app)

    # Delay to wait for the page to load
    time.sleep(2)

    dash_duo.wait_for_element("h1", timeout=4)

    h1_text = dash_duo.find_element("h1").text
    assert h1_text == "Paralympics Dashboard"