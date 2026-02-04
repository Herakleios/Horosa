from constant.concept import DiZhi, TianGan
from units.common import find_clashed, find_tg_union, find_dz_union, find_gz_by_offset, rotate_gz_order


# 测试地支相冲
def test_find_clashed():
    assert find_clashed(DiZhi.Zi) == DiZhi.Wu
    assert find_clashed(DiZhi.Chou) == DiZhi.Wei
    assert find_clashed(DiZhi.Yin) == DiZhi.Shen
    assert find_clashed(DiZhi.Mao) == DiZhi.You
    assert find_clashed(DiZhi.Chen) == DiZhi.Xu
    assert find_clashed(DiZhi.Si) == DiZhi.Hai
    assert find_clashed(DiZhi.Wu) == DiZhi.Zi
    assert find_clashed(DiZhi.Wei) == DiZhi.Chou
    assert find_clashed(DiZhi.Shen) == DiZhi.Yin
    assert find_clashed(DiZhi.You) == DiZhi.Mao
    assert find_clashed(DiZhi.Xu) == DiZhi.Chen
    assert find_clashed(DiZhi.Hai) == DiZhi.Si


# 测试天干相合
def test_find_tg_union():
    assert find_tg_union(TianGan.Jia) == TianGan.Ji
    assert find_tg_union(TianGan.Yi) == TianGan.Geng
    assert find_tg_union(TianGan.Bing) == TianGan.Xin
    assert find_tg_union(TianGan.Ding) == TianGan.Ren
    assert find_tg_union(TianGan.Wu) == TianGan.Gui

    assert find_tg_union(TianGan.Ji) == TianGan.Jia
    assert find_tg_union(TianGan.Geng) == TianGan.Yi
    assert find_tg_union(TianGan.Xin) == TianGan.Bing
    assert find_tg_union(TianGan.Ren) == TianGan.Ding
    assert find_tg_union(TianGan.Gui) == TianGan.Wu


# 测试地支相合
def test_find_dz_union():
    assert find_dz_union(DiZhi.Zi) == DiZhi.Chen
    assert find_dz_union(DiZhi.Chou) == DiZhi.Si
    assert find_dz_union(DiZhi.Yin) == DiZhi.Wu
    assert find_dz_union(DiZhi.Mao) == DiZhi.Wei
    assert find_dz_union(DiZhi.Chen) == DiZhi.Shen
    assert find_dz_union(DiZhi.Si) == DiZhi.You
    assert find_dz_union(DiZhi.Wu) == DiZhi.Xu
    assert find_dz_union(DiZhi.Wei) == DiZhi.Hai
    assert find_dz_union(DiZhi.Shen) == DiZhi.Zi
    assert find_dz_union(DiZhi.You) == DiZhi.Chou
    assert find_dz_union(DiZhi.Xu) == DiZhi.Yin
    assert find_dz_union(DiZhi.Hai) == DiZhi.Mao


# 测试地支偏移
def test_find_gz_by_offset():
    assert find_gz_by_offset(DiZhi.Hai, 2) == DiZhi.Chou
    assert find_gz_by_offset(DiZhi.Chou, -2) == DiZhi.Hai

def test_rotate():
    assert rotate_gz_order(DiZhi, -2)[0] == DiZhi.Yin