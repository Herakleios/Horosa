from constant.concept import TianGan, DiZhi
from units.xun import Xun


# 测试旬日生成算法
def test_retreated_tiangan():
    assert Xun.calculate(TianGan.Jia, DiZhi.Zi).retreated[DiZhi.Wu] is TianGan.Geng
    assert Xun.calculate(TianGan.Ren, DiZhi.Wu).retreated[DiZhi.Chou] is TianGan.Ding
    assert Xun.calculate(TianGan.Bing, DiZhi.Xu).retreated[DiZhi.Wu] is None
    assert Xun.calculate(TianGan.Geng, DiZhi.Zi).retreated[DiZhi.Chen] is None
    assert Xun.calculate(TianGan.Jia, DiZhi.Chen).retreated[DiZhi.Zi] is TianGan.Ren
    assert Xun.calculate(TianGan.Wu, DiZhi.Wu).retreated[DiZhi.Yin] is TianGan.Jia


# 测试旬日生成结果
def test_assemble_result():
    result = Xun.calculate(TianGan.Xin, DiZhi.Chou)
    assert result.retreated[DiZhi.Wu] is TianGan.Jia
    assert DiZhi.Chen in result.empty and DiZhi.Si in result.empty
    assert result.start is DiZhi.Wu
