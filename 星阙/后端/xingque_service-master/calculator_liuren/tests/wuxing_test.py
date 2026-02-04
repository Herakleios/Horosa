from constant.concept import WuXing, WuXingRelation
from units.wuxing import relation


def test_relation():
    # 木生火
    assert relation(WuXing.Wood, WuXing.Fire) == WuXingRelation.Generate
    # 火生土
    assert relation(WuXing.Fire, WuXing.Earth) == WuXingRelation.Generate
    # 土生金
    assert relation(WuXing.Earth, WuXing.Metal) == WuXingRelation.Generate
    # 金生水
    assert relation(WuXing.Metal, WuXing.Water) == WuXingRelation.Generate
    # 水生木
    assert relation(WuXing.Water, WuXing.Wood) == WuXingRelation.Generate

    # 木同土
    assert relation(WuXing.Wood, WuXing.Wood) == WuXingRelation.Mutual
    # 火同火
    assert relation(WuXing.Fire, WuXing.Fire) == WuXingRelation.Mutual
    # 土同土
    assert relation(WuXing.Earth, WuXing.Earth) == WuXingRelation.Mutual
    # 金同金
    assert relation(WuXing.Metal, WuXing.Metal) == WuXingRelation.Mutual
    # 水同水
    assert relation(WuXing.Water, WuXing.Water) == WuXingRelation.Mutual

    # 木克土
    assert relation(WuXing.Wood, WuXing.Earth) == WuXingRelation.Overcome
    # 土克水
    assert relation(WuXing.Earth, WuXing.Water) == WuXingRelation.Overcome
    # 水克火
    assert relation(WuXing.Water, WuXing.Fire) == WuXingRelation.Overcome
    # 火克金
    assert relation(WuXing.Fire, WuXing.Metal) == WuXingRelation.Overcome
    # 金克木
    assert relation(WuXing.Metal, WuXing.Wood) == WuXingRelation.Overcome

    # 木化金
    assert relation(WuXing.Wood, WuXing.Metal) == WuXingRelation.Transform
    # 金化火
    assert relation(WuXing.Metal, WuXing.Fire) == WuXingRelation.Transform
    # 火化水
    assert relation(WuXing.Fire, WuXing.Water) == WuXingRelation.Transform
    # 水化土
    assert relation(WuXing.Water, WuXing.Earth) == WuXingRelation.Transform
    # 土化木
    assert relation(WuXing.Earth, WuXing.Wood) == WuXingRelation.Transform

    # 木泄水
    assert relation(WuXing.Wood, WuXing.Water) == WuXingRelation.Drain
    # 水泄金
    assert relation(WuXing.Water, WuXing.Metal) == WuXingRelation.Drain
    # 金泄土
    assert relation(WuXing.Metal, WuXing.Earth) == WuXingRelation.Drain
    # 土泄火
    assert relation(WuXing.Earth, WuXing.Fire) == WuXingRelation.Drain
    # 火泄木
    assert relation(WuXing.Fire, WuXing.Wood) == WuXingRelation.Drain


