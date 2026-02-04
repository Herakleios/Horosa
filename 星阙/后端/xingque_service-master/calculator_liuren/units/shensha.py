# 神煞

from calculator_liuren.constant.concept import DiZhi, TianGan, day_or_night_order
from calculator_liuren.units.calendar import get_chinese_hour, is_light


def find_deity(day_tg: TianGan, light: bool = is_light(get_chinese_hour()[1])) -> DiZhi:
    """
    寻找太乙贵人
    """
    return day_or_night_order[day_tg][0 if light else 1]


def find_horse(day_dz: DiZhi) -> DiZhi:
    """
    寻找驿马
    入参：
        day_dz: 日支
    返回:
        驿马
    """

    if day_dz in [DiZhi.Hai, DiZhi.Mao, DiZhi.Wei]:
        return DiZhi.Si
    elif day_dz in [DiZhi.Si, DiZhi.You, DiZhi.Chou]:
        return DiZhi.Hai
    elif day_dz in [DiZhi.Yin, DiZhi.Wu, DiZhi.Xu]:
        return DiZhi.Shen
    else:
        return DiZhi.Yin

