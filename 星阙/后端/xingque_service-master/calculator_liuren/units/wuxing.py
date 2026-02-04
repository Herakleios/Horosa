from calculator_liuren.constant.concept import WuXing, WuXingRelation, wuxing_relations
from calculator_liuren.tools.enums import get_enum_index


def relation(a: WuXing, b: WuXing, season: WuXing = None) -> WuXingRelation:
    """
    判断两个给定的五行元素之间的关系。

    参数:
        a (str): 第一个元素。
        b (str): 第二个元素。

    返回:
        str: 两个元素之间的关系。
    """
    if season is not None and a == season:
        return WuXingRelation.Mutual

    a_index = get_enum_index(a)
    b_index = get_enum_index(b)

    return wuxing_relations[(b_index - a_index) % 5]
