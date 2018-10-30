DEFAULT_CONFIG = {
    'sys': {
        'categories': [
            'algorithms',
            'database',
            'shell'
        ],
        'langs': [
            # 'bash',
            # 'c',
            # 'cpp',
            # 'csharp',
            # 'golang',
            # 'java',
            # 'javascript',
            # 'kotlin',
            # 'mysql',
            # 'python',
            'python3',
            # 'ruby',
            # 'scala',
            # 'swift'
        ],
        'urls': {
            'base': 'https://leetcode-cn.com',
            'graphql': 'https://leetcode-cn.com/graphql',
            'login': 'https://leetcode-cn.com/accounts/login/',
            'problems': 'https://leetcode-cn.com/api/problems/$category/',
            'problem': 'https://leetcode-cn.com/problems/',
            'algorithm': 'https://leetcode-cn.com/api/problems/algorithms/',
            # 'problem': 'https://leetcode-cn.com/problems/$slug/description/',
            'test': 'https://leetcode-cn.com/problems/$slug/interpret_solution/',
            'session': 'https://leetcode-cn.com/session/',
            'submit': 'https://leetcode-cn.com/problems/$slug/submit/',
            'submissions': 'https://leetcode-cn.com/api/submissions/$slug',
            'solution': 'https://leetcode-cn.com/api/submissions/',
            'submission': 'https://leetcode-cn.com/submissions/detail/$id/',
            'verify': 'https://leetcode-cn.com/submissions/detail/$id/check/',
            'favorites': 'https://leetcode-cn.com/list/api/questions',
            'favorite_delete': 'https://leetcode-cn.com/list/api/questions/$hash/$id',
        }
    },
    'autologin': {
        'enable': False,
        'retry': 2
    },
    'code': {
        'editor': 'vim',
        'lang': 'cpp'
    },
    'color': {
        'enable': True,
        'theme': 'default'
    },
    'icon': {
        'theme': ''
    },
    'network': {
        'concurrency': 10
    },
    'plugins': {}
}

keys = {
    'solution': '../solution',
    'user': '../user',
    'stat': '../stat',
    'problems': 'problems'
}