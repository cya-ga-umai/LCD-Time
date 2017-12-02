#!/usr/bin/python
# coding: utf-8
import smbus
import time
import datetime

LCD_I2C_ADDRESS = 0x50
LCD_CONFIG_ADDRESS = 0x00
LCD_DISPLAY_ADDRESS = 0x80


def lcd_init():
    i2c.write_byte_data(LCD_I2C_ADDRESS, LCD_CONFIG_ADDRESS, 0x01)
    time.sleep(0.001)
    i2c.write_byte_data(LCD_I2C_ADDRESS, LCD_CONFIG_ADDRESS, 0x38)
    time.sleep(0.001)
    i2c.write_byte_data(LCD_I2C_ADDRESS, LCD_CONFIG_ADDRESS, 0x0f)
    time.sleep(0.001)
    i2c.write_byte_data(LCD_I2C_ADDRESS, LCD_CONFIG_ADDRESS, 0x06)
    time.sleep(0.001)


def print_lcd(str):
    for c in list(str):
        i2c.write_byte_data(LCD_I2C_ADDRESS, LCD_DISPLAY_ADDRESS, ord(c))
        time.sleep(0.001)


i2c = smbus.SMBus(1)

lcd_init()

while True:
    i2c.write_byte_data(LCD_I2C_ADDRESS, LCD_CONFIG_ADDRESS, 0x01)
    now = datetime.datetime.now()
    print_lcd(now.strftime("%Y/%m/%d"))
    i2c.write_byte_data(LCD_I2C_ADDRESS, LCD_CONFIG_ADDRESS, 0xc0)
    print_lcd(now.strftime("%H:%M:%S"))
    time.sleep(1)
