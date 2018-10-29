import requests
from spider.config import DEFAULT_CONFIG
from spider.cache import SpiderCache
from spider.session import SpiderSession


class Controller():
    def __init__(self, cache, session):
        self.cache = cache
        self.session = session

    def make_options(self, url):
        options = {'url': url, 'headers': {}}
        if self.session.is_login():
            self.sign_options(options, self.session.get_user())
        return options

    def sign_options(self, options, user):
        options['headers']['Cookie'] = 'LEETCODE_SESSION=' + user['sessionId'] + ';csrftoken=' + user['sessionCSRF'] + ';'
        options['headers']['X-CSRFToken'] = user['sessionCSRF']
        options['headers']['X-Requested-With'] = 'XMLHttpRequest'

    def login(self, user):
        pass

    def singin(self, user):
        req = requests.request('GET', DEFAULT_CONFIG['sys']['urls']['login'])
        user['loginCSRF'] = req.cookies.get('csrftoken')
        options = {
            'url': DEFAULT_CONFIG['sys']['urls']['login'],
            'headers': {
                'Origin': DEFAULT_CONFIG['sys']['urls']['base'],
                'Referer': DEFAULT_CONFIG['sys']['urls']['login'],
                'Cookie': 'csrftoken=' + user['loginCSRF'] + ';'
            },
            'form': {
                'csrfmiddlewaretoken': user['loginCSRF'],
                'login': user['login'],
                'password': user['pass']
            }
        }
        req = requests.request('POST', options['url'], data=options['form'], headers=options['headers'])
        user['sessionCSRF'] = req.cookies.get('csrftoken')
        user['sessionId'] = req.cookies.get('LEETCODE_SESSION')
        self.session.save_user(user)
        return user


if __name__ == '__main__':
    cache = SpiderCache()
    session = SpiderSession(cache)
    controller = Controller(cache, session)
    user = {
        'login': 'zhipenghao930930@gmail.com',
        'pass': 'peqxe4-jihtez-noVwez'
    }
    controller.singin(user)
