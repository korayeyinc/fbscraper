#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fbscraper.py
#
#  Python - Selenium based web scraping app.
#

import argparse, time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


class Browser():
    def __init__(self, args):
        self.link    = args.url
        self.user    = args.username
        self.passwd  = args.password
        browser_opts = Options()
        self.browser = webdriver.Firefox(executable_path=args.driver, options=browser_opts)
        # check mode
        if (args.mode == 'headless'):
            browser_opts.add_argument('-headless')


    def run(self):
        self.browser.get(self.link)
        # login screen input_id strings
        user_input   = 'email'
        passwd_input = 'pass'

        self._send_keys(user_input, self.user)
        self._send_keys(passwd_input, self.passwd, post=True)
        time.sleep(2)


    # Key send event for input boxes/fields
    def _send_keys(self, element, value, post=False):
        _input = self.browser.find_element_by_id(element)
        _input.send_keys(value)
        # check post value and send the form if required
        if (post == True):
            _input.send_keys(Keys.RETURN)


    # Click event for buttons
    def _click_button(self, btn_id):
        _button = self.browser.find_elements_by_xpath(btn_id)
        _button.click()


def main(args):
    browser = Browser(args)
    browser.login()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG', conflict_handler='resolve')

    parser.add_argument(
        "-l", "--url",
        type = str,
        default = 'https://www.facebook.com/',
        help = "Target URL to be scraped.")

    parser.add_argument(
        "-u",
        "--username",
        type = str,
        default= '',
        help="Login username")

    parser.add_argument(
        "-p",
        "--password",
        type = str,
        default = '',
        help = "Login password")

    parser.add_argument(
        "-d",
        "--driver",
        type = str,
        default = './driver/geckodriver',
        help = "Path to the web driver. Assumes it's 'geckodriver' and located in './driver' directory")

    parser.add_argument(
        "-m",
        "--mode",
        type = str,
        default = '',
        help = "Driver running mode. Use 'headless' parameter to run in headless mode.")

    # parse command line arguments
    args = parser.parse_args()
    main(args)
