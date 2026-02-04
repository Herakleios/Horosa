import json
from datetime import datetime

from skyfield.elementslib import eccentricity

from calculator_liuren.constant.concept import TianGan, DiZhi
from calculator_liuren.units.calendar import get_liuren_datetime, get_chinese_day, calculate_years_old, get_chinese_datetime, is_light
from calculator_liuren.units.lessons import Lessons
from calculator_liuren.units.passes import Passes
from calculator_liuren.units.plane import Plane
from calculator_liuren.units.shensha import find_deity
from calculator_liuren.units.xun import Xun
from rich import print as rich_print


class XunResult:
    def __init__(self, xun: Xun):
        self.start = xun.start.value
        self.end = xun.end.value
        self.ding = xun.ding.value
        self.empty = [i.value for i in xun.empty]


class LiurenResult:
    def __init__(self, current_date: datetime, plane: Plane, lessons: Lessons, passes: Passes, xun: Xun):
        def format_none(value):
            return '空' if value is None else value.value

        tian_jiang = [tj.value[1] for tj in plane.tian_jiang]
        equatorial = [eq.value for eq in plane.equatorial_plane]
        ecliptic = [ec.value for ec in plane.ecliptic_plane]

        self.ecliptic = ecliptic
        self.equatorial = equatorial
        self.tian_jiang = tian_jiang

        self.datetime = get_chinese_datetime(current_date)
        self.shishen = []
        for i in range(12):
            _xun = format_none(plane.xun[i])
            self.shishen.append([
                equatorial[i], ecliptic[i], _xun, tian_jiang[i]])

        self.lesson = []
        l = [lessons.first, lessons.second, lessons.third, lessons.fourth]
        for i in range(4):
            _xun = format_none(l[i][2])
            _jiang = l[i][3].value[1]
            self.lesson.append([l[i][0].value, l[i][1].value, _jiang, _xun])

        self.passes = []
        for i in range(3):
            _xun = format_none(passes.xun[i])
            _jiang = passes.tian_jiang[i].value[1]
            # 六亲
            _wuxing = passes.wuxing[i].value[2]
            self.passes.append([passes.three[i].value, _jiang, _wuxing, _xun])

        self.major = passes.major_category
        self.sub = passes.sub_category

        self.xun = XunResult(xun)
        self.month = plane.month.value

        self.ben = None
        self.xing = None

    def inject_ming(self, ben: tuple[TianGan, DiZhi], xing: tuple[TianGan, DiZhi]):
        """
        注入本命，行年
        """
        self.ben = [ben[0].value, ben[1].value]
        self.xing = [xing[0].value, xing[1].value]


def calculate_liuren(date: datetime, birth: datetime = None, male: bool = None, light: bool = None) -> LiurenResult:
    """
    计算六壬
    入参：
        day: 日期
    返回：
        六壬结果
    """
    # 计算 月将，日干支，时将
    _month, _day, _hour = get_liuren_datetime(date)

    # 生成式盘
    plane = Plane.generate(_month, _hour)
    # 寻找太乙贵人
    if light is None:
        light = is_light(_hour)
    deity = find_deity(_day[0], light)
    # 注入天将
    plane.inject_tian_jiang(deity)
    # 计算遁干
    xun = Xun.calculate(_day[0], _day[1])
    # 注入旬日
    plane.inject_xun(xun)

    # 推演四课
    lessons = Lessons.derive(plane, _day[0], _day[1])

    # 发三传
    passes = Passes.derive(plane, lessons)

    result = LiurenResult(date, plane, lessons, passes, xun)

    # 计算本命，行年
    ben, xing = None, None
    if birth is not None and male is not None:
        ben = get_chinese_day(birth)
        xing = calculate_years_old(birth, male)
        result.inject_ming(ben, xing)

    # TODO：众煞

    return result


def old_format(liuren: LiurenResult) -> dict:
    """
    格式化六壬结果（旧）
    """
    d, p, l = liuren.datetime, liuren.passes, liuren.lesson
    m = liuren.month
    m_i = liuren.equatorial.index(m)

    _tj = liuren.tian_jiang[m_i:] + liuren.tian_jiang[:m_i]
    _eq = liuren.equatorial[m_i:] + liuren.equatorial[:m_i]
    _ec = liuren.ecliptic[m_i:] + liuren.ecliptic[:m_i]

    _xun = []
    for i in range(12):
        _xun.append(liuren.shishen[i][2])
    _x = _xun[m_i:] + _xun[:m_i]

    return {
        '日期': f'{d[2]}日{d[3][1]}时',
        '格局': [liuren.major, liuren.sub],
        '三传': {
            '初传': p[0],
            '中传': p[1],
            '末传': p[2],
        },
        '四课': {
            '四课': [f'{l[3][0]}{l[3][1]}', l[3][2]],
            '三课': [f'{l[2][0]}{l[2][1]}', l[2][2]],
            '二课': [f'{l[1][0]}{l[1][1]}', l[1][2]],
            '一课': [f'{l[0][0]}{l[0][1]}', l[0][2]],
        },
        '地转天盘': {_eq[i]: _ec[i] for i in range(12)},
        '地转天将': {_eq[i]: _tj[i] for i in range(12)},
        '地转天干': {_eq[i]: _x[i] for i in range(12)},
        '月将': m,
    }


def new_format(liuren: LiurenResult) -> dict:
    """
    格式化六壬结果（新）
    """
    return {
        '日期': liuren.datetime,
        '课体': [liuren.major, liuren.sub],
        '式盘': liuren.shishen,
        '四课': liuren.lesson,
        '三传': liuren.passes,
        '旬': {
            '旬首': liuren.xun.start,
            '旬尾': liuren.xun.end,
            '旬丁': liuren.xun.ding,
            '旬空': liuren.xun.empty
        },
        '月将': liuren.month,
        '本命': liuren.ben if liuren.ben is not None else '无',
        '行年': liuren.xing if liuren.xing is not None else '无'
    }


if __name__ == '__main__':
    year, month, day, hour, minute = 2024, 1, 20, 22, 7
    result = calculate_liuren(datetime(year, month, day, hour, minute))

    # 旧结构格式化输出
    rich_print(old_format(result))
    # 新结构格式化输出
    rich_print(new_format(result))

    # 旧结构正常输入
    print(old_format(result))
    # 新结构正常输入
    print(new_format(result))
