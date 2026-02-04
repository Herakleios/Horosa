from datetime import datetime

from units.calendar import is_light, get_chinese_hour
from constant.concept import DiZhi, TianGan


# 测试寻找太乙贵人
def test_find_tai_yi_gui_ren():
    from units.shensha import find_deity

    if is_light(get_chinese_hour()[1]):
        assert find_deity(TianGan.Jia) == DiZhi.Wei
        assert find_deity(TianGan.Yi) == DiZhi.Shen
        assert find_deity(TianGan.Bing) == DiZhi.You
        assert find_deity(TianGan.Ding) == DiZhi.Hai
        assert find_deity(TianGan.Wu) == DiZhi.Chou
        assert find_deity(TianGan.Ji) == DiZhi.Zi
        assert find_deity(TianGan.Geng) == DiZhi.Chou
        assert find_deity(TianGan.Xin) == DiZhi.Yin
        assert find_deity(TianGan.Ren) == DiZhi.Mao
        assert find_deity(TianGan.Gui) == DiZhi.Si
    else:
        assert find_deity(TianGan.Jia) == DiZhi.Chou
        assert find_deity(TianGan.Yi) == DiZhi.Zi
        assert find_deity(TianGan.Bing) == DiZhi.Hai
        assert find_deity(TianGan.Ding) == DiZhi.You
        assert find_deity(TianGan.Wu) == DiZhi.Wei
        assert find_deity(TianGan.Ji) == DiZhi.Shen
        assert find_deity(TianGan.Geng) == DiZhi.Wei
        assert find_deity(TianGan.Xin) == DiZhi.Wu
        assert find_deity(TianGan.Ren) == DiZhi.Si
        assert find_deity(TianGan.Gui) == DiZhi.Mao
