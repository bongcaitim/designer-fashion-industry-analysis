import pandas as pd
def filter_links(product_links):
    # Lọc ra những đường link có chứa 'iphone-15' hoặc 'Samsung-Galaxy-S23'
    filtered_links = [link for link in product_links if 'iphone-15' in link.lower() or 'samsung-galaxy-s23' in link.lower()]
    return filtered_links

def filter_and_extract_gb_from_df(data):
    # Làm sạch và chuyển đổi 'Discounted Price' sang dạng số
    data['Discounted Price Clean'] = pd.to_numeric(data['Discounted Price'].str.extract(r'₫([\d.]+)')[0].str.replace('.', '', regex=False), errors='coerce')
    
    # Xử lý và chuyển đổi 'sold_quanlity' từ định dạng như "16,4k" sang số nguyên
    def convert_sold_quantity(value):
        if 'k' in str(value).lower():
            return pd.to_numeric(value.lower().replace('k', '').replace(',', '.')) * 1000
        else:
            return pd.to_numeric(value, errors='coerce')

    data['sold_quanlity_clean'] = data['sold_quanlity'].apply(convert_sold_quantity).fillna(0).astype(int)
    
    # Trích xuất thông tin GB từ 'Product Title'
    data['GB'] = data['Product Title'].str.extract(r'(\d+GB)')
    
    # Lọc dữ liệu theo điều kiện đã cho: Discounted Price >= 14,000,000 VND và sold_quanlity >= 200
    filtered_data = data[(data['Discounted Price Clean'] >= 14000000) & (data['sold_quanlity_clean'] >= 200)]
    
    # Trả về DataFrame đã lọc với tất cả các cột ban đầu
    return filtered_data