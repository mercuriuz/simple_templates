from functools import reduce


def calculate(nums, val):
    cache_data = {}
    results = {}
    for num in nums:
        if cache_data.get(val - num) is not None:
            results[(num, val - num)] = 1
        else:
            cache_data[num] = 1
    return results.keys() if len(results.keys()) > 0 else 0


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 5, 6, 7]
    val = 111
    print(calculate(nums, val))

    demo = [1461.56, 1169.13, 3605.05, 1056.90, 3151.86, 500, 500]
    debt = reduce(lambda x, y: x + y, demo)
    print(debt)
