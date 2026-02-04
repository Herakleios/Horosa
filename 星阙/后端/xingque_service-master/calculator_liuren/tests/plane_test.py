from datetime import datetime

from constant.concept import DiZhi, WuXingRelation, TianGan, TianJiang
from units.calendar import get_chinese_datetime, get_liuren_datetime, is_light
from units.plane import Plane
from units.shensha import find_deity
from units.xun import Xun


def test_transmission():
    from units.plane import Plane
    # 午未申酉戌亥子丑寅卯辰巳
    # 戌亥子丑寅卯辰巳午未申酉
    plane = Plane.generate(DiZhi.Wu, DiZhi.Shen)

    assert plane.transmission(DiZhi.Zi) == DiZhi.Xu
    assert plane.transmission(DiZhi.Chou) == DiZhi.Hai
    assert plane.transmission(DiZhi.Yin) == DiZhi.Zi
    assert plane.transmission(DiZhi.Mao) == DiZhi.Chou
    assert plane.transmission(DiZhi.Chen) == DiZhi.Yin
    assert plane.transmission(DiZhi.Si) == DiZhi.Mao
    assert plane.transmission(DiZhi.Wu) == DiZhi.Chen
    assert plane.transmission(DiZhi.Wei) == DiZhi.Si
    assert plane.transmission(DiZhi.Shen) == DiZhi.Wu
    assert plane.transmission(DiZhi.You) == DiZhi.Wei
    assert plane.transmission(DiZhi.Xu) == DiZhi.Shen
    assert plane.transmission(DiZhi.Hai) == DiZhi.You


def test_count_overcome():
    from units.plane import Plane

    # 午未申酉戌亥子丑寅卯辰巳
    # 戌亥子丑寅卯辰巳午未申酉
    plane = Plane.generate(DiZhi.Wu, DiZhi.Shen)
    assert plane.count_deep(DiZhi.Chou, WuXingRelation.Overcome) == 2
    assert plane.count_deep(DiZhi.Hai, WuXingRelation.Overcome) == 6


# 测试对齐天将
def test_alignment_gui():
    month, day, hour = get_liuren_datetime(datetime(2019, 2, 8, 22, 55))
    plane = Plane.generate(month, hour)
    deity = find_deity(day[0], is_light(hour))
    plane.inject_tian_jiang(deity)
    assert plane.get_tian_jiang(DiZhi.Zi) == TianJiang.XuanWu

    month, day, hour = get_liuren_datetime(datetime(2019, 2, 8, 9, 55))
    plane = Plane.generate(month, hour)
    deity = find_deity(day[0], is_light(hour))
    plane.inject_tian_jiang(deity)
    assert plane.get_tian_jiang(DiZhi.Zi) == TianJiang.TengShe


# 测试遁干
def test_retreated_tian_gan():
    plane = Plane.generate(DiZhi.Yin, DiZhi.Zi)
    plane.inject_xun(Xun.calculate(TianGan.Xin, DiZhi.Chou))
    assert plane.xun[0] == TianGan.Ren
    assert plane.xun[1] == TianGan.Gui
    assert plane.xun[2] is None
    assert plane.xun[3] is None
    assert plane.xun[4] == TianGan.Jia
