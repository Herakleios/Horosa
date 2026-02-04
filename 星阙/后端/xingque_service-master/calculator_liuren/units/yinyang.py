from calculator_liuren.constant.concept import TianGan, DiZhi
from calculator_liuren.tools.enums import get_enum_index


def is_yang(target: TianGan | DiZhi) -> bool:
    """
    判断是否为阳干或阳支
    入参：
        target: 干支
    返回:
        是否为阳干或阳支
    """
    return get_enum_index(target) % 2 == 0


def is_yin(target: TianGan | DiZhi) -> bool:
    """
    判断是否为阴干或阴支
    入参：
        target: 干支
    返回:
        是否为阴干或阴支
    """
    return get_enum_index(target) % 2 == 1


def is_same_yin_yang(a: TianGan | DiZhi, b: TianGan | DiZhi) -> bool:
    """
    判断两个干支是否同阴阳
    入参：
        a: 干支
        b: 干支
    返回:
        是否同阴阳
    """
    return is_yin(a) == is_yin(b)
