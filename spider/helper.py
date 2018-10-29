import os


def mkdir(full_path):
    if (os.path.exists(full_path)):
        return
    os.mkdir(full_path)


def get_cache_file(key):
    return '/'.join([get_cache_dir(), key + '.json'])


def get_cache_dir():
    return '/'.join([get_home_dir(), 'cache'])


def get_home_dir():
    return '/'.join([get_user_home_dir(), '.lc'])


def get_user_home_dir():
    return os.getenv('HOME')


if __name__ == '__main__':
    print(get_user_home_dir())
    print(get_home_dir())
    print(get_cache_dir())
    print(get_cache_file('hello'))
