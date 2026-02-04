# 公用函数
from enum import Enum
from typing import Type

from calculator_liuren.constant.concept import DiZhi, restrained_relation, TianGan, dizhi_order, tiangan_order
from calculator_liuren.tools.enums import get_enum_index, get_enum_by_index


def find_restrained(target: DiZhi) -> DiZhi:
    """
    寻找所刑的地支
    入参：
        target: 地支
    返回:
        所刑的地支
    """
    return restrained_relation[target]


def find_clashed(target: DiZhi) -> DiZhi:
    """
    寻找所冲的地支
    入参：
        target: 地支
    返回:
        所冲的地支
    """

    index = get_enum_index(target)

    if index <= 5:
        return get_enum_by_index(DiZhi, index + 6)
    else:
        return get_enum_by_index(DiZhi, index - 6)


def is_self_restrained(target: DiZhi) -> bool:
    """
    判断是否自刑
    入参：
        target: 地支
    返回:
        是否自刑
    """
    return target == find_restrained(target)

def is_restrained(target: DiZhi, source: DiZhi) -> bool:
    """
    判断是否互刑
    入参：
        target: 地支
        source: 地支
    返回:
        是否被所刑
    """
    return (target == DiZhi.Zi and source == DiZhi.Mao) or (target == DiZhi.Mao and source == DiZhi.Zi)


def find_tg_union(tg: TianGan) -> TianGan:
    """
    获取天干的相合天干
    入参：
        tg: 天干
    返回：
        所合天干
    """
    _index = get_enum_index(tg)

    return get_enum_by_index(TianGan, _index - 5) if _index >= 5 else get_enum_by_index(TianGan, _index + 5)


def find_dz_union(dz: DiZhi) -> DiZhi:
    """
    获取地支的相合地支
    入参：
        dz: 地支
    返回：
        相合地支
    """

    _index = get_enum_index(dz)

    return find_gz_by_offset(dz, 4)


def rotate_gz_order(e: Type[TianGan | DiZhi], start: int) -> list[DiZhi | TianGan]:
    """
    旋转地支顺序(顺时针)
    """
    if e == TianGan:
        if start == 0:
            return tiangan_order

        _offset = -(start % 10)
        return tiangan_order[_offset:] + tiangan_order[:_offset]
    else:
        if start == 0:
            return dizhi_order

        _offset = -(start % 12)
        return dizhi_order[_offset:] + dizhi_order[:_offset]


def find_gz_by_offset(gz: DiZhi | TianGan, offset: int) -> DiZhi:
    """
    获取干支的偏移地支
    入参：
        gz: 干支
        offset: 偏移量
    返回：
        偏移地支
    """

    return rotate_gz_order(gz.__class__, -offset)[get_enum_index(gz)]
