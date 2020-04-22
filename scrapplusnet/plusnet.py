#!/usr/bin/env python3.8
import requests
import hashlib
import re
import os


def salted_password(admin_password, salt):
    password = f'{admin_password}{salt}'
    return hashlib.md5(password.encode()).hexdigest()


def extract_login_info(content):
    auth_key = re.search(r'name="auth_key" value="(\d+)"', content)
    post_token = re.search(r'name="post_token" value="(\w+)"', content)
    password_id = re.search(r'name="password_(\d+)" ', content)
    return dict(
        auth_key=auth_key.group(1),
        post_token=post_token.group(1),
        password_id=password_id.group(1)
    )


def hub_page(page_id, hub_ip, hub_password):
    session = requests.session()
    result = session.get(f'http://{hub_ip}/index.cgi?active_page={page_id}')
    if protected := re.match(r'<!-- Page\((\d+)\)=\[Login\] -->', result.text):
        page_data = extract_login_info(result.text)
        md5_pass = salted_password(hub_password, page_data['auth_key'])
        data = {
            'md5_pass': md5_pass,
            'active_page': protected.group(1),
            'post_token': page_data['post_token'],
            f'password_{page_data["password_id"]}': '',
            'mimic_button_field': 'submit_button_login_submit: ..',
            'auth_key': page_data['auth_key']
        }
        result = session.post(f'http://{hub_ip}/index.cgi', data=data)
        result.raise_for_status()
    return result.text


if __name__ == '__main__':
    content = hub_page(9143, '192.168.1.254', os.environ.get('PLUSNET_HUB_PASSWORD', 'H3FPJK6F'))
    print(content)