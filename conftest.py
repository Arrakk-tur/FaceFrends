# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(60)
    request.addfinalizer(wd.quit)
    return wd