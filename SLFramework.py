# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:57:30 2019

@author: 007
"""
import FunctionLibrary as fl
import data
#from selenium import webdriver

print("Test Case 1:")
ResPath=fl.setup("TC1")
url="http://www.facebook.com"
driver=fl.open_url("1",url,ResPath)
fl.click(driver,"2","//*[@id='u_0_11']",ResPath)
fl.validateText(driver,"3","Create an account","//*[@id='content']/div/div/div/div/div[2]/div[1]/div[1]/span",ResPath)
fl.Dropdown(driver,"4","Mar","birthday_month",ResPath)
fl.ValDropdown(driver,"5",data.ls,"//*[@name='birthday_month']/option",ResPath)
fl.ValDropdown(driver,"6",data.date,"//*[@name='birthday_day']/option",ResPath)
fl.Dropdown(driver,"7","4","birthday_day",ResPath)
fl.wait(5,"8",ResPath)
fl.quit(driver,"9",ResPath)
#driver.get("http://www.facebook.com")

