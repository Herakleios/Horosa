from datetime import datetime

from calculator_liuren.constant.concept import DiZhi, WuXing, Flow, WuXingRelation, Season
from calculator_liuren.tools.enums import get_enum_by_index
from calculator_liuren.units.common import rotate_gz_order
from calculator_liuren.units.ganzhi import get_wuxing_by
from calculator_liuren.units.wuxing import relation

offset_map = {
    WuXing.Wood: 1,
    WuXing.Fire: -2,
    WuXing.Earth: 4,
    WuXing.Metal: -5,
    WuXing.Water: 4
}


def flow(a: DiZhi, b: DiZhi) -> Flow:
    """
    判断两个地支之间的气势关系。

    参数:
        a (DiZhi): 地支
        b (DiZhi): 地支


    返回:
        Flow: 两个地支之间的气势关系。
    """
    order = rotate_gz_order(DiZhi, offset_map[get_wuxing_by(a)])
    return get_enum_by_index(Flow, order.index(b))


month_wuxing = [
    WuXing.Wood,
    WuXing.Wood,
    WuXing.Fire,
    WuXing.Fire,
    WuXing.Metal,
    WuXing.Metal,
    WuXing.Water,
    WuXing.Water,
    WuXing.Earth,
    WuXing.Earth,
    WuXing.Earth,
    WuXing.Metal
]


def power(target: DiZhi) -> WuXingRelation:
    month = datetime.now().month
    season = month // 3

    a_wuxing = get_wuxing_by(target)
    b_wuxing = month_wuxing[month - 1]
    if b_wuxing is WuXing.Earth:
        return relation(a_wuxing, b_wuxing, get_enum_by_index(Season, season))
    else:
        return relation(a_wuxing, b_wuxing)