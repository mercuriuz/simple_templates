import requests
import json

base_url = 'https://leetcode-cn.com'

login_page_url = base_url + '/accounts/login'
list_url = base_url + '/api/problems/algorithms/'

headers = {
    'Referer': 'https://leetcode-cn.com',
    'Accept-Encoding': '',
}

session1 = requests.Session()

req1 = session1.get(login_page_url, headers=headers)

csrftoken = req1.cookies.get('csrftoken')

payloads = {
    'csrfmiddlewaretoken': csrftoken,
    'login': 'zhipenghao930930@gmail.com',
    'password': 'peqxe4-jihtez-noVwez'
}

req2 = session1.post(login_page_url, payloads, headers=headers)
print(req2.cookies)
req3 = session1.get(list_url, headers=headers)

data = req3.json()

total = data['num_total']
solved = data['num_solved']
locked = 0

print('Total: {}, Solved: {}, Locked: {}'.format(total, solved, locked))
ac_list = data['stat_status_pairs']
session1.close()
