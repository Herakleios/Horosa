# 四课
import copy

from calculator_liuren.constant.concept import TianGan, DiZhi, WuXingRelation
from calculator_liuren.units.ganzhi import get_lodging_dizhi_from_tiangan, get_wuxing_by
from calculator_liuren.units.plane import Plane
from calculator_liuren.units.wuxing import relation


class Lessons:
    """
    四课
    """

    def __init__(self, four: list[list[TianGan | DiZhi]]):
        def calculate() -> (list[DiZhi], list[DiZhi], list[DiZhi], list[DiZhi]):
            """
            计算四课中的贼、摄、遥、遥克
            入参：
                four: 四课
            返回：
                贼，摄，遥，遥克
            """
            zei, she, yao, yao_inv = [], [], [], []

            day_tg = four[0][1]

            # 解析四课中的贼与摄
            for i in four:
                up = i[0]
                down = i[1]
                _relation = relation(get_wuxing_by(down), get_wuxing_by(up))
                # 下克上
                if _relation == WuXingRelation.Overcome:
                    if up not in zei:
                        zei.append(up)
                # 上克下
                elif _relation == WuXingRelation.Transform:
                    if up not in she:
                        she.append(up)

            # 解析四课中的遥克
            for i in [four[1], four[2], four[3]]:
                target = i[0]
                if relation(get_wuxing_by(target), get_wuxing_by(day_tg)) == WuXingRelation.Overcome:
                    # 无“近克”，二三四课的上神有克日干者
                    yao.append(target)
                elif relation(get_wuxing_by(day_tg), get_wuxing_by(target)) == WuXingRelation.Overcome:
                    # 无“近克”，日干克了二三四课的某个或多个上神
                    yao_inv.append(target)

            return zei, she, yao, yao_inv

        def calculate_set() -> set:
            _four = copy.deepcopy(four)
            _four[0][1] = get_lodging_dizhi_from_tiangan(_four[0][1])
            lessons_set = set()
            for i in _four:
                lessons_set.add(f'{i[0].value}{i[1].value}')

            return lessons_set

        self.first = four[0]
        self.second = four[1]
        self.third = four[2]
        self.fourth = four[3]
        self.zei, self.she, self.yao, self.yao_inv = calculate()
        self.__set = calculate_set()

    @classmethod
    def derive(cls, plane: Plane, day_tg: TianGan, day_dz: DiZhi):
        def calculate_four_lessons() -> list[list[DiZhi | TianGan]]:
            """
            计算四课。

            入参：
                plane: 式盘
                day_tg: 日干
                day_dz: 日支

            返回：
                四课列表

            """

            # 一课
            first_up = plane.transmission(get_lodging_dizhi_from_tiangan(day_tg))
            first_lesson = [first_up, day_tg, plane.get_xun(first_up), plane.get_tian_jiang(first_up)]
            # 二课
            second_up = plane.transmission(first_up)
            second_lesson = [second_up, first_lesson[0], plane.get_xun(second_up), plane.get_tian_jiang(second_up)]
            # 三课
            third_up = plane.transmission(day_dz)
            third_lesson = [third_up, day_dz, plane.get_xun(third_up), plane.get_tian_jiang(third_up)]
            # 四课
            fourth_up = plane.transmission(third_up)
            fourth_lesson = [fourth_up, third_lesson[0], plane.get_xun(fourth_up), plane.get_tian_jiang(fourth_up)]

            return [first_lesson, second_lesson, third_lesson, fourth_lesson]

        return cls(calculate_four_lessons())

    @classmethod
    def mock(cls, target: str):
        target = target.replace(' ', '')

        _map = {}
        for i, dz in enumerate(DiZhi):
            _map[dz.value] = dz
        for i, tg in enumerate(TianGan):
            _map[tg.value] = tg

        l = [_map[target[i]] for i in [6, 7, 4, 5, 2, 3, 0, 1]]
        return cls([[l[0], l[1]], [l[2], l[3]], [l[4], l[5]], [l[6], l[7]]])

    def get_up(self, index: 1 | 2 | 3 | 4) -> DiZhi:
        """
        获取上神
        入参：
            index: 上神索引, 1-4
        返回：
            上神
        """
        return [self.first, self.second, self.third, self.fourth][index - 1][0]

    def get_day_tg(self) -> TianGan:
        """
        获取日干
        返回：
            日干
        """
        return self.first[1]

    def get_day_dz(self) -> DiZhi:
        """
        获取日支
        返回：
            日支
        """
        return self.third[1]

    def no_immediate_clash(self) -> bool:
        """
        判断是否无近克
        返回：
            是否无近克
        """
        return len(self.zei) + len(self.she) == 0

    def no_remote_clash(self) -> bool:
        """
        判断是否无遥克
        返回：
            是否无遥克
        """
        return len(self.yao) + len(self.yao_inv) == 0

    def not_complete(self):
        """
        判断是否四课不备
        返回：
            是否四课不备
        """

        return len(self.__set) != 4

    def half_complete(self):
        """
        判断是否有两课
        返回：
            是否只有两课
        """

        return len(self.__set) == 2

    def __str__(self):
        l = [[lesson[0], lesson[1]] for lesson in [self.fourth, self.third, self.second, self.first]]
        r = []
        for i in l:
            r.append(str(i[0].value))
            r.append(str(i[1].value))

        return ' '.join(r)
