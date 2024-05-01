from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import requests
import time
from datetime import datetime
from IPython.display import clear_output
import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
import re
from urllib.parse import urlparse, unquote
import json
import csv
# os.environ['PATH'] += r"E:\Installers\chromedriver_win32\chromedriver.exe"

import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urlparse
from datetime import datetime

def crawl_list_view_elise(url, domain):
    product_info_list = []
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html5lib")
    all_product_list = soup.find('div', class_='list')
    all_items = all_product_list.find_all('div', class_='c-item')
    for item in all_items:
        product_id = None
        
        product_sku = None
        
        general_id = f'{domain}_{product_id}'
        
        product_name = item.find('h3', class_='c-name').text.strip()
        
        product_price = item.find('div', class_='price').text.strip()
        
        product_url = item.find('a')['href']
        
        colors = []
        color_elements = item.find_all('p', class_='c-box_color')
        for ce in color_elements:
            ce_a_tag = ce.find('a', class_='c-color')
            color = ce_a_tag.get('title')
            colors.append(color)
            
        # Product images
        images = item.find_all('img')
        img_dict = {}

        image_order = 1
        for img in images:   
            img_name = img['alt']
            img_order_name = f'{image_order:03d}_{img_name}'
            
            img_src = img['src']
            img_dict[img_order_name] = img_src
                    
            image_order += 1
        
        product_info = {
        'general_id': general_id,
        'product_id': product_id,
        'sku': product_sku,
        'url': product_url,
        'product_name': product_name,
        'price': product_price,
        'image_list': img_dict
        }    
        
        # print(json.dumps(product_info, indent=4))    
        product_info_list.append(product_info)
        
    product_info_list_df = pd.DataFrame(product_info_list)
    return product_info_list_df


def crawl_detail_view_elise(product_url, domain):
    html_content = requests.get(product_url).text
    soup = BeautifulSoup(html_content, "html5lib")
    
    product_id = soup.find('p', class_='c-code').text.replace('MSP:', '').strip()
    
    general_id = f'{domain}_{product_id}'
    
    sku = None
    
    product_name = soup.find('h2', class_='c-title_module').text.strip()
    
    price = soup.find('span', id='price-no-discount')['data-price']
    
    colors = []
    color_elements = soup.find_all('p', class_='color c-show_color--name')
    for ce in color_elements:
        color = ce.find('span').text.strip()
        colors.append(color)
    
    description = soup.find('div', id='description').text.strip()
    
    instruction = soup.find('div', id='care_instration').text.strip()
    
    sizes = []
    sizes_element = soup.find('div', class_='items-option input_size')
    size_links = sizes_element.find_all('a', class_='c-name_size--choose')
    for size_link in size_links:
        size = size_link['data-name']
        sizes.append(size)
    sizes = set(sizes)
    
    nav = soup.find('nav', class_='location-page')
    categories = nav.find_all('li')
    category = categories[-2].text.strip()

    product_data = {
        "product_url": product_url,
        "product_id": product_id,
        "general_id": general_id,
        "sku": sku,
        "product_name": product_name,
        "price": price,
        "size": sizes,
        "color": color,
        "description": description,
        'image_list': None,
        'instruction': instruction, 
        'category': category
        
    }

    return product_data  

from time import sleep
from IPython.display import clear_output
import pandas as pd
import os

combined_csv_path = r'E:\COLLEGE\PROJECT\designer-fashion-industry-analysis\Crawling\data_for_analysis\sixdo\sixdo_website_data.csv'

# NẾU CHƯA TỒN TẠI DATA TỔNG THÌ TẠO DATA TỔNG
if os.path.exists(combined_csv_path):
    combined_product_data = pd.read_csv(combined_csv_path)
else:
    combined_product_data = pd.DataFrame()
    
# CHECK ĐÃ CÀO LINK NÀY CHƯA
if os.path.exists(combined_csv_path):
    product_data = pd.read_csv(combined_csv_path)
    try:
        existed_urls = product_data['product_url'].dropna().unique()
    except KeyError:
        existed_urls = []
else:
    existed_urls = []
    

start_page = 17
end_page = 36

for page_num in range(start_page, end_page+1):
    clear_output(wait=True)
    print(f'Processing page {page_num}/{end_page}')
    page_url = f'https://sixdo.vn/san-pham/page-{page_num}'
    html_content = requests.get(page_url).text
    soup = BeautifulSoup(html_content, "html5lib")
    all_product_list = soup.find('div', class_='list')
    all_items = all_product_list.find_all('div', class_='c-item')
    
    all_items_len = len(all_items)
    count = 1
    
    for item in all_items:
        product_url = item.find('a')['href']
        
        if product_url in existed_urls:
            print(f'\rExisted URL', end='')
            print(f'\rFinished product {count}/{all_items_len} on page {page_num}', end='')
            count += 1
        
        else:
            combined_product_data = pd.read_csv(combined_csv_path)
            product_data_dict = crawl_detail_view_elise(product_url=product_url, domain='sixdo')
            product_data_df = pd.DataFrame([product_data_dict])
            product_data_df = product_data_df.astype(str)
            
            concatenated_df = pd.concat([combined_product_data, product_data_df], ignore_index=True)
            concatenated_df = concatenated_df.drop_duplicates()
            concatenated_df.to_csv(combined_csv_path, index=False)  # Save to CSV
            
            print(f'''\rA BRAND NEW URL!!! Finished product {count}/{all_items_len} on page {page_num}''', end='')
            
            count += 1
            sleep(5)
    print()