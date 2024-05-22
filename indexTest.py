# imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# set driver
driver = webdriver.Chrome()
driver.get("C:\Users\zelenakzn\Desktop\GitHub\Dolgozat\index.html")

# functions

# test1: dupla kattintás után szerepel-e az "animation" class
def test1():
    element_one = driver.find_element(By.ID, "element-one")
    actions = ActionChains(driver)
    actions.double_click(element_one).perform()
    time.sleep(1)
    classes = element_one.get_attribute("class")
    assert "animation" in classes
    print("1. teszt sikeres")

# ha rámegy az egér, utána létezik-e box-shadow
def test2():
    element_two = driver.find_element(By.ID, "element-two")
    actions = ActionChains(driver)
    actions.double_click(element_two).perform()
    time.sleep(1)
    box_shadow = element_two.value_of_css_property("box-shadow")
    assert box_shadow != "none"
    print("2. teszt sikeres")
# kattintás után eltűnik-e
def test3():
    element_three = driver.find_element(By.ID, "element-three")
    element_three.click()
    time.sleep(1)
    display = element_three.value_of_css_property("display")
    assert display == "none"
    print("3. teszt sikeres")
# kattintás után a háttere zöld lesz-e
def test4():
    element_four = driver.find_element(By.ID, "element-four")
    element_four.click()
    time.sleep(1)
    background_color = element_four.value_of_css_property("background-color")
    assert background_color == "rgba(0,128,0,1)"
    print("4. teszt sikeres")
# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
def test5():
    element_four = driver.find_element(By.ID "element-four")
    actions = ActionChains(driver)
    actions.move_to_element(element_four).perform()
    time.sleep(1)
    element_four.screenshot("element_four_hover.png")
    print("5. teszt sikeres, képernyőkép pipa")

test1()
time.sleep(1)

test2()
time.sleep(1)

test3()
time.sleep(1)

test4()
time.sleep(1)

test5()
driver.quit()


