# 三传
from typing import List, Set

from calculator_liuren.units.common import is_self_restrained, find_restrained, find_clashed, is_restrained, find_tg_union, find_dz_union, \
    find_gz_by_offset
from calculator_liuren.units.ganzhi import get_wuxing_by, get_lodging_dizhi_from_tiangan
from calculator_liuren.units.lessons import Lessons
from calculator_liuren.units.shensha import find_horse
from calculator_liuren.units.plane import Plane

from calculator_liuren.constant.concept import DiZhi, WuXingRelation, meng_zhong_ji_list, TianGan, TianJiang, restrained_relation
from calculator_liuren.units.wuxing import relation
from calculator_liuren.units.yinyang import is_same_yin_yang, is_yang


class Passes:
    def __init__(self, first: DiZhi, middle: DiZhi, final: DiZhi, xun: list[TianGan | None],
                 tian_jiang: list[TianJiang],
                 wuxing: list[WuXingRelation], major_category: str, sub_category: str):
        self.three = [first, middle, final]
        self.xun = xun
        self.tian_jiang = tian_jiang
        self.wuxing = wuxing
        self.major_category = major_category
        self.sub_category = sub_category

    @classmethod
    def derive(cls, plane: Plane, four: Lessons):
        """
        计算三传

        入参：
            plane: 式盘
            four: 四课

        返回
            初传
        """

        def calculate_three_passes() -> tuple[list[DiZhi], str, str]:
            """
            计算三传

            入参：
                four: 四课的地支列表
                day_tg: 日干

            返回
                初传
            """

            _major = ''
            _sub = ''

            def set_major(v: str):
                nonlocal _major
                _major = v

            def set_sub(v: str):
                nonlocal _sub
                _sub = v

            day_tg = four.get_day_tg()
            day_dz = four.get_day_dz()

            def derive_middle_and_final(_first: DiZhi) -> list[DiZhi]:
                """
                中末递取
                入参：
                    first: 初传
                返回:
                    初传，中传，末传
                """
                _middle = plane.transmission(_first)
                _final = plane.transmission(_middle)
                return [_first, _middle, _final]

            # 贼列表, 摄列表, 遥克神克日干列表, 遥克日干克神列表
            zei_list, she_list, yao_ke, invert_yao_ke = four.zei, four.she, four.yao, four.yao_inv

            # 伏吟之法
            if plane.is_fu_yin() and four.no_immediate_clash():
                set_major('伏吟')
                if is_yang(day_tg):
                    # 伏吟有近克 或 阳日伏吟无近克
                    # 初传为一课上神
                    first = four.get_up(1)
                    # 被初传所刑的地支为中传，如果初传自刑，就取三课上神
                    self_restrained = is_self_restrained(first)
                    middle = four.get_up(3) if self_restrained else find_restrained(first)
                    set_sub('杜传' if self_restrained else '自任')

                    # 被中传所刑的地支为末传，如果中传自刑，就取被中传所冲的地支
                    clashed = (is_self_restrained(middle) or is_restrained(first, middle))
                    final = find_clashed(middle) if clashed else find_restrained(middle)
                    set_sub('不虞' if clashed else _sub)
                    return [first, middle, final], _major, _sub
                else:
                    # 阴日伏吟无近克
                    # 初传为一课上神
                    first = four.get_up(3)
                    # 被初传所刑的地支为中传，如果初传自刑，就取三课上神
                    self_restrained = is_self_restrained(first)
                    middle = four.get_up(1) if self_restrained else find_restrained(first)
                    set_sub('杜传' if self_restrained else '自信')
                    # 被中传所刑的地支为末传，如果中传自刑，就取被中传所冲的地支
                    clashed = (is_self_restrained(middle) or is_restrained(first, middle))
                    final = find_clashed(middle) if clashed else find_restrained(middle)
                    set_sub('不虞' if clashed else _sub)
                    return [first, middle, final], _major, _sub

            # 反吟无近克
            if plane.is_fan_yin():
                set_major('反吟')
                if four.no_immediate_clash():
                    set_sub('无依')
                    # 初传为日支的驿马
                    first = find_horse(day_dz)
                    # 三课上神为中传
                    middle = four.get_up(3)
                    # 一课上神为末传
                    final = four.get_up(1)
                    return [first, middle, final], _major, _sub
                else:
                    set_sub('无亲')
                    r, f = get_only(zei_list, WuXingRelation.Overcome)
                    return derive_middle_and_final(r), _major, _sub

            # 八专之法, 无近克，有遥克
            if four.half_complete() and four.no_immediate_clash():
                set_major('八专')
                set_sub('八专')
                if is_yang(day_tg):
                    # 阳日
                    # 一课上神，顺数三位为初传
                    first = find_gz_by_offset(four.get_up(1), 2)
                else:
                    # 阴日
                    # 四课上神，逆数三位为初传
                    first = find_gz_by_offset(four.get_up(4), -2)

                # 一课上神为中传, 一课上神为末传
                middle = final = four.get_up(1)
                return [first, middle, final], _major, _sub

            # 别责：无近克，无遥克，四课不全
            if four.not_complete() and four.no_immediate_clash() and four.no_remote_clash():
                set_major('别责')
                if is_yang(day_tg):
                    # 阳日
                    # 日干所合天干的上神为初传
                    set_sub('不备')
                    first = plane.transmission(get_lodging_dizhi_from_tiangan(find_tg_union(day_tg)))
                else:
                    # 阴日
                    # 在日支之前(顺时针方向)的日支所合之神，为初传
                    set_sub('芜淫')
                    first = find_dz_union(day_dz)

                # 一课上神为中传, 一课上神为末传
                middle = final = four.get_up(1)
                return [first, middle, final], _major, _sub

            # 贼摄之法
            first = zei_she(zei_list, she_list)
            if first is not None:
                set_major('贼克')
                set_sub('重审' if len(zei_list) == 1 else '元首')
                return derive_middle_and_final(first), _major, _sub

            sub_list = ['知一', '涉害', '见机', '察微', '缀瑕']
            if len(zei_list) > 1:
                # 比用之法
                # 多课贼，贼课中有且仅只有唯一上课与日干阴阳相同
                first, flag = get_only(zei_list, WuXingRelation.Overcome)
                if flag == 0:
                    set_major('比用')
                else:
                    set_major('涉害')
                set_sub(sub_list[flag])
            elif len(zei_list) == 0 and len(she_list) > 1:
                # 涉害之法
                # 无贼，多课摄，摄课中有且仅只有唯一上课与日干阴阳相同
                first, flag = get_only(she_list, WuXingRelation.Transform)
                if flag == 0:
                    set_major('比用')
                else:
                    set_major('涉害')
                set_sub(sub_list[flag])
            elif four.no_immediate_clash():
                # 遥克之法
                # 无近克，考虑“遥克”——日干(一课下神)与二三四课的上神是否相克
                set_major('遥克')
                if len(yao_ke) == 1:
                    # 如果只有一个上神克日干，那此上神便是初传
                    set_sub('蒿失')
                    first = yao_ke[0]
                elif len(yao_ke) == 0 and len(invert_yao_ke) == 1:
                    # 如果日干只克一个上神，那此上神便是初传
                    set_sub('弹射')
                    first = invert_yao_ke[0]
                elif len(yao_ke) > 1:
                    set_sub('蒿失')
                    # 如果多个上神克日干，那么仿照“比用”，与日干阴阳相同者是初传
                    # 如果多个上神克日干，且与日干阴阳相同、或全不同，那么仿照“涉害”，选择涉害深者为初传
                    first = get_only(yao_ke, WuXingRelation.Overcome)[0]
                elif len(yao_ke) == 0 and len(invert_yao_ke) > 1:
                    set_sub('弹射')
                    # 如果日干克了多个上神，那么仿照“比用”，与日干阴阳相同者是初传;
                    # 如果日干克了多个上神，且与日干阴阳相同、或全不同，那么仿照“涉害”，选择涉害深者为初传
                    first = get_only(invert_yao_ke, WuXingRelation.Transform)[0]

            if first is not None:
                return derive_middle_and_final(first), _major, _sub

            # 昴星之法
            if len(zei_list) + len(she_list) + len(yao_ke) + len(invert_yao_ke) == 0:
                r, i = ang_star(four)
                set_major('昴星')
                set_sub(['虎视', '冬蛇'][i])
                return r, _major, _sub

        def ang_star(four_lessons: Lessons) -> tuple[list[DiZhi], int]:
            """
            昴星之法 : 无近克，无遥克
            入参：
                plane: 式盘
                four_lessons: 四课
            返回:
                初传，中传，末传
            """
            day_tg = four_lessons.get_day_tg()

            if is_yang(day_tg):
                # 日干为阳干
                # 地盘酉的上神为初传
                first = plane.transmission(DiZhi.You)
                # 三课上神(日支上神)为中传
                middle = four_lessons.get_up(3)
                # 一课上神的(日干上神)为末传
                final = four_lessons.get_up(1)
                return [first, middle, final], 0
            else:
                # 日干为阴干
                # 天盘酉的下神为初传
                first = plane.invert_transmission(DiZhi.You)
                # 一课上神(日干上神)为中传
                middle = four_lessons.get_up(1)
                # 三课上神的(日支上神)为末传
                final = four_lessons.get_up(3)
                return [first, middle, final], 1

        def zei_she(zei_list: list[DiZhi], she_list: list[DiZhi]) -> DiZhi | None:
            """
            贼摄之法
            入参：
                zei_list: 贼列表
                she_list: 摄列表
            返回:
                有且仅有一个结果时，返回结果，否则返回None
            """
            if len(zei_list) == 1:
                # 四课中，有且仅有一个"下克上"
                return zei_list[0]
            elif len(zei_list) == 0 and len(she_list) == 1:
                # 四课中，有且仅有一个"上克下"，并无“下克上”
                return she_list[0]
            else:
                return None

        def get_only(overcome_list: list[DiZhi],
                     target: WuXingRelation) -> tuple[DiZhi | None, int]:
            """
            使用比用之法或涉害之法，获取唯一上神
            入参：
                overcome_list: 克列表
                target: 目标五行关系
                day_tg: 日干
                plane: 式盘
                four_lessons: 四课
            返回:
                有且仅有一个结果时，返回结果，否则返回None
                0 - 知一
                1 - 涉害
                2 - 见机
                3 - 察微
                4 - 缀瑕
            """

            day_tg = four.get_day_tg()

            def meng_zhong(up_list: list[DiZhi]) -> tuple[DiZhi | None, int]:
                """
                孟仲之法
                入参：
                    up_list: 上神列表
                    plane: 式盘
                    four: 四课
                    day_tg: 日干
                返回:
                    有且仅有一个结果时，返回结果，否则返回None
                    0 - 孟
                    1 - 仲
                    2 - 无法使用孟仲之法
                """
                # 对应的下神列表
                down_up_map = {plane.invert_transmission(up): up for up in up_list}

                meng_list = []
                zhong_list = []

                for down, up in down_up_map.items():
                    if meng_zhong_ji_list.index(down) // 4 == 0:
                        meng_list.append(up)
                    elif meng_zhong_ji_list.index(down) // 4 == 1:
                        zhong_list.append(up)

                if len(meng_list) == 1:
                    return meng_list[0], 0
                elif len(zhong_list) == 1:
                    return zhong_list[0], 1
                else:
                    if is_yang(day_tg):
                        # 日干为阳干
                        return four.get_up(1), 2
                    else:
                        # 日干为阴干
                        return four.get_up(3), 2

            def get_the_deepest(compare_list: List | Set) -> tuple[DiZhi, int]:
                """
                获取最深的上神
                入参：
                    compare_list: 比较列表
                返回：
                    最深的上神，是否使用孟仲之法
                    0 - 不使用孟仲之法
                    1 - 使用孟
                    2 - 使用仲
                    3 - 无法使用孟仲
                """
                record = {}
                # 比较涉害深度
                for _item in compare_list:
                    _deep = plane.count_deep(_item, target)
                    if _deep in record:
                        record[_deep].append(_item)
                    else:
                        record[_deep] = [_item]

                # 倒序排序
                _sorted = sorted(record.items(), reverse=True)
                _max = _sorted[0][1]

                if len(_max) == 1:
                    return _max[0], 0
                else:
                    # 使用孟仲之法
                    mz, _f = meng_zhong(_max)
                    return mz, _f + 1

            same_set = set()
            for item in overcome_list:
                if is_same_yin_yang(item, day_tg):
                    same_set.add(item)

            if len(same_set) == 1:
                # 只有一上神与日干阴阳相同使用比用之法
                return next(iter(same_set)), 0
            elif len(same_set) > 0:
                # 有多个上神与日干阴阳相同是使用涉害之法
                r, f = get_the_deepest(same_set)
                return r, f + 1
            elif len(same_set) == 0:
                # 无上神与日干阴阳相同时使用涉害之法
                r, f = get_the_deepest(overcome_list)
                return r, f + 1
            else:
                return None, -1

        result, major, sub = calculate_three_passes()
        xun = [plane.get_xun(r) for r in result]
        tian_jiang = [plane.get_tian_jiang(r) for r in result]

        wuxing = [relation(get_wuxing_by(r), get_wuxing_by(four.get_day_tg())) for r in result]
        return cls(result[0], result[1], result[2], xun, tian_jiang, wuxing, major, sub)
