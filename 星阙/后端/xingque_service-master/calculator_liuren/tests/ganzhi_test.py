from doctest import DocTest

from constant.concept import TianGan, WuXing, DiZhi


def test_derive_lodging_dizhi_from_tiangan():
    from units.ganzhi import derive_lodging_dizhi_from_tiangan
    from constant.concept import lodge_relation

    for tiangan, dizhi in lodge_relation.items():
        assert derive_lodging_dizhi_from_tiangan(tiangan) == dizhi

def test_get_tg_dz_wuxing():
    from units.ganzhi import get_wuxing_by
    assert get_wuxing_by(TianGan.Jia) == WuXing.Wood
    assert get_wuxing_by(DiZhi.Zi) == WuXing.Water

