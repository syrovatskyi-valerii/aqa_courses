class WaitSeveralElements:
    def __init__(self, locator, quantity):
        self.locator = locator
        self.quantity = quantity

    def __call__(self, driver):

        try:
            # find a few elements
            # loсator - це тапл, а find_elements очікує 2 значення By, locator_path
            els = driver.find_elements(*self.locator) # list of elements
            return len(els) == self.quantity

        except:
            return False  # Якщо елемент не знайдено або не відображається, повертаємо False