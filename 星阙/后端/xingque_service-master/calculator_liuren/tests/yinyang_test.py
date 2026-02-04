from constant.concept import TianGan, DiZhi
from units.yinyang import is_same_yin_yang


def test_same_yin_yang():
    assert is_same_yin_yang(TianGan.Jia, DiZhi.Zi)
    assert is_same_yin_yang(TianGan.Yi, DiZhi.Chou)
