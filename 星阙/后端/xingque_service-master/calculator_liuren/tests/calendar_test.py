from datetime import datetime

from constant.concept import DiZhi, TianGan, SolarTerm
from units.calendar import is_light, get_solar_term, get_chinese_year, calculate_years_old, \
    calculate_chun_fen, get_chinese_day, get_month, get_chinese_hour, get_chinese_datetime, get_liuren_datetime


def test_is_light():
    assert not is_light(DiZhi.Zi)
    assert not is_light(DiZhi.Chou)
    assert not is_light(DiZhi.Yin)
    assert is_light(DiZhi.Mao)
    assert is_light(DiZhi.Chen)
    assert is_light(DiZhi.Si)
    assert is_light(DiZhi.Wu)
    assert is_light(DiZhi.Wei)
    assert is_light(DiZhi.Shen)
    assert not is_light(DiZhi.You)
    assert not is_light(DiZhi.Xu)
    assert not is_light(DiZhi.Hai)

    # assert not is_light(get_chinese_hour())


def test_get_current_solar_term():
    assert get_solar_term() == SolarTerm.BaiLu


def test_get_chinese_year():
    assert get_chinese_year() == (TianGan.Jia, DiZhi.Chen)
    assert get_chinese_year(datetime(2023, 9, 1)) == (TianGan.Gui, DiZhi.Mao)


def test_get_chinese_hour():
    assert get_chinese_hour(datetime(2024, 1, 20, 0, 7))[1] == DiZhi.Zi
    assert get_chinese_hour(datetime(2024, 1, 20, 1, 7))[1] == DiZhi.Chou
    assert get_chinese_hour(datetime(2024, 1, 20, 3, 7))[1] == DiZhi.Yin
    assert get_chinese_hour(datetime(2024, 1, 20, 5, 7))[1] == DiZhi.Mao
    assert get_chinese_hour(datetime(2024, 1, 20, 7, 7))[1] == DiZhi.Chen
    assert get_chinese_hour(datetime(2024, 1, 20, 9, 7))[1] == DiZhi.Si
    assert get_chinese_hour(datetime(2024, 1, 20, 11, 7))[1] == DiZhi.Wu
    assert get_chinese_hour(datetime(2024, 1, 20, 13, 7))[1] == DiZhi.Wei
    assert get_chinese_hour(datetime(2024, 1, 20, 15, 7))[1] == DiZhi.Shen
    assert get_chinese_hour(datetime(2024, 1, 20, 17, 7))[1] == DiZhi.You
    assert get_chinese_hour(datetime(2024, 1, 20, 19, 7))[1] == DiZhi.Xu
    assert get_chinese_hour(datetime(2024, 1, 20, 21, 7))[1] == DiZhi.Hai
    assert get_chinese_hour(datetime(2025, 1, 20, 23, 7))[1] == DiZhi.Zi


def test_get_datatime_by_solar_term():
    assert get_solar_term(calculate_chun_fen(2024)) == SolarTerm.LiChun
    assert get_solar_term(calculate_chun_fen(2023)) == SolarTerm.LiChun
    assert get_solar_term(calculate_chun_fen(2022)) == SolarTerm.LiChun


def test_calculate_years_old():
    assert calculate_years_old(datetime(2024, 10, 1), True) == (TianGan.Bing, DiZhi.Yin)
    assert calculate_years_old(datetime(2024, 1, 1), True) == (TianGan.Ding, DiZhi.Mao)
    assert calculate_years_old(datetime(2023, 10, 1), True) == (TianGan.Ding, DiZhi.Mao)
    assert calculate_years_old(datetime(2022, 10, 1), True) == (TianGan.Wu, DiZhi.Chen)
    assert calculate_years_old(datetime(2021, 10, 1), True) == (TianGan.Ji, DiZhi.Si)
    assert calculate_years_old(datetime(2020, 10, 1), True) == (TianGan.Geng, DiZhi.Wu)

    assert calculate_years_old(datetime(2024, 10, 1), False) == (TianGan.Ren, DiZhi.Shen)
    assert calculate_years_old(datetime(2023, 10, 1), False) == (TianGan.Xin, DiZhi.Wei)
    assert calculate_years_old(datetime(2022, 10, 1), False) == (TianGan.Geng, DiZhi.Wu)
    assert calculate_years_old(datetime(2021, 10, 1), False) == (TianGan.Ji, DiZhi.Si)
    assert calculate_years_old(datetime(2020, 10, 1), False) == (TianGan.Wu, DiZhi.Chen)


def test_get_chinese_day():
    assert get_chinese_day(datetime(1900, 1, 2)) == (TianGan.Yi, DiZhi.Hai)


def test_get_month():
    assert get_month(datetime(2024, 1, 20, 22, 7)) == DiZhi.Chou
    assert get_month(datetime(2024, 1, 20, 22, 10)) == DiZhi.Zi


def test_get_chinese_datetime():
    dt = get_chinese_datetime(datetime(2024, 1, 20, 22, 7))
    assert len(dt) == 4


def test_get_liuren_datetime():
    month, day, hour = get_liuren_datetime(datetime(2024, 9, 22, 23, 24))
    print(month, day, hour)