from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
import os
from time import sleep
import requests
import time
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import shutil

def launch_driver():
    options = uc.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # options.add_argument("--disable-extensions")
    # options.add_argument("--headless")
    options.add_experimental_option("prefs",{"credentials_enable_service": False,"profile.password_manager_enabled": False,"profile.default_content_setting_values.notifications" : 2,"useAutomationExtension" :False})
    options.add_argument("--start-maximized")

    driver = uc.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver

def insert_cookies(driver, url, cookie_string = "_fbp=fb.1.1664072361859.2073394353;_hjSessionUser_868286=eyJpZCI6ImEzY2NjMGNjLTliMzQtNWM1NC1iNDZjLTAyMzk0YmY0NmUxZiIsImNyZWF0ZWQiOjE2NjQwNzIzNjY4MTcsImV4aXN0aW5nIjp0cnVlfQ==;amp_adc4c4=viDliDkCdeGpNNh1esZ2i6.czdQSDNyV3Q4RmNaNDgxSjMzWlZiRFU4YnFpMg==..1h1qi4drj.1h1qi5k1b.0.ea.ea;SPC_F=CKZ6ea46ilSRyVKxhqZJdtQzWWREmdWM;REC_T_ID=6a17b6f7-7b01-11ee-a523-02128f22f73d;SPC_CLIENTID=Q0taNmVhNDZpbFNSlbyomshadrgykhil;_ga_M32T05RVZT=GS1.1.1702419891.149.1.1702420259.22.0.0;_gcl_au=1.1.834556064.1706320297;_fbc=fb.1.1709444966370.IwAR2FfEbbH-lbf6zuYrBlYw9DHUwUHYkuBxlB5HKCSkaMzM_JgSHmnoc6P3M;_gcl_aw=GCL.1709445493.CjwKCAiAuYuvBhApEiwAzq_YiVwuBxvP4c6lK0HiEHN849-eFclzyI0ooIkld5kOgOMyWHiwgZZyvxoCtRIQAvD_BwE;_gac_UA-61914164-6=1.1709445496.CjwKCAiAuYuvBhApEiwAzq_YiVwuBxvP4c6lK0HiEHN849-eFclzyI0ooIkld5kOgOMyWHiwgZZyvxoCtRIQAvD_BwE;_ga_3XVGTY3603=GS1.1.1709606428.4.1.1709607232.60.0.0;_gcl_dc=GCL.1710159861.CjkKEQjw17qvBhCAgvSB9K2PwvMBEiQA2Y8avtZdk-JPTk649ckeGcuKKtViwuEekpqMCTRjCSW8huDw_wcB;_med=affiliates;language=en;__LOCALE__null=VN;csrftoken=sMKBukt6gA97pZSlYmjRhSGsG3sXV03H;SPC_SI=IIACZgAAAABaUUlmUDcxTr9XPwAAAAAAbjVxTDlwVlY=;SPC_SEC_SI=v1-OTd0RTBQMXpoNVpEb2x5NAVC9oEsxzUJ75fJmdHJMzL0Wz8OK98iRCtMitLHOwtt4p7j6ye8y32Xp4KXrSLpsQf9Rm3YRkkZW7ywBKLjilc=;_sapid=1229e018fa38647dc24a6c760d5242d71966abfb873ccb685a67380d;_QPWSDCXHZQA=f252a810-ca09-4166-860e-71c856fa6e07;REC7iLP4Q=1b6f4e09-01ea-49b3-9ced-482d2a21a1ca;_hjSession_868286=eyJpZCI6ImI2MDNiMjM1LTI2NmMtNDc5Mi1iYTIwLWEzYmM2MDllYTc2ZSIsImMiOjE3MTE2ODQwNzI4NTUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=;AMP_TOKEN=%24NOT_FOUND;_ga=GA1.2.1117054609.1664072364;_gid=GA1.2.1129100352.1711684073;_dc_gtm_UA-61914164-6=1;SPC_EC=.azJ4N2pTOEpJTGtrQU40UD5k5JFTEUwusdQPvPIvve8Ecu17T4L7vP9sNp/BW2uF9D/Dci7S68lj3o/X6niyWkVSpkSx9wm5PPzP7Hw0ZIP5QZMGLHC5yh2x2p+nM+r+KrDFer91421PmaC0JIllfxpBpZpOalnMz0uvg8My5vc0fb+Yrm07Gn0CJxB5cUz2m3mYca2+x+IbIPMzIbDZoQ==;SPC_ST=.azJ4N2pTOEpJTGtrQU40UD5k5JFTEUwusdQPvPIvve8Ecu17T4L7vP9sNp/BW2uF9D/Dci7S68lj3o/X6niyWkVSpkSx9wm5PPzP7Hw0ZIP5QZMGLHC5yh2x2p+nM+r+KrDFer91421PmaC0JIllfxpBpZpOalnMz0uvg8My5vc0fb+Yrm07Gn0CJxB5cUz2m3mYca2+x+IbIPMzIbDZoQ==;_ga_4GPP1ZXG63=GS1.1.1711684072.57.0.1711684076.56.0.0;SPC_U=169479634;SPC_R_T_ID=25ypNvL5vlzg4w5vQ4aYmD5Z2KofPwJV53d0al5I517Ur2OS7PGo5ADh5+MrXm631fO+nA5zjWrN3wnaVnkchoNEiql7VyYdphNInxoYxb7DCvgU+rGsufpcjgWed177Yovjx/khs8BbXHQdvf6VMV/uJQg6i1C19V8dr3WWt3Y=;SPC_R_T_IV=SkJrWTFWbnk0WU0zUmJLYw==;SPC_T_ID=25ypNvL5vlzg4w5vQ4aYmD5Z2KofPwJV53d0al5I517Ur2OS7PGo5ADh5+MrXm631fO+nA5zjWrN3wnaVnkchoNEiql7VyYdphNInxoYxb7DCvgU+rGsufpcjgWed177Yovjx/khs8BbXHQdvf6VMV/uJQg6i1C19V8dr3WWt3Y=;SPC_T_IV=SkJrWTFWbnk0WU0zUmJLYw==;SPC_IA=1;shopee_webUnique_ccd=XtpA9Q%2FxYzLog4eg4DS1Ew%3D%3D%7C4OvJNLIQ3a4PMk9jNq7P5DUc7d1S8w6MlF3cw%2FnuowWag5Ypes28aEsORCmwI%2F8sfnDYthCBUmM%3D%7C9sc6jMAgM06BCIBg%7C08%7C3;ds=fa492bd679e06baf221ed5f8006ffbd8;|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"):
    cookie_dict = {}
    items = cookie_string.split(';')
    for item in items:
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookie_dict[key] = value

    driver.get(url)  
    sleep(3)
    for name, value in cookie_dict.items():
        driver.add_cookie({'name': name, 'value': value})
    driver.refresh() 
    
    print("Cookies added successfully.")
    
def login(driver):
    import random
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.chrome.service import Service

    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    sleep(4.765)


    def type_slow(element, text):
        for char in text:
            element.send_keys(char)
            sleep(random.uniform(0.1, 0.8))
    # Find and fill in the username field slowly
    username_field = driver.find_element('name', 'loginKey')
    # nhập username 
    type_slow(username_field, '0977829788')

    # Move to the password field and fill it in slowly
    password_field = driver.find_element('name', 'password')
    ActionChains(driver).move_to_element(password_field).perform()
    # nhập password
    type_slow(password_field, 'Baytuanloc2412/')

    login_button = driver.find_element("css selector", '#main > div > div.uqT7Nz > div > div > div > div:nth-child(2) > div > div.p7oxk2 > form > button')
    sleep(1.78)
    login_button.click()

def safe_find_element(driver, selector, by=By.CSS_SELECTOR):
    try:
        element = driver.find_element(by, selector)
        return element
    except NoSuchElementException:
        return None
def scroll_by_percentage(driver, vertical_percentage=0, horizontal_percentage=0):
    # Calculate the scroll amount based on percentages
    vertical_scroll_amount = driver.execute_script("return (document.documentElement.scrollHeight - window.innerHeight) * arguments[0];", vertical_percentage / 100)
    horizontal_scroll_amount = driver.execute_script("return (document.documentElement.scrollWidth - window.innerWidth) * arguments[0];", horizontal_percentage / 100)
    print('Scrolling......')
    # Scroll the page vertically and horizontally
    driver.execute_script("window.scrollBy({0}, {1});".format(horizontal_scroll_amount, vertical_scroll_amount))
    
def get_product_links(driver, page_num):
    product_links = []  # Danh sách để lưu trữ các link sản phẩm
    if brand == 'elise':
        url = f'https://shopee.vn/elise_official?page={page_num}&sortBy=pop'
    elif brand == 'sixdo':
        if page_num == 0:
            url = 'https://shopee.vn/sixdoofficial#product_list'
        else:
            url = f'https://shopee.vn/sixdoofficial?page={page_num}&sortBy=pop&tab=0'
        
    driver.get(url)
    sleep(4.765)  # Adjust based on your actual wait time needed for the page to load
    scroll_by_percentage(driver, vertical_percentage=80)
    if brand == 'elise':
        try:
            for card_num in range(0, 31):  # Thay đổi số lượng lặp nếu cần
                try:
                    # Cập nhật selector để phản ánh đúng cấu trúc của trang web
                    selector = f"#main > div > div:nth-child(3) > div > div > div > div.shop-page > div > div.container > div.shop-page__all-products-section > div.shop-page_product-list > div > div.shop-search-result-view > div > div:nth-child({card_num}) > a"
                    element = driver.find_element(By.CSS_SELECTOR, selector)
                    product_link = element.get_attribute('href')
                    if product_link:
                        product_links.append(product_link)
                except NoSuchElementException:
                    print(f"Sản phẩm thứ {card_num} không được tìm thấy.")
                    continue  # Dừng vòng lặp nếu phần tử không được tìm thấy
                except Exception as e:
                    print(f"Error occurred while processing element {card_num} on page {page_num}: {e}")
                    print(f"URL causing the error: {url}")
                    continue

            return product_links
        except TimeoutException:
            print("Timed out waiting for page to load")
            return None
    elif brand == 'sixdo':
        shop_view = driver.find_element(By.CLASS_NAME, 'shop-search-result-view')
        rows = shop_view.find_element(By.CSS_SELECTOR, "div.row")
        prod_cards = rows.find_elements(By.XPATH, 'div')
        for prod in prod_cards:
            product_link = prod.find_element(By.CLASS_NAME, 'contents').get_attribute('href')
            product_links.append(product_link)
        return product_links

def safe_find_text(by, selector):
    global driver
    try:
        element_text = driver.find_element(by, selector).text
        return element_text
    except NoSuchElementException:
        return None

def get_product_info(driver, link):
    driver.get(link)
    sleep(5)  # Đợi trang tải và cookies có hiệu lực

    print(link)

    # Lấy ngày hiện tại
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(current_date)
    
    if brand=='sixdo':
        product_title_css_selector = r'#sll2-normal-pdp-main > div > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div.WBVL_7 > span'
        crossed_price_css_selector = r'#sll2-normal-pdp-main > div > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div:nth-child(3) > div > div > section > div > div.qg2n76'
        current_price_css_selector = r'#sll2-normal-pdp-main > div > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div:nth-child(3) > div > div > section > div > div.flex.items-center > div.G27FPf'
        percent_discount_css_selector = r'#sll2-normal-pdp-main > div > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div:nth-child(3) > div > div > section > div > div.flex.items-center > div.o_z7q9'
        number_bar_selector = r'#sll2-normal-pdp-main > div > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div.flex.asFzUa'
        product_variations_and_stocks_box_selector = r'#sll2-normal-pdp-main > div > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div.at_ZtL > div > div'

    elif brand == 'elise':
        product_title_css_selector = r'#main > div > div:nth-child(3) > div.theme--ofs > div.KrtGbA > div > div.container > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div.WBVL_7 > span'
        crossed_price_css_selector = r'#main > div > div:nth-child(3) > div:nth-child(1) > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div:nth-child(3) > div > div > section > div > div.qg2n76'
        current_price_css_selector = r'#main > div > div:nth-child(3) > div.theme--ofs > div.KrtGbA > div > div.container > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div:nth-child(3) > div > div > section > div > div.flex.items-center > div.G27FPf'
        percent_discount_css_selector = '#main > div > div:nth-child(3) > div:nth-child(1) > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div:nth-child(3) > div > div > section > div > div.flex.items-center > div.o_z7q9'
        number_bar_selector = '#main > div > div:nth-child(3) > div.theme--ofs > div.KrtGbA > div > div > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div.flex.asFzUa'
        product_variations_and_stocks_box_selector = r'#main > div > div:nth-child(3) > div.theme--ofs > div.KrtGbA > div > div.container > section.product-briefing.flex.card.vX9SYw > section.flex.flex-auto.i9t0tr > div > div.at_ZtL > div > div.flex.KIoPj6.W5LiQM'
    
    product_title = safe_find_text(By.CSS_SELECTOR, product_title_css_selector)
    print("Product Title:", product_title)
    crossed_price = safe_find_text(By.CSS_SELECTOR, crossed_price_css_selector)
    print(crossed_price)
    current_price_in_red = safe_find_text(By.CSS_SELECTOR, current_price_css_selector)
    print(current_price_in_red)
    percent_discount = safe_find_text(By.CSS_SELECTOR, percent_discount_css_selector)
    print("Percent_discount:", percent_discount)   
    
    number_bar = driver.find_element(By.CSS_SELECTOR, number_bar_selector)
    number_bar_parts = number_bar.find_elements(By.CLASS_NAME, 'flex')

    parts = []

    for button in number_bar_parts:
        text = button.text
        text = text.replace('\n', ' ')
        parts.append(text)

    if len(parts) == 3:
        rating_score = parts[0]
        rating_count = parts[1].split()[0]
        sold_quant = parts[2].split()[0]

    else:
        rating_score = None
        rating_count = None
        sold_quant = parts[0].split()[0]
        
    print(f'Đánh giá chung: {rating_score}')
    print(f"Lượt đánh giá: {rating_count}")
    print(f"Lượt bán: {sold_quant}")
    
     
    product_variations_and_stocks_box = driver.find_element(By.CSS_SELECTOR, product_variations_and_stocks_box_selector)
    var_sections = product_variations_and_stocks_box.find_elements(By.TAG_NAME, 'section')
    variation_dict = {}
    for section in var_sections:
        title = section.find_element(By.TAG_NAME, 'h3').text.strip().strip('\n')
        content = section.find_element(By.XPATH, './h3/following-sibling::div[1]').text.strip().strip('\n').split('\n')
        variation_dict[title] = content
    print('Variations:\n',variation_dict)
    
    # Tải ảnh
    img_dict = {}
    img_element_css_selector = r'#sll2-normal-pdp-main > div > div > div > div > section.product-briefing.flex.card.vX9SYw > section.TFDXyQ > div.flex.flex-column > div.airUhU > div:nth-child(1) > div > div.wOzCmT.thumbnail-selected-mask'
    image_element = driver.find_element(By.CSS_SELECTOR, img_element_css_selector)
    image_element.click()
    pictures = driver.find_element(By.CLASS_NAME, 'K02C_O').find_elements(By.TAG_NAME, 'picture')
    for image_order, picture in enumerate(pictures, start=1):
        img = picture.find_element(By.TAG_NAME, 'img')
        img_name = product_title
        img_order_name = f'{image_order:03d}_{img_name}' 
        img_src = img.get_attribute('src')
        img_dict[img_order_name] = img_src

    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    ############################################
    ############ ELEMENTS O DUOI ###############
    ############################################
    scroll_by_percentage(driver, vertical_percentage=20)
    ############################################
    
    # CHI TIẾT SẢN PHẨN
    product_specifications_dict = {}
    
    if brand=='elise':
        detail_counter = 1
        while True:  
            try:
                main_element = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/section[1]')

                # Find all child elements with class 'Tq1nbH' using dynamic XPath
                css_selectors = f'#main > div > div:nth-child(3) > div.theme--ofs > div > div > div > div.wAMdpk > div > div.page-product__content--left > div.product-detail.page-product__detail > section:nth-child(1) > div > div:nth-child({detail_counter})'
                
                child_element = main_element.find_element(By.CSS_SELECTOR, css_selectors)
                
                detail_label = child_element.find_element(By.TAG_NAME, 'label').text
                
                detail_content = child_element.text.replace(detail_label, '')
                if detail_label in ['Danh Mục', 'Category']:
                    detail_content = detail_content.replace('\n','>').strip('>')
                else:
                    detail_content = detail_content.replace('\n', '')
                
                product_specifications_dict[detail_label] = detail_content

                detail_counter += 1

            except NoSuchElementException:
                print(f"Phần tử detail thứ {detail_counter} không được tìm thấy, thoát khỏi vòng lặp.")
                break
        description_xpath = '//*[@id="main"]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div[1]/section[2]/div'
        description = safe_find_text(By.XPATH, description_xpath)
    
    elif brand=='sixdo':
        # EXTRACT PRODUCT SPECIFICATIONS
        page_product_detail_css_selector = r'#sll2-normal-pdp-main > div > div > div > div > div.wAMdpk > div > div.page-product__content--left > div.product-detail.page-product__detail'
        page_product_detail = driver.find_element(By.CSS_SELECTOR, page_product_detail_css_selector)
        page_product_detail_sections = page_product_detail.find_elements(By.CSS_SELECTOR, 'section.I_DV_3')

        product_specifications, product_description = page_product_detail_sections[0], page_product_detail_sections[1]
        product_specifications = product_specifications.find_element(By.CSS_SELECTOR, 'div:nth-child(2)')

        product_spec_lines = product_specifications.find_elements(By.CLASS_NAME, 'Tq1nbH')
        for line in product_spec_lines:
            detail_label = line.find_element(By.TAG_NAME, 'label').text
            detail_content = line.text.replace(detail_label, '')
            
            if detail_label in ['Danh Mục', 'Category']:
                detail_content = detail_content.replace('\n','>').strip('>')
            else:
                detail_content = detail_content.replace('\n', '')
            
            print(f"{detail_label}: {detail_content}")
    
            product_specifications_dict[detail_label] = detail_content
            
        # EXTRACT PRODUCT DESCRIPTION
        product_description = product_description.find_element(By.CLASS_NAME, 'Gf4Ro0')
        description = product_description.text.strip()
    
    
    
    print(f"Mô tả: {description}")


    product_info = {
        'Platform': 'Shopee',
        'Date Crawled': current_date,
        'Product Title': product_title,
        'Crossed Price': crossed_price,
        'Current Price': current_price_in_red,
        'Percent Discount' : percent_discount,
        'Sold': sold_quant,
        'Rating Count': rating_count,
        'Average Rating': rating_score,
        'Description': description,
        'Image List': img_dict
    }
    product_info.update(variation_dict)
    product_info.update(product_specifications_dict)

    return product_info

def get_comments():
    def extract_comments():
        page_comments = []
        comments = driver.find_elements(By.CSS_SELECTOR, 'div.shopee-product-rating')
        for comment in comments:
        # AUTHOR OF THE COMMENT
            comment_author = comment.find_element(By.CLASS_NAME, 'shopee-product-rating__author-name').text.strip()
            
        # TIME AND VARIATION
            time_and_variation_element = comment.find_element(By.CLASS_NAME, 'shopee-product-rating__time')
            time_and_variation = time_and_variation_element.text.strip()
            categorized_comment = []
            written_comment = None
            seller_response = None
            
            
        # CO SELLER RESPONSE    
            try:
                seller_response_element = comment.find_element(By.CSS_SELECTOR, 'div.TQTPT9')
                seller_response = seller_response_element.text.strip('\n').strip().replace('\n', '')
            except NoSuchElementException:
                seller_response = None
                
        # CO CATEGORIZE
            div_elements_with_margin_top = comment.find_elements(By.CSS_SELECTOR, 'div[style*="margin-top"]')
            if not div_elements_with_margin_top:  # Check if the list is empty
                next_div_element = time_and_variation_element.find_element(By.XPATH, 'following-sibling::div')
                if next_div_element.get_attribute('class') not in ('TQTPT9', 'shopee-product-rating__actions'):
                    written_comment = next_div_element.text.strip()
            else:
                for i in range(len(div_elements_with_margin_top)):
                    unspecified_cmt = div_elements_with_margin_top[i].text.strip().strip('\n')
                    if i == (len(div_elements_with_margin_top))-1:
                        written_comment = unspecified_cmt
                    else:
                        categorized_comment.append(unspecified_cmt)
            
            # RATING
            svg_elements = comment.find_elements(By.CSS_SELECTOR, '.shopee-product-rating__rating svg')
            count_fill_none = sum(1 for svg in svg_elements if svg.find_element(By.CSS_SELECTOR, 'polygon').get_attribute('fill') == 'none')
            stars = 5 - count_fill_none
            
            
            comment_dict = {'Author': comment_author, 'Time and Category': time_and_variation, 'Categorized Feedbacks': categorized_comment, 'Stars': stars, 'Written Comment': written_comment, "Seller's Response": seller_response}
            page_comments.append(comment_dict)
            print(comment_dict,end='\n\n')
        return page_comments
    
    
    
    def end_page():
        buttons_container = driver.find_element(By.CSS_SELECTOR, 'div.shopee-page-controller.product-ratings__page-controller')
        
        buttons = buttons_container.find_elements(By.TAG_NAME, 'button')
        
        next_button_selector = "#sll2-normal-pdp-main > div > div > div > div > div.wAMdpk > div > div.page-product__content--left > div:nth-child(2) > div > div > div.product-ratings__list > div.shopee-page-controller.product-ratings__page-controller > button.shopee-icon-button.shopee-icon-button--right"
        next_button = driver.find_element(By.CSS_SELECTOR, next_button_selector)
        
        next_button_index = buttons.index(next_button)
        
        if next_button_index > 0 and "shopee-button-solid--primary" in buttons[next_button_index - 1].get_attribute('class'):
            return True
        else:
            return False
        
        
    

    ###### RETURN COMMENTS #####
    all_comments_list = []
    product_info_section = driver.find_element(By.XPATH, "//h2[text()='Product Information Section']/following-sibling::div")
    try:
        button_element = product_info_section.find_element(By.CSS_SELECTOR, 'button.flex:nth-child(2)')
        button_element.click()
    except NoSuchElementException:
        return all_comments_list

    counter = 1
    while True:
        delay = random.uniform(3, 5)
        time.sleep(delay)
        page_comments = extract_comments()
        all_comments_list.extend(page_comments)  
            
        if end_page() == True:
            print(f'\rFinished {counter} page.', end='')
            print('\nLast page.')
            break
        else:
            print(f'\rFinished {counter} page.', end='')
            next_page_button_css_selector = "#sll2-normal-pdp-main > div > div > div > div > div.wAMdpk > div > div.page-product__content--left > div:nth-child(2) > div > div > div.product-ratings__list > div.shopee-page-controller.product-ratings__page-controller > button.shopee-icon-button.shopee-icon-button--right"
            next_page = driver.find_element(By.CSS_SELECTOR, next_page_button_css_selector)
            next_page.click()
        counter += 1
    return all_comments_list


# Thêm cookies vào trình duyệt
driver = launch_driver()
url = "https://shopee.vn"
cookie_string = "_fbp=fb.1.1664072361859.2073394353;_hjSessionUser_868286=eyJpZCI6ImEzY2NjMGNjLTliMzQtNWM1NC1iNDZjLTAyMzk0YmY0NmUxZiIsImNyZWF0ZWQiOjE2NjQwNzIzNjY4MTcsImV4aXN0aW5nIjp0cnVlfQ==;amp_adc4c4=viDliDkCdeGpNNh1esZ2i6.czdQSDNyV3Q4RmNaNDgxSjMzWlZiRFU4YnFpMg==..1h1qi4drj.1h1qi5k1b.0.ea.ea;SPC_F=CKZ6ea46ilSRyVKxhqZJdtQzWWREmdWM;REC_T_ID=6a17b6f7-7b01-11ee-a523-02128f22f73d;SPC_CLIENTID=Q0taNmVhNDZpbFNSlbyomshadrgykhil;_ga_M32T05RVZT=GS1.1.1702419891.149.1.1702420259.22.0.0;_fbc=fb.1.1709444966370.IwAR2FfEbbH-lbf6zuYrBlYw9DHUwUHYkuBxlB5HKCSkaMzM_JgSHmnoc6P3M;_gcl_aw=GCL.1709445493.CjwKCAiAuYuvBhApEiwAzq_YiVwuBxvP4c6lK0HiEHN849-eFclzyI0ooIkld5kOgOMyWHiwgZZyvxoCtRIQAvD_BwE;_gac_UA-61914164-6=1.1709445496.CjwKCAiAuYuvBhApEiwAzq_YiVwuBxvP4c6lK0HiEHN849-eFclzyI0ooIkld5kOgOMyWHiwgZZyvxoCtRIQAvD_BwE;_ga_3XVGTY3603=GS1.1.1709606428.4.1.1709607232.60.0.0;_gcl_dc=GCL.1710159861.CjkKEQjw17qvBhCAgvSB9K2PwvMBEiQA2Y8avtZdk-JPTk649ckeGcuKKtViwuEekpqMCTRjCSW8huDw_wcB;language=en;_med=refer;SPC_SI=DI8fZgAAAAAwUFR6dnhna3DO7gAAAAAAVmVMZ1dUYkI=;SPC_SEC_SI=v1-UkxmYkRRS2lkNzVocEF4S/SkQURalhRq6e4g84WooxqVACYT2+yhRH05Iyqk45ttlGIcIe17CRNCr3/3OOMm8quM0hx6WmpOPb/4U7za6lU=;_QPWSDCXHZQA=f252a810-ca09-4166-860e-71c856fa6e07;REC7iLP4Q=1b6f4e09-01ea-49b3-9ced-482d2a21a1ca;_gid=GA1.2.1334171042.1714095381;__LOCALE__null=VN;_gcl_au=1.1.1220014005.1714110999;csrftoken=94BzOzel6rADscSJvmCTIz0dOfK2N4XP;SPC_U=-;SPC_EC=-;_sapid=1229e018fa38647dc24a6c760d5242d71966abfb873ccb685a67380d;shopee_webUnique_ccd=9soQsoVuGZ%2F0WS4aMYrvZQ%3D%3D%7CFxSjKBz99s8AbsWnO%2BcmwAPR8N2eK7Bo6Vca7zH6mpBEtNk32QjVspd7DgGz%2B%2BNwPvkAaPAGw7U%3D%7CYl1qIez2csS8IJsh%7C08%7C3;ds=70fb0a278a77b5fa554882214b83f36d;SPC_R_T_ID=uuRWmUMmGqoy/f5vw/KT92GcTsU7LfNvxJfdYr5P4dwMAZJzOTYFDFKTqp5r04ehyKtLbCPFpR95xn2B5PqY3gDTrNjmzperxUVXHuVVgo0XKz338jmBf/n9FtC1cTx8JNxzbaWKm4/y6li9V+IGRvNMi4OoINXs2/OtR6vIz0Q=;SPC_R_T_IV=cEl0ZmtrbnBKbWNjckp3Wg==;SPC_T_ID=uuRWmUMmGqoy/f5vw/KT92GcTsU7LfNvxJfdYr5P4dwMAZJzOTYFDFKTqp5r04ehyKtLbCPFpR95xn2B5PqY3gDTrNjmzperxUVXHuVVgo0XKz338jmBf/n9FtC1cTx8JNxzbaWKm4/y6li9V+IGRvNMi4OoINXs2/OtR6vIz0Q=;SPC_T_IV=cEl0ZmtrbnBKbWNjckp3Wg==;_ga_4GPP1ZXG63=GS1.1.1714111007.78.0.1714111007.60.0.0;_hjSession_868286=eyJpZCI6ImMyODU5ZDI0LTU1MGMtNDY2Ny1hODM2LWY0NjVkMDE2NzU3YiIsImMiOjE3MTQxMTEwMDgxMzQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=;AMP_TOKEN=%24NOT_FOUND;_ga=GA1.2.1117054609.1664072364;_dc_gtm_UA-61914164-6=1;|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
insert_cookies(driver, url, cookie_string)
driver.implicitly_wait(8)
sleep(30)

import json
import os
from IPython.display import clear_output

# domain='elise'
# # Folder chứa data
brand = 'sixdo'
data_folder = f'E:\\COLLEGE\\PROJECT\\designer-fashion-industry-analysis\\temp_crawling_results\\{brand}'
if not os.path.exists(data_folder):
    os.makedirs(data_folder)
# # Folder cho website
# domain_folder = os.path.join(data_folder, domain)
# if not os.path.exists(domain_folder):
#     os.makedirs(domain_folder)
# part_folder_size = 300



# current_datetime = datetime.now()
# attempt = get_attempt(current_datetime)
# attempt_folder_path = create_attempt_folder(data_folder, domain_folder, current_datetime, attempt)


# detail_folder_path = create_detail_folder(attempt_folder_path, product_id, product_name, part_folder_size)


            
product_links = []
start_page = 0
end_page = 1
for page_num in range(start_page, end_page): 
    
    # THERE SHOULD BE CÀO LIST HERE
    
    # Lấy các links sản phẩm trên list view này
    product_links_on_page = get_product_links(driver, page_num)

    all_product_list = []

    count = 1
    for url in product_links_on_page:
        print(f"PROCESSING PAGE {page_num+1} / {end_page}\nProgress: {count}/{len(product_links_on_page)}")
        
        
        this_product_info = get_product_info(driver, url)
        prod_name = this_product_info['Product Title']
        json_file_path = os.path.join(data_folder, f"info_{prod_name}.json")

        if os.path.exists(json_file_path):
            print(f"Skipping URL {url} as JSON file already exists.")
            count += 1
            continue
        
        
        clear_output(wait=True)
        print(f"PROCESSING PAGE {page_num+1} / {end_page}\nProgress: {count}/{len(product_links_on_page)}")

        # this_product_cmt_list = get_comments()

        this_product_json = {'product_url': url,
                            'product_info': this_product_info,
                            'product_comments': []}
        
        # Clear output
        count += 1
        

        
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(this_product_json, json_file, ensure_ascii=False, indent=4)
            
            
        clear_output(wait=True) 