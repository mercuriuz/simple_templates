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


def get_solution_dir():
    return '/'.join(['..', 'solutions'])


def get_resources_dir():
    return '/'.join(['..', 'resources'])


def get_resource_file(key):
    return '/'.join([get_resources_dir(), key])


def format_id(id):
    if id < 10:
        return '00{}'.format(id)
    elif id < 100:
        return '0{}'.format(id)
    else:
        return '{}'.format(id)


if __name__ == '__main__':
    print(get_user_home_dir())
    print(get_home_dir())
    print(get_cache_dir())
    print(get_cache_file('hello'))
    print(get_resources_dir())
    print(get_resource_file('README.tpl'))
    print(get_solution_dir())
    print(int('010'))
    a = './../solutions/345.reverse-vowels-of-a-string/reverse-vowels-of-a-string.py'
    print(a.replace('../', ''))