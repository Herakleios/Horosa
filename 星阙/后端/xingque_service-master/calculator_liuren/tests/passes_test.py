from constant.concept import DiZhi, TianGan, WuXingRelation
from units.lessons import Lessons
from units.passes import Plane, Passes


def test_generate_four_lessons():
    result = '寅 辰 戌 子 辰 午 子 甲'
    four_lessons = Lessons.mock(result)
    assert result == four_lessons.__str__()


def test_count_deep():
    plane = Plane.generate(DiZhi.Xu, DiZhi.Zi)
    count = plane.count_deep(DiZhi.Chou, WuXingRelation.Overcome)
    assert count == 2
    count = plane.count_deep(DiZhi.Hai, WuXingRelation.Overcome)
    assert count == 6


def calculate_four_lessons(plane: Plane, day_tg: TianGan, day_dz: DiZhi) -> Lessons:
    """
    计算四课
    入参：
        plane: 式盘
        day_tg: 日干
        day_dz: 日支
    返回：
        四课
    """
    return Lessons.derive(plane, day_tg, day_dz)


def calculate_three_passes(plane: Plane, four_lessons: Lessons) -> list[DiZhi]:
    """
    计算三传
    入参：
        plane: 式盘
        four_lessons: 四课
    返回：
        三传
    """
    return Passes.derive(plane, four_lessons).three


# 测试三传，贼涉课
def test_calc_three_passes_zei_she():
    plane = Plane.generate(DiZhi.Mao, DiZhi.Zi)
    four = calculate_four_lessons(plane, TianGan.Bing, DiZhi.Wu)

    assert calculate_three_passes(plane, four) == [DiZhi.Shen, DiZhi.Hai, DiZhi.Yin]


# 测试三传，比用课
def test_calc_three_passes_bi_yong():
    plane = Plane.generate(DiZhi.Mao, DiZhi.Zi)

    four = Lessons.mock('子 未 未 寅 子 未 未 甲')
    three_passes = calculate_three_passes(plane, four)
    assert three_passes[0] == DiZhi.Zi

    four = Lessons.mock('未亥亥卯寅午午辛')
    three_passes = calculate_three_passes(plane, four)
    assert three_passes[0] == DiZhi.Wei


# 测试三传，涉害课
def test_calc_three_passes_she_hai():
    plane = Plane.generate(DiZhi.Hai, DiZhi.Chou)
    four_lessons = calculate_four_lessons(plane, TianGan.Ding, DiZhi.Mao)
    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Hai, DiZhi.You, DiZhi.Wei]


# 测试三传，遥克课
def test_calc_three_passes_yao_ke():
    plane = Plane.generate(DiZhi.You, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Ding, DiZhi.Mao)

    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Zi, DiZhi.You, DiZhi.Wu]


# 测试三传，昴星课
def test_calc_three_passes_any_star():
    plane = Plane.generate(DiZhi.Chen, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Wu, DiZhi.Yin)

    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Chou, DiZhi.Wu, DiZhi.You]


# 测试三传，伏吟课
def test_calc_three_passes_fu_yin():
    plane = Plane.generate(DiZhi.Zi, DiZhi.Zi)

    # # 阳日
    # four_lessons = calculate_four_lessons(plane, TianGan.Wu, DiZhi.Chen)
    # three = calculate_three_passes(plane, four_lessons)
    # assert three == [DiZhi.Si, DiZhi.Shen, DiZhi.Yin]
    #
    # # 阴日
    # four_lessons = calculate_four_lessons(plane, TianGan.Ding, DiZhi.Si)
    # three = calculate_three_passes(plane, four_lessons)
    # assert three == [DiZhi.Si, DiZhi.Shen, DiZhi.Yin]


# 测试三传，反吟课
def test_calc_three_passes_fan_yin():
    # 阳日
    plane = Plane.generate(DiZhi.Wu, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Geng, DiZhi.Xu)
    three = Passes.derive(plane, four_lessons)
    assert three.three == [DiZhi.Yin, DiZhi.Shen, DiZhi.Yin]

    # 阴日
    plane = Plane.generate(DiZhi.Wu, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Geng, DiZhi.Xu)
    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Yin, DiZhi.Shen, DiZhi.Yin]


# 测试三传，别责课
def test_calc_three_passes_bie_ze():
    # 阳日
    plane = Plane.generate(DiZhi.Chou, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Bing, DiZhi.Chen)
    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Hai, DiZhi.Wu, DiZhi.Wu]

    # 阴日
    plane = Plane.generate(DiZhi.Hai, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Xin, DiZhi.You)
    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Chou, DiZhi.You, DiZhi.You]


# 测试三传，八专课
def test_calc_three_passes_ba_zhuan():
    # 阳日
    plane = Plane.generate(DiZhi.You, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Jia, DiZhi.Yin)
    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Chou, DiZhi.Hai, DiZhi.Hai]

    # 阴日
    plane = Plane.generate(DiZhi.Mao, DiZhi.Zi)
    four_lessons = calculate_four_lessons(plane, TianGan.Ding, DiZhi.Wei)
    three = calculate_three_passes(plane, four_lessons)
    assert three == [DiZhi.Hai, DiZhi.Xu, DiZhi.Xu]
