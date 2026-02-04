from datetime import datetime

from lib import calculate_liuren, old_format


def test_bug_fix_91801():
    result = calculate_liuren(datetime(2019, 2, 8, 9, 55))
    assert result.lesson[0][3] == '蛇'
    assert result.lesson[1][3] == '常'
    assert result.lesson[2][3] == '常'
    assert result.lesson[3][3] == '合'


def test_bug_fix_91802():
    result = calculate_liuren(datetime(2024, 7, 3, 0, 55))
    assert result.major == '涉害'


def test_bug_fix_91803():
    result = calculate_liuren(datetime(2024, 5, 10, 0, 55))
    assert result.lesson[0][3] == '常'
    assert result.lesson[1][3] == '后'
    assert result.lesson[2][3] == '贵'
    assert result.lesson[3][3] == '合'


def test_bug_fix_91804():
    result = calculate_liuren(datetime(2023, 9, 17, 1, 7))
    assert result.major == '昴星'
    result = calculate_liuren(datetime(2024, 4, 13, 1, 7))
    assert result.major == '八专'


def test_bug_fix_91805():
    result = calculate_liuren(datetime(2024, 7, 3, 14, 55))
    assert result.major == '伏吟'
    assert result.sub == '自任'

    result = calculate_liuren(datetime(2024, 2, 20, 22, 10))
    assert result.major == '伏吟'
    assert result.sub == '自任'

    result = calculate_liuren(datetime(2023, 4, 16, 19, 55))
    assert result.major == '伏吟'
    assert result.sub == '自任'

    result = calculate_liuren(datetime(2023, 4, 29, 17, 55))
    assert result.major == '伏吟'
    assert result.sub == '自信'

    result = calculate_liuren(datetime(2024, 8, 13, 12, 55))
    assert result.major == '伏吟'
    assert result.sub == '杜传'

    result = calculate_liuren(datetime(2023, 3, 25, 19, 55))
    assert result.major == '伏吟'
    assert result.sub == '不虞'


def test_bug_fix_91806():
    result = calculate_liuren(datetime(2024, 8, 12, 4, 7))
    assert result.major == '贼克'
    assert result.sub == '元首'

    result = calculate_liuren(datetime(2024, 5, 26, 9, 7))
    assert result.major == '贼克'
    assert result.sub == '重审'
