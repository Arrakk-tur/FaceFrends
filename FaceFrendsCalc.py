# -*- coding: utf-8 -*-
import time
import Var as v


def test_FaceFrendsCalc(driver):
    wd = driver
    wd.get(v.site)
    wd.find_element_by_id(v.email).click()
    wd.find_element_by_id(v.email).send_keys(v.Umail)
    wd.find_element_by_id(v.pswd).click()
    wd.find_element_by_id(v.pswd).send_keys(v.Upas)
    wd.find_element_by_id(v.Lb).click()
    assert wd.find_element_by_id(v.glav)
    wd.find_element_by_css_selector(v.ProfPage).click()
    wd.find_element_by_css_selector(v.druzijaB).click()
    assert wd.find_element_by_id(v.FriendsH)
    # if EC.presence_of_element_located(By.CLASS_NAME, v.uiHeader):
    #     ActionChains(wd).send_keys(Keys.END).perform()
    # else:
    SCROLL_PAUSE_TIME = 1.5

    # Get scroll height
    last_height = wd.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = wd.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    frList = wd.find_element_by_id(v.FriendsList)
    frLi = frList.find_elements_by_tag_name("li")
    frCount = len(frLi)
    print frCount
