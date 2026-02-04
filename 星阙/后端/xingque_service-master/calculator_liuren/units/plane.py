# 式盘

from calculator_liuren.constant.concept import dizhi_order, DiZhi, WuXingRelation, invert_lodge_relation, TianJiang, TianGan, \
    seq_order
from calculator_liuren.tools.enums import get_enum_index, get_enum_by_index
from calculator_liuren.units.common import find_clashed
from calculator_liuren.units.ganzhi import get_wuxing_by
from calculator_liuren.units.wuxing import relation
from calculator_liuren.units.xun import Xun


# 式盘
class Plane:
    """
    天盘与地盘的配对。
    """

    def __init__(self, month: DiZhi, hour: DiZhi, ecliptic_plane: list[DiZhi]):
        self.month = month
        self.hour = hour
        self.equatorial_plane = dizhi_order
        self.ecliptic_plane = ecliptic_plane
        self.tian_jiang = None
        self.xun = []

    @classmethod
    def generate(cls, month: DiZhi, hour: DiZhi):
        """
        生成式盘。

        入参：
            month: 月将
            hour: 时将

        返回：
            生成的式盘
        """

        def alignment_hour() -> list[DiZhi]:
            """
            所谓配，即对应，天盘某神对应地盘某神，这两神便彼此配对。

            参数:
                month (DiZhi): 月将。
                hour (DiZhi): 时将

            返回:
                list[DiZhi, DiZhi]: 配好的天盘。
            """

            # 获取时将的索引
            hour_index = get_enum_index(hour)
            # 计算月将的索引
            month_index = get_enum_index(month) - hour_index
            # 配好的天盘
            return dizhi_order[month_index:] + dizhi_order[:month_index]

        return cls(month, hour, alignment_hour())

    def transmission(self, target: DiZhi) -> DiZhi:
        """
        某神在天盘中，而在地盘中找到此神，看它的上神为何，这个过程称为“递”，即传递

        参数:
            target (str): 目标上神。

        返回:
            str: 递后的上神。
        """
        # 返回递后的上神
        return self.ecliptic_plane[self.equatorial_plane.index(target)]

    def invert_transmission(self, up: DiZhi) -> DiZhi:
        """
        获取下神。

        参数:
            up (str): 上神。

        返回:
            str: 下神。
        """
        return self.equatorial_plane[self.ecliptic_plane.index(up)]

    def get_tian_jiang(self, up: DiZhi) -> TianJiang | None:
        """
        获取天将。

        参数:
            up (str): 上神。

        返回:
            str: 天将。
        """

        if self.tian_jiang is None:
            return None

        _index = self.ecliptic_plane.index(up)
        return self.tian_jiang[_index]

    def get_xun(self, up: DiZhi) -> TianGan | None:
        """
        获取旬日。

        参数:
            up (str): 上神。

        返回:
            str: 旬日。
        """

        if len(self.xun) == 0:
            return None

        _index = self.ecliptic_plane.index(up)
        return self.xun[_index]

    def count_deep(self, up: DiZhi, target: WuXingRelation) -> int:
        """
        计算克数。

        参数:
            target (str): 目标上神。

        返回:
            int: 克数。
        """

        count = 0
        # 获取目标神的索引
        begin = self.ecliptic_plane.index(up)
        _plane = self.equatorial_plane[begin:] + self.equatorial_plane[:begin]
        end = _plane.index(up)

        # 获取目标上神的五行
        target_wuxing = get_wuxing_by(up)

        for i in range(end + 1):
            # 计算被克次数
            # 被下神克
            _down = _plane[i]
            if relation(get_wuxing_by(_down), target_wuxing) == target:
                count += 1
            # 被下神中藏的天干克
            if _down in invert_lodge_relation:
                for shen in invert_lodge_relation[_down]:
                    if relation(get_wuxing_by(shen), target_wuxing) == target:
                        count += 1

        # 计算被克次数
        return count

    def inject_tian_jiang(self, target: DiZhi):
        """
        注入天将。

        参数:
            target (str): 太乙贵人所在的日干所在的十二神位置。
        """

        def alignment_gui(right: bool) -> list[TianJiang]:
            """
            对齐天将与十二神。

            参数:
                shen (list[DiZhi]): 十二神。
                right (bool): 是否顺布。

            返回:
                list[TianJiang]: 对应的天将顺序列表。
            """
            shen = self.ecliptic_plane

            # 配好的序列
            index_list = []
            if right:
                # 计算偏移量
                offset = shen.index(DiZhi.Zi) - shen.index(target)
                index_list = [(get_enum_index(s) + offset) % 12 for s in shen]
            else:
                # 计算偏移量
                index_list = [(get_enum_index(target) - get_enum_index(s)) % 12 for s in shen]

            return [get_enum_by_index(TianJiang, i) for i in index_list]

        # 贵人下神
        down = self.invert_transmission(target)
        # 判断天将顺序
        self.tian_jiang = alignment_gui((down in seq_order[0]))

    def inject_xun(self, xun: Xun):
        """
        注入旬日。

        参数:
            tg (str): 天干。
            dz (str): 地支。
        """
        for i in range(12):
            self.xun.append(xun.retreated[self.ecliptic_plane[i]])

    def is_fu_yin(self) -> bool:
        """
        判断是否伏吟。
        返回:
            bool: 是否伏吟。
        """
        return self.month == self.hour

    def is_fan_yin(self) -> bool:
        """
        判断是否反吟。
        返回:
            bool: 是否反吟。
        """
        return find_clashed(self.month) == self.hour
