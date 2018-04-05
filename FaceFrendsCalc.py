# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import pytest
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
    if EC.presence_of_element_located(By.CLASS_NAME, v.uiHeader):
        ActionChains(wd).send_keys(Keys.END).perform()
    else:
        frList = wd.find_element_by_id(v.FriendsList)
        print frList
        frLi = frList.find_elements_by_tag("ul")
        print frLi
    # frCount = len(frLi)
    # print frCount
