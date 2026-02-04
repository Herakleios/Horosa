from datetime import datetime, timedelta

from lunar_python import Lunar

from calculator_liuren.constant.concept import DiZhi, TianGan, tiangan_order, dizhi_order, SolarTerm, solar_terms_map, dizhi_map, \
    tiangan_map
from calculator_liuren.tools.enums import get_enum_index

from calculator_liuren.units.common import rotate_gz_order

# 定义时辰和对应的时间范围
chinese_hours = [
    (DiZhi.Zi, 23, 0),
    (DiZhi.Chou, 1, 2),
    (DiZhi.Yin, 3, 4),
    (DiZhi.Mao, 5, 6),
    (DiZhi.Chen, 7, 8),
    (DiZhi.Si, 9, 10),
    (DiZhi.Wu, 11, 12),
    (DiZhi.Wei, 13, 14),
    (DiZhi.Shen, 15, 16),
    (DiZhi.You, 17, 18),
    (DiZhi.Xu, 19, 20),
    (DiZhi.Hai, 21, 22)
]


def is_light(hour: DiZhi) -> bool:
    """
    判断现在是否为白天。
    从卯时到酉时为白天，否则为晚上。
    """
    _index = get_enum_index(hour)
    return 3 <= _index <= 8


def get_solar_term(now: datetime = datetime.now()) -> SolarTerm:
    """
    获取当前节气

    入参：
        now: 当前时间
    返回：
        当前节气
    """
    lunar = Lunar.fromDate(now)
    solar_term = lunar.getPrevJieQi().toString()
    return solar_terms_map[solar_term]


def calculate_chun_fen(year: int) -> datetime:
    """
    计算春分日期时间

    入参：
        year: 年份
    返回：
        春分日期时间
    """

    d = Lunar.fromDate(datetime(year, 1, 1))
    lichun = d.getJieQiTable()['立春'].toYmdHms()
    _time = datetime.strptime(lichun, '%Y-%m-%d %H:%M:%S')
    return _time


def get_chinese_hour(day: datetime = datetime.now()) -> tuple[TianGan, DiZhi]:
    """
    获取当前时辰。
    """

    lunar = Lunar.fromDate(day)
    hour_str = lunar.getTimeInGanZhi()
    return tiangan_map[hour_str[0]], dizhi_map[hour_str[1]]


def get_chinese_year(dt: datetime = datetime.now()) -> tuple[TianGan, DiZhi]:
    """
    获取农历年份。
    """
    # 农历年份的计算方法为：1900年为庚子年，以此类推
    lunar = Lunar.fromDate(dt)
    gz = lunar.getYearInGanZhi()

    return tiangan_map[gz[0]], dizhi_map[gz[1]]


base_day = datetime(1900, 1, 1)


def get_chinese_day(day: datetime = datetime.now) -> tuple[TianGan, DiZhi]:
    """
    获取农历日期
    """
    # 计算当前日期与基准日期的差值
    if day.hour == 23:
        lunar = Lunar.fromDate(day + timedelta(days=1))
    else:
        lunar = Lunar.fromDate(day)

    gz = lunar.getDayInGanZhi()
    return tiangan_map[gz[0]], dizhi_map[gz[1]]


def get_month(date: datetime) -> DiZhi:
    """
    获取月将
    """
    return get_solar_term(date).value[2]


def get_liuren_datetime(day: datetime = datetime.now()) -> tuple[DiZhi, tuple[TianGan, DiZhi], DiZhi]:
    """
    获取月将，日干，日支和时将

    入参：
        day: 当前时间
    返回：
        月将，(日干，日支)和时将

    """
    month = get_month(day)
    chinese_day = get_chinese_day(day)
    hour = get_chinese_hour(day)[1]
    return month, chinese_day, hour


def calculate_years_old(birth: datetime, male: bool) -> tuple[TianGan, DiZhi]:
    """
    计算行年

    入参：
        birth: 出生日期
        male: 是否男性

    返回：
        行年
    """
    year, month, day = birth.year, birth.month, birth.day

    begin = [TianGan.Bing, DiZhi.Yin] if male else [TianGan.Ren, DiZhi.Shen]

    tg_index = get_enum_index(begin[0])
    tian_gan = tiangan_order[tg_index:] + tiangan_order[:tg_index]
    dz_index = get_enum_index(begin[1])
    di_zhi = dizhi_order[dz_index:] + dizhi_order[:dz_index]

    # 计算当前立春时间
    lichun = calculate_chun_fen(year)

    # 计算年龄差
    year = year - 1 if birth < lichun else year
    current_year = datetime.now().year
    distance = current_year - year

    if male:
        return tian_gan[distance % 10], di_zhi[distance % 12]
    else:
        return tian_gan[-distance % 10], di_zhi[-distance % 12]


def get_chinese_datetime(current_datetime: datetime) -> list[str]:
    """
    获取农历日期时间

    入参：
        current_datetime: 当前时间
    返回：
        农历日期时间
    """
    lunar = Lunar.fromDate(current_datetime)
    return [lunar.getYearInGanZhi(), lunar.getMonthInGanZhi(), lunar.getDayInGanZhi(), lunar.getTimeInGanZhi()]