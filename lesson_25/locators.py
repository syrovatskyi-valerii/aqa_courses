'''Написати 25 XPath та 25 CSS локаторів для сайту https://qauto2.forstudy.space/
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
Дані для входу на сайт -
login - guest
pass - welcome2qauto
Для доступу через селеніум можна використати наступну конструкцію - driver.get("<https://UserName:Password@qauto2.forstudy.space>;");
'''

# "Header" on main page:
//button[@class='btn btn-outline-white header_signin']      #xpath
button.btn.btn-outline-white.header_signin                  #css
//button[@appscrollto='aboutSection' and text()='About']        #xpath
//button[@appscrollto='contactsSection'and text()='Contacts']   #xpath

# "Sign up" button on main page:
//a[@class='btn header-link -active']           #xpath
button.hero-descriptor_btn.btn.btn-primary      #css

# Modal window "Log in":
//label[text()='Email']     #xpath
//label[text()='Password']  #xpath
//input[@id='signinEmail']  #xpath
#signinEmail                #css
//input[@id='signinPassword']   #xpath
#signinPassword                 #css
//input[@id='remember'] #xpath
#remember               #css
//button[@class='btn btn-link' and text()='Registration']           #xpath
//button[@class='btn btn-primary' and text()='Login']               #xpath
//button[@class='btn btn-link' and text()='Forgot password']        #xpath
//button[@class='close']        #xpath
button.close                    #css

# Main page -> Contact section:
//a[@class='contacts_link display-4' and text()='ithillel.ua']       #xpath
a.contacts_link.display-4                                            #css
#or
[href='https://ithillel.ua']

//a[@class='contacts_link h4' and text()='support@ithillel.ua']     #xpath
[href="mailto:developer@ithillel.ua"]                               #css
//a[@href='https://www.facebook.com/Hillel.IT.School']              #xpath
[href='https://www.facebook.com/Hillel.IT.School']                  #css


# On page "https://qauto2.forstudy.space/panel/garage":
//a[@routerlink='garage' and @href='/panel/garage']                 #xpath
//a[@routerlink='expenses' and @href='/panel/expenses']             #xpath
//a[@routerlink='instructions' and @href='/panel/instructions']     #xpath
a.btn.btn-link.text-danger.btn-sidebar.sidebar_btn                  #css


# On page "https://qauto2.forstudy.space/panel/instructions":
#brandSelectDropdown                                                #css
#modelSelectDropdown                                                #css
//button[@class='instructions-search-controls_search btn btn-primary' and text()='Search']      #xpath

# Drop-down menu "My profile" in header:
#userNavDropdown        #css
a.dropdown-item.btn.btn-link.user-nav_link[href='/panel/garage']            #css
a.dropdown-item.btn.btn-link.user-nav_link[href='/panel/expenses']          #css
a.dropdown-item.btn.btn-link.user-nav_link[href='/panel/instructions']      #css
//button[@class='dropdown-item btn btn-link user-nav_link' and text()='Logout']     #xpath

# "Add a car" modal window:
div.modal-content   #css
#addCarBrand        #css
#addCarModel        #css
#addCarMileage      #css
//button[@class='btn btn-primary' and text()='Add']             #xpath
//button[@class='btn btn-secondary' and text()='Cancel']        #xpath
//h4[@class='modal-title' and text()='Add a car']               #xpath

# "Edit a car" modal window:
#carCreationDate        #css
//button[@class='btn btn-outline-danger' and text()='Remove car']       #xpath
//button[@class='btn btn-primary' and text()='Save']                    #xpath
button.btn.date-picker-toggle       #css

# "Remove car" modal window:
div.modal-content                                       #css
//h4[@class='modal-title' and text()='Remove car']      #xpath
//p[text()='Do you really want to remove Audi TT from your account?']                                       #xpath
//p[@class='text-danger' and text()='All related data will be lost, this action can not be undone!']        #xpath
//button[@class='btn btn-danger' and text()='Remove']                                                       #xpath

# "Add an expense" modal window:
#addExpenseCar                  #css
#addExpenseLiters               #css
#addExpenseTotalCost            #css
