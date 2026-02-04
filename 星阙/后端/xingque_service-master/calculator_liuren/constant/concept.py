from enum import Enum

from calculator_liuren.tools.enums import get_enum_by_index


class TianGan(Enum):
    Jia = '甲'
    Yi = '乙'
    Bing = '丙'
    Ding = '丁'
    Wu = '戊'
    Ji = '己'
    Geng = '庚'
    Xin = '辛'
    Ren = '壬'
    Gui = '癸'

    def __str__(self):
        return self.value


class DiZhi(Enum):
    Zi = '子'
    Chou = '丑'
    Yin = '寅'
    Mao = '卯'
    Chen = '辰'
    Si = '巳'
    Wu = '午'
    Wei = '未'
    Shen = '申'
    You = '酉'
    Xu = '戌'
    Hai = '亥'

    def __str__(self):
        return self.value


dizhi_order = [get_enum_by_index(DiZhi, i) for i in range(12)]
dizhi_map = {i.value: i for i in DiZhi}
tiangan_order = [get_enum_by_index(TianGan, i) for i in range(10)]
tiangan_map = {i.value: i for i in TianGan}


class SolarTerm(Enum):
    LiChun = ('立春', 315, DiZhi.Zi)
    YuShui = ('雨水', 330, DiZhi.Hai)
    JingZhe = ('惊蛰', 345, DiZhi.Hai)
    ChunFen = ('春分', 0, DiZhi.Xu)
    QingMing = ('清明', 15, DiZhi.Xu)
    GuYu = ('谷雨', 30, DiZhi.You)
    LiXia = ('立夏', 45, DiZhi.You)
    XiaoMan = ('小满', 60, DiZhi.Shen)
    MangZhong = ('芒种', 75, DiZhi.Shen)
    XiaZhi = ('夏至', 90, DiZhi.Wei)
    XiaoShu = ('小暑', 105, DiZhi.Wei)
    DaShu = ('大暑', 120, DiZhi.Wu)
    LiQiu = ('立秋', 135, DiZhi.Wu)
    ChuShu = ('处暑', 150, DiZhi.Si)
    BaiLu = ('白露', 165, DiZhi.Si)
    QiuFen = ('秋分', 180, DiZhi.Chen)
    HanLu = ('寒露', 195, DiZhi.Chen)
    ShuangJiang = ('霜降', 210, DiZhi.Mao)
    LiDong = ('立冬', 225, DiZhi.Mao)
    XiaoXue = ('小雪', 240, DiZhi.Yin)
    DaXue = ('大雪', 255, DiZhi.Yin)
    DongZhi = ('冬至', 270, DiZhi.Chou)
    XiaoHan = ('小寒', 285, DiZhi.Chou)
    DaHan = ('大寒', 300, DiZhi.Zi)

    def __str__(self):
        return self.value


# 定义节气名称
solar_terms_map = {i.value[0]: i for i in SolarTerm}


# 天将
class TianJiang(Enum):
    # value[0] 为全称，value[1] 为简称
    GuiRen = ['贵人', '贵']
    TengShe = ['螣蛇', '蛇']
    ZhuQue = ['朱雀', '雀']
    LiuHe = ['六合', '合']
    GouChen = ['勾陈', '勾']
    QingLong = ['青龙', '龙']
    TianKong = ['天空', '空']
    BaiHu = ['白虎', '虎']
    TaiChang = ['太常', '常']
    XuanWu = ['玄武', '玄']
    TaiYin = ['太阴', '阴']
    TianHou = ['天后', '后']

    def __str__(self):
        return self.value[0]


class Element:
    def __init__(self, name: str, tiangan: list[TianGan], dizhi: list[DiZhi]):
        self.name = name
        self.dizhi = dizhi
        self.tiangan = tiangan


class Flow(Enum):
    ChangSheng = '长生'
    MuYu = '沐浴'
    GuanDai = '冠带'
    LinGuan = '临官'
    DiWang = '帝旺'
    Shuai = '衰'
    Bing = '病'
    Si = '死'
    Mu = '墓'
    Jue = '绝'
    Tai = '胎'
    Yang = '养'


class WuXing(Enum):
    Wood = Element('木', [TianGan.Jia, TianGan.Yi], [DiZhi.Yin, DiZhi.Mao])
    Fire = Element('火', [TianGan.Bing, TianGan.Ding], [DiZhi.Si, DiZhi.Wu])
    Earth = Element('土', [TianGan.Wu, TianGan.Ji], [DiZhi.Chen, DiZhi.Wei, DiZhi.Xu, DiZhi.Chou])
    Metal = Element('金', [TianGan.Geng, TianGan.Xin], [DiZhi.Shen, DiZhi.You])
    Water = Element('水', [TianGan.Ren, TianGan.Gui], [DiZhi.Hai, DiZhi.Zi])

    def __str__(self):
        return self.value.name


class Season(Enum):
    Spring = ('春', WuXing.Wood)
    Summer = ('夏', WuXing.Fire)
    Autumn = ('秋', WuXing.Metal)
    Winter = ('冬', WuXing.Water)


# 定义五行元素的顺序
wuxing_map = {
    '木': WuXing.Wood,
    '火': WuXing.Fire,
    '土': WuXing.Earth,
    '金': WuXing.Metal,
    '水': WuXing.Water,
}
wuxing_order = [WuXing.Wood, WuXing.Fire, WuXing.Earth, WuXing.Metal, WuXing.Water]
dizhi_wuxing_relation = {dizhi: wuxing for wuxing in wuxing_order for dizhi in wuxing.value.dizhi}
tiangan_wuxing_relation = {dizhi: wuxing for wuxing in wuxing_order for dizhi in wuxing.value.tiangan}


# 定义五行元素之间的关系
class WuXingRelation(Enum):
    Mutual = ('同', '王', '兄')
    Generate = ('生', '相', '父')
    Overcome = ('克', '休', '官')
    Transform = ('化', '死', '财')
    Drain = ('泄', '囚', '孙')


# 定义五行元素之间的关系
wuxing_relations = [WuXingRelation.Mutual,
                    WuXingRelation.Generate,
                    WuXingRelation.Overcome,
                    WuXingRelation.Transform,
                    WuXingRelation.Drain]

# 天干地支寄居关系
lodge_relation = {
    TianGan.Jia: DiZhi.Yin,
    TianGan.Yi: DiZhi.Chen,
    TianGan.Bing: DiZhi.Si,
    TianGan.Ding: DiZhi.Wei,
    TianGan.Wu: DiZhi.Si,
    TianGan.Ji: DiZhi.Wei,
    TianGan.Geng: DiZhi.Shen,
    TianGan.Xin: DiZhi.Xu,
    TianGan.Ren: DiZhi.Hai,
    TianGan.Gui: DiZhi.Chou,
}

# 地支天干归藏关系
invert_lodge_relation = {}
for k, v in lodge_relation.items():
    if v not in invert_lodge_relation:
        invert_lodge_relation[v] = [k]
    else:
        invert_lodge_relation[v].append(k)

# 地支孟仲季
meng_zhong_ji_list = [DiZhi.Yin, DiZhi.Shen, DiZhi.Si, DiZhi.Hai,
                      DiZhi.Zi, DiZhi.Wu, DiZhi.Mao, DiZhi.You,
                      DiZhi.Chen, DiZhi.Wu, DiZhi.Chou, DiZhi.Wei]

# 所刑关系
restrained_relation = {
    DiZhi.Zi: DiZhi.Mao,
    DiZhi.Mao: DiZhi.Zi,
    DiZhi.Yin: DiZhi.Si,
    DiZhi.Si: DiZhi.Shen,
    DiZhi.Shen: DiZhi.Yin,
    DiZhi.Wei: DiZhi.Chou,
    DiZhi.Chou: DiZhi.Xu,
    DiZhi.Xu: DiZhi.Wei,
    DiZhi.Chen: DiZhi.Chen,
    DiZhi.Wu: DiZhi.Wu,
    DiZhi.You: DiZhi.You,
    DiZhi.Hai: DiZhi.Hai,
}

# 太乙贵人判断昼夜时与日干的关系
day_or_night_order = {
    TianGan.Jia: [DiZhi.Chou, DiZhi.Wei],
    TianGan.Yi: [DiZhi.Zi, DiZhi.Shen],
    TianGan.Bing: [DiZhi.Hai, DiZhi.You],
    TianGan.Ding: [DiZhi.Hai, DiZhi.You],
    TianGan.Wu: [DiZhi.Chou, DiZhi.Wei],
    TianGan.Ji: [DiZhi.Zi, DiZhi.Shen],
    TianGan.Geng: [DiZhi.Chou, DiZhi.Wei],
    TianGan.Xin: [DiZhi.Wu, DiZhi.Yin],
    TianGan.Ren: [DiZhi.Si, DiZhi.Mao],
    TianGan.Gui: [DiZhi.Si, DiZhi.Mao],
}

# 天将顺序
seq_order = [
    [DiZhi.Hai, DiZhi.Zi, DiZhi.Chou, DiZhi.Yin, DiZhi.Mao, DiZhi.Chen],
    [DiZhi.Si, DiZhi.Wu, DiZhi.Wei, DiZhi.Shen, DiZhi.You, DiZhi.Xu],
]
