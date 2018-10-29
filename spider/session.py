from spider.config import keys
from spider.cache import SpiderCache


class SpiderSession():
    def __init__(self, cache):
        self.cache = cache

    def get_user(self):
        return self.cache.get(keys['user'])

    def save_user(self, user):
        self.cache.set(keys['user'], user)

    def delete_user(self):
        self.cache.delete(keys['user'])

    def delete_coding_session(self):
        self.cache.deleet(keys['problems'])

    def is_login(self):
        return self.get_user() is not None

    def update_stat(self, key, value):
        pass


if __name__ == '__main__':
    cache = SpiderCache()
    session = SpiderSession(cache)
    print(session.get_user())
