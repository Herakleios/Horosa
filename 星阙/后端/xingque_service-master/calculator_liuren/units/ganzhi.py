# 天干地支

from calculator_liuren.constant.concept import lodge_relation, TianGan, WuXing, DiZhi, dizhi_wuxing_relation, \
    tiangan_wuxing_relation, invert_lodge_relation
from calculator_liuren.tools.enums import get_enum_index


def get_wuxing_by(target: TianGan | DiZhi) -> WuXing:
    """
    获取天干地支的五行。

    参数:
        target (TianGan | DiZhi): 天干或地支

    返回:
        WuXing: 五行。
    """

    if isinstance(target, TianGan):
        return tiangan_wuxing_relation[target]
    else:
        return dizhi_wuxing_relation[target]


def get_lodging_dizhi_from_tiangan(tg: TianGan) -> DiZhi:
    """
    获取天干寄居的地支。

    参数:
        tg (str): 天干

    返回:
        str: 寄居的地支。
    """
    return lodge_relation[tg]


def get_tiangan_by_lodging_dizhi(dz: DiZhi) -> list[TianGan] | None:
    """
    获取地支对应的天干。

    参数:
        dz (str): 地支

    返回:
        str: 对应的天干。
    """
    if dz in invert_lodge_relation:
        return invert_lodge_relation[dz]
    else:
        return None


def derive_lodging_dizhi_from_tiangan(tg: TianGan) -> DiZhi:
    """
    推算天干寄居的地支,仅测试用。

    参数:
        tg (str): 天干

    返回:
        str: 寄居的地支。
    """

    # 获取天干的五行
    _wuxing = get_wuxing_by(tg)
    # 获取天干的索引
    index = get_enum_index(tg)

    # 阳干取对应五行代表的季节的首月对应的地支
    # 阴干取对应五行代表的季节的末月对应的地支
    _dizhi = ''
    if index % 2 == 0:
        _dizhi = (WuXing.Fire if _wuxing == WuXing.Earth else _wuxing).value.dizhi[0]
    else:
        rule = [WuXing.Wood, WuXing.Fire, WuXing.Metal, WuXing.Water]
        season_index = 1 if _wuxing == WuXing.Earth else rule.index(_wuxing)
        _dizhi = WuXing.Earth.value.dizhi[season_index]

    return _dizhi
