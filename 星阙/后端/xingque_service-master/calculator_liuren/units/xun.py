# 旬日

from calculator_liuren.constant.concept import TianGan, DiZhi, tiangan_order
from calculator_liuren.tools.enums import get_enum_index
from calculator_liuren.units.common import rotate_gz_order


class Xun:

    def __init__(self, retreated: dict[DiZhi, TianGan], empty: list[DiZhi], start: DiZhi, end: DiZhi, ding: DiZhi):
        self.retreated = retreated
        self.empty = empty
        self.start = start
        self.end = end
        self.ding = ding

    @classmethod
    def calculate(cls, tg: TianGan, dz: DiZhi):
        """
        遁干

        入参：
            tg: 天干
            dz: 地支

        返回：
            旬日
        """

        # 计算偏移量
        tg_index = get_enum_index(tg)
        dz_index = get_enum_index(dz)
        offset = (dz_index - tg_index) % 12
        start = abs(offset - 12 if offset > 0 else offset)

        # 旋转地支顺序
        rotated = rotate_gz_order(DiZhi, start)

        # 生成遁干表
        retreated = {}
        for i in range(12):
            if i < 10:
                retreated[rotated[i]] = tiangan_order[i]
            else:
                retreated[rotated[i]] = None

        empty, start, end, ding = [], None, None, None

        for k, v in retreated.items():
            if v is None:
                empty.append(k)
            elif v == TianGan.Jia:
                start = k
            elif v == TianGan.Gui:
                end = k
            elif v == TianGan.Ding:
                ding = k

        return cls(retreated, empty, start, end, ding)
