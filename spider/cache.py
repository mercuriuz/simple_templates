from spider.helper import mkdir, get_cache_dir, get_cache_file
import os
import json


class SpiderCache():
    def __init__(self):
        mkdir(get_cache_dir())

    def get(self, key):
        full_path = get_cache_file(key)
        if not os.path.exists(full_path):
            return None
        with open(full_path, 'r') as f:
            return json.load(f)

    def set(self, key, value):
        full_path = get_cache_file(key)
        with open(full_path, 'w') as f:
            json.dump(value, f)
        return True

    def delete(self, key):
        full_path = get_cache_file(key)
        if not os.path.exists(full_path):
            return False
        os.remove(full_path)
        return True


if __name__ == '__main__':
    cache = SpiderCache()
    print(cache.get('abc') is None)
    input()
    cache.set('abc', 'hh')
    print(cache.get('abc') is None)
    input()
    cache.delete('abc')
    print(cache.get('abc') is None)
