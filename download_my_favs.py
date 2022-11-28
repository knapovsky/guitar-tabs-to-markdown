#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

username = 'username'
password = 'password'

browser = webdriver.Firefox()
browser.get('https://www.ultimate-guitar.com/user/mytabs')
browser.find_element_by_css_selector('ggw-g._1Oybz.Lgzwb.eCjBm').click()
browser.find_element_by_name('username').send_keys(username)
browser.find_element_by_name('password').send_keys(password)
browser.find_element_by_css_selector('.ggw-g._1iU2Q._2HOed._2aipe.eCjBm').click()

tab_section = browser.find_element_by_class_name('_7Ivu3')
tracks = tab_section.find_elements_by_class_name('_335bj')
DATA = []
cnt = 0
for track in tracks:
    TRACKDATA = []
    try:
        TRACKDATA.append(track.find_element_by_css_selector('a.link-secondary').text)
    except:
        TRACKDATA.append(DATA[cnt-1][0])
    nameLink = track.find_element_by_css_selector('a.link-primary')
    TRACKDATA.append(nameLink.text)
    TRACKDATA.append(nameLink.get_attribute("href"))
    DATA.append(TRACKDATA)
    cnt = cnt + 1

cnt = 0
for track in DATA:
    try:
        browser.get(track[2])
        browser.find_element_by_css_selector('button.ggw-g._2PwLX._3m-lU').click()
        textEl = browser.find_element_by_css_selector('textarea._3pS6m.TZpJT._3ORni._2smpm')
        text = textEl.get_attribute('value')
        DATA[cnt].append(text)
    except:
        DATA[cnt].append('NOT FOUND')
    cnt = cnt + 1

import io
cnt = 0
for track in DATA:
    print(track[0] + ' - ' + track[1] + '.md')
    file = io.open(track[0] + ' - ' + track[1] + '.md', 'w', encoding="utf-8")
    #file.write(codecs.BOM_UTF8)
    file.write('```\n')
    file.write(track[3])
    file.write('\n```')
    file.close()
    cnt = cnt + 1