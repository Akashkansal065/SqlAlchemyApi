from selenium import webdriver
import Selenyum.selecore.driverinitialize as drivs


class AllElements(drivs):
    name = drivs.find_element_by_name("q")
    name.send_keys("Lag gaye")


all = AllElements()