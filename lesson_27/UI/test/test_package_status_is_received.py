

def test_package_status_is_received(driver, received_number_package, check_package_page, status_result_page):

    # Given a valid package number (TTH)
    number = received_number_package

    # Open the search page
    check_package_page.open_page()

    # Searching by valid package number
    check_package_page.search_by_package_number(number_package=number)

    # Click on "Ok" button in pop-up
    status_result_page.click_on_ok_button_in_pop_up()

    # Verify that status should be displayed as 'Отримана' (Received)
    status_result_page.check_received_status()

