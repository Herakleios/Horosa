from constant.concept import DiZhi, Flow, WuXingRelation
from units.energy import flow, power


def test_get_flow():
    assert flow(DiZhi.Shen, DiZhi.Si) == Flow.ChangSheng
    assert flow(DiZhi.Yin, DiZhi.Hai) == Flow.ChangSheng
    assert flow(DiZhi.Si, DiZhi.Yin) == Flow.ChangSheng
    assert flow(DiZhi.Hai, DiZhi.Shen) == Flow.ChangSheng
    assert flow(DiZhi.Chen, DiZhi.Shen) == Flow.ChangSheng


def test_get_power():
    assert power(DiZhi.Chen) == WuXingRelation.Mutual
    assert power(DiZhi.Xu) == WuXingRelation.Mutual
    assert power(DiZhi.Chou) == WuXingRelation.Mutual
    assert power(DiZhi.Wei) == WuXingRelation.Mutual
