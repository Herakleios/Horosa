import re
import math
import datetime
from itertools import cycle, repeat
from sxtwl import fromSolar
import ephem
import time

cnum = list("一二三四五六七八九十")
tian_gan = '甲乙丙丁戊己庚辛壬癸'
di_zhi = '子丑寅卯辰巳午未申酉戌亥'
cnumber = list("一二三四五六七八九")
door_r = list("休生傷杜景死驚開")
star_r = list("蓬任沖輔英禽柱心")
eight_gua = list("坎坤震巽中乾兌艮離")
clockwise_eightgua = list("坎艮震巽離坤兌乾")
wuxing = "火水金火木金水土土木,水火火金金木土水木土,火火金金木木土土水水,火木水金木水土火金土,木火金水水木火土土金"
wuxing_relation_2 = dict(
    zip(list(map(lambda x: tuple(re.findall("..", x)), wuxing.split(","))), "尅我,我尅,比和,生我,我生".split(",")))
cmonth = list("一二三四五六七八九十") + ["十一", "十二"]
jieqi_name = re.findall('..', '春分清明穀雨立夏小滿芒種夏至小暑大暑立秋處暑白露秋分寒露霜降立冬小雪大雪冬至小寒大寒立春雨水驚蟄')
jj = {"甲子": "戊", "甲戌": "己", "甲申": "庚", "甲午": "辛", "甲辰": "壬", "甲寅": "癸"}
door_wuxing = dict(zip(door_r, "水土木木火土金金"))
star_wuxing = dict(zip(star_r, "水土木木火土金金"))
guxu = {'甲子': {'孤': '戌亥', '虛': '辰巳'},
        '甲戌': {'孤': '申酉', '虛': '寅卯'},
        '甲申': {'孤': '午未', '虛': '子丑'},
        '甲午': {'孤': '辰巳', '虛': '戌亥'},
        '甲辰': {'孤': '寅卯', '虛': '申酉'},
        '甲寅': {'孤': '子丑', '虛': '午未'}}
jiazi = ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉',
         '甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未',
         '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳',
         '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯',
         '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑',
         '甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']
liujiaxun = {('甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉'): '甲子',
             ('甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未'): '甲戌',
             ('甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳'): '甲申',
             ('甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯'): '甲午',
             ('甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑'): '甲辰',
             ('甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥'): '甲寅'}
jieqi2ju = {'冬至': '一七四陽', '驚蟄': '一七四陽', '小寒': '二八五陽', '大寒': '三九六陽', '春分': '三九六陽', '雨水': '九六三陽',
            '清明': '四一七陽', '立夏': '四一七陽', '立春': '八五二陽', '穀雨': '五二八陽', '小滿': '五二八陽', '芒種': '六三九陽',
            '夏至': '九三六陰', '白露': '九三六陰', '小暑': '八二五陰', '寒露': '六九三陰', '立冬': '六九三陰', '處暑': '一四七陰',
            '霜降': '五八二陰', '小雪': '五八二陰', '大雪': '四七一陰', '大暑': '七一四陰', '秋分': '七一四陰', '立秋': '二五八陰'}


# 基本功能函數
def split_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def multi_key_dict_get(d, k):
    for keys, v in d.items():
        if k in keys:
            return v
    return None


def new_list(olist, o):
    a = olist.index(o)
    res1 = olist[a:] + olist[:a]
    return res1


def new_list_r(olist, o):
    zhihead_code = olist.index(o)
    res1 = []
    for i in range(len(olist)):
        res1.append(olist[zhihead_code % len(olist)])
        zhihead_code = zhihead_code - 1
    return res1


def gendatetime(year, month, day, hour):
    return "{}年{}月{}日{}時".format(year, month, day, hour)


def repeat_list(n, thelist):
    return [repetition for i in thelist for repetition in repeat(i, n)]


# 甲子平支
# def jiazi():
#     return list(map(lambda x: "{}{}".format(tian_gan[x % len(tian_gan)],
#                                             di_zhi[x % len(di_zhi)]),
#                     list(range(60))))


def ganzhiwuxing(gangorzhi):
    gz_list = "甲寅乙卯震巽,丙巳丁午離,壬亥癸子坎,庚申辛酉乾兌,未丑戊己未辰戌艮坤".split(",")
    ganzhiwuxing_dict = dict(zip(list(map(lambda x: tuple(x), gz_list)), list("木火水金土")))
    return multi_key_dict_get(ganzhiwuxing_dict, gangorzhi)


def jieqicode(year, month, day, hour, minute):
    """以年月日時分節氣找奇門上中下元局"""
    return multi_key_dict_get({("冬至", "驚蟄"): "一七四",
                               "小寒": "二八五",
                               ("大寒", "春分"): "三九六",
                               "立春": "八五二",
                               "雨水": "九六三",
                               ("清明", "立夏"): "四一七",
                               ("穀雨", "小滿"): "五二八",
                               "芒種": "六三九",
                               ("夏至", "白露"): "九三六",
                               "小暑": "八二五",
                               ("大暑", "秋分"): "七一四",
                               "立秋": "二五八",
                               "處暑": "一四七",
                               ("霜降", "小雪"): "五八二",
                               ("寒露", "立冬"): "六九三",
                               "大雪": "四七一"},
                              jq(year, month, day, hour, minute))


def jieqicode_jq(jq):
    """以節氣名稱找奇門上中下元局"""
    return multi_key_dict_get({("冬至", "驚蟄"): "一七四",
                               "小寒": "二八五",
                               ("大寒", "春分"): "三九六",
                               "立春": "八五二",
                               "雨水": "九六三",
                               ("清明", "立夏"): "四一七",
                               ("穀雨", "小滿"): "五二八",
                               "芒種": "六三九",
                               ("夏至", "白露"): "九三六",
                               "小暑": "八二五",
                               ("大暑", "秋分"): "七一四",
                               "立秋": "二五八",
                               "處暑": "一四七",
                               ("霜降", "小雪"): "五八二",
                               ("寒露", "立冬"): "六九三",
                               "大雪": "四七一"},
                              jq)


def findyuan(year, month, day, hour, minute):
    gz = gangzhi(year, month, day, hour, minute)
    return multi_key_dict_get(findyuan_dict(), gz[2])


def find_wx_relation(zhi1, zhi2):
    combine_zhi = ganzhiwuxing(zhi1) + ganzhiwuxing(zhi2)
    return multi_key_dict_get(wuxing_relation_2, combine_zhi)


# 換算干支
def gangzhi1(year, month, day, hour, minute):
    if hour == 23:
        d = ephem.Date(round((ephem.Date("{}/{}/{} {}:00:00.00".format(
            str(year).zfill(4),
            str(month).zfill(2),
            str(day + 1).zfill(2),
            str(0).zfill(2)))), 3))
    else:
        d = ephem.Date("{}/{}/{} {}:00:00.00".format(
            str(year).zfill(4),
            str(month).zfill(2),
            str(day).zfill(2),
            str(hour).zfill(2)))
    dd = list(d.tuple())
    cdate = fromSolar(dd[0], dd[1], dd[2])
    yTG, mTG, dTG, hTG = "{}{}".format(
        tian_gan[cdate.getYearGZ().tg],
        di_zhi[cdate.getYearGZ().dz]), "{}{}".format(
        tian_gan[cdate.getMonthGZ().tg],
        di_zhi[cdate.getMonthGZ().dz]), "{}{}".format(
        tian_gan[cdate.getDayGZ().tg],
        di_zhi[cdate.getDayGZ().dz]), "{}{}".format(
        tian_gan[cdate.getHourGZ(dd[3]).tg],
        di_zhi[cdate.getHourGZ(dd[3]).dz])
    if year < 1900:
        mTG1 = find_lunar_month(yTG).get(lunar_date_d(year, month, day).get("月"))
    else:
        mTG1 = mTG
    hTG1 = find_lunar_hour(dTG).get(hTG[1])
    return [yTG, mTG1, dTG, hTG1]


def gangzhi(year, month, day, hour, minute):
    if hour == 23:
        d = ephem.Date(round((ephem.Date("{}/{}/{} {}:00:00.00".format(
            str(year).zfill(4),
            str(month).zfill(2),
            str(day + 1).zfill(2),
            str(0).zfill(2)))), 3))
    else:
        d = ephem.Date("{}/{}/{} {}:00:00.00".format(
            str(year).zfill(4),
            str(month).zfill(2),
            str(day).zfill(2),
            str(hour).zfill(2)))
    dd = list(d.tuple())
    cdate = fromSolar(dd[0], dd[1], dd[2])
    yTG, mTG, dTG, hTG = "{}{}".format(
        tian_gan[cdate.getYearGZ().tg],
        di_zhi[cdate.getYearGZ().dz]), "{}{}".format(
        tian_gan[cdate.getMonthGZ().tg],
        di_zhi[cdate.getMonthGZ().dz]), "{}{}".format(
        tian_gan[cdate.getDayGZ().tg],
        di_zhi[cdate.getDayGZ().dz]), "{}{}".format(
        tian_gan[cdate.getHourGZ(dd[3]).tg],
        di_zhi[cdate.getHourGZ(dd[3]).dz])
    if year < 1900:
        mTG1 = find_lunar_month(yTG).get(lunar_date_d(year, month, day).get("月"))
    else:
        mTG1 = mTG
    hTG1 = find_lunar_hour(dTG).get(hTG[1])
    zi = gangzhi1(year, month, day, 0, 0)[3]
    reminute = ""
    if 10 > minute >= 0:
        reminute = "00"
    if 20 > minute >= 10:
        reminute = "10"
    if 30 > minute >= 20:
        reminute = "20"
    if 40 > minute >= 30:
        reminute = "30"
    if 50 > minute >= 40:
        reminute = "40"
    if 60 > minute >= 50:
        reminute = "50"
    hourminute = str(hour) + ":" + str(reminute)
    gangzhi_minute = ke_jiazi_d(zi).get(hourminute)
    return [yTG, mTG1, dTG, hTG1, gangzhi_minute]


# 旬
def xun(gz):
    d_value1 = dict(zip(di_zhi, list(range(1, 13)))).get(gz[1])
    d_value2 = dict(zip(tian_gan, list(range(1, 11)))).get(gz[0])
    xun_value = d_value1 - d_value2
    if xun_value < 0:
        xun_value = xun_value + 12
    return {0: "戊", 10: "己", 8: "庚", 6: "辛", 4: "壬", 2: "癸"}.get(xun_value)


# 五虎遁，起正月
def find_lunar_month(year):
    fivetigers = {
        tuple(list('甲己')): '丙寅',
        tuple(list('乙庚')): '戊寅',
        tuple(list('丙辛')): '庚寅',
        tuple(list('丁壬')): '壬寅',
        tuple(list('戊癸')): '甲寅'
    }
    if multi_key_dict_get(fivetigers, year[0]) is None:
        result = multi_key_dict_get(fivetigers, year[1])
    else:
        result = multi_key_dict_get(fivetigers, year[0])
    return dict(zip(range(1, 13), new_list(jiazi, result)[:12]))


# 五鼠遁，起子時
def find_lunar_hour(day):
    fiverats = {
        tuple(list('甲己')): '甲子',
        tuple(list('乙庚')): '丙子',
        tuple(list('丙辛')): '戊子',
        tuple(list('丁壬')): '庚子',
        tuple(list('戊癸')): '壬子'
    }
    if multi_key_dict_get(fiverats, day[0]) is None:
        result = multi_key_dict_get(fiverats, day[1])
    else:
        result = multi_key_dict_get(fiverats, day[0])
    return dict(zip(list(di_zhi), new_list(jiazi, result)[:12]))


# 五馬遁，起子刻
def find_lunar_ke(hour):
    fivehourses = {
        tuple(list('丙辛')): '甲午',
        tuple(list('丁壬')): '丙午',
        tuple(list('戊癸')): '戊午',
        tuple(list('甲己')): '庚午',
        tuple(list('乙庚')): '壬午'
    }
    if multi_key_dict_get(fivehourses, hour[0]) is None:
        result = multi_key_dict_get(fivehourses, hour[1])
    else:
        result = multi_key_dict_get(fivehourses, hour[0])
    return new_list(jiazi, result)


# def liujiaxun_dict():
#     jz = jiazi[0::10]
#     jzlist = list(map(lambda x: new_list(jiazi, x)[0:10], jz))
#     nlist = list(map(lambda x: tuple(x), jzlist))
#     return dict(zip(nlist, jiazi[0::10]))


def findyuan_dict():
    jz = jiazi[0::5]
    jzlist = list(map(lambda i: new_list(jiazi, i)[0:5], jz))
    nlist = list(map(lambda x: tuple(x), jzlist))
    return dict(zip(nlist, ["上元", "中元", "下元"] * 4))


# 分干支
def minutes_jiazi_d():
    t = [f"{h}:{m}" for h in range(24) for m in range(60)]
    minutelist = dict(zip(t, cycle(repeat_list(2, jiazi()))))
    return minutelist


def ke_jiazi_d(hour):
    t = [f"{h}:{m}0" for h in range(24) for m in range(6)]
    minutelist = dict(zip(t, cycle(repeat_list(1, find_lunar_ke(hour)))))
    return minutelist


# 農曆
def lunar_date_d(year, month, day):
    lunar_m = ['占位', '正月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '冬月', '腊月']
    day_new = fromSolar(year, month, day)
    return {"年": day_new.getLunarYear(),
            "農曆月": lunar_m[int(day_new.getLunarMonth())],
            "月": day_new.getLunarMonth(),
            "日": day_new.getLunarDay()}


# 日空時空
def daykong_shikong(year, month, day, hour, minute):
    gz = gangzhi(year, month, day, hour, minute)
    dk = multi_key_dict_get(liujiaxun, gz[2])
    sk = multi_key_dict_get(liujiaxun, gz[3])
    daykong = multi_key_dict_get(guxu, dk).get("孤")
    shikong = multi_key_dict_get(guxu, sk).get("孤")
    return {"日空": daykong,
            "時空": shikong}


def hourkong_minutekong(year, month, day, hour, minute):
    gz = gangzhi(year, month, day, hour, minute)
    g3 = multi_key_dict_get(liujiaxun, gz[3])
    g4 = multi_key_dict_get(liujiaxun, gz[4])
    daykong = multi_key_dict_get(guxu, g3).get("孤")
    shikong = multi_key_dict_get(guxu, g4).get("孤")
    return {"日空": daykong, "時空": shikong}


# 奇門排局拆補
def qimen_ju_name_chaibu(year, month, day, hour, minute):
    yydun = {tuple(new_list(jieqi_name, "冬至")[0:12]): "陽遁",
             tuple(new_list(jieqi_name, "夏至")[0:12]): "陰遁"}
    jieqi = jq(year, month, day, hour, minute)
    find_yingyang = multi_key_dict_get(yydun, jieqi)
    find_yuan = findyuan(year, month, day, hour, minute)
    jieqi_code = jieqicode(year, month, day, hour, minute)
    return "{}{}局{}".format(find_yingyang, {
        "上元": jieqi_code[0],
        "中元": jieqi_code[1],
        "下元": jieqi_code[2]}.get(find_yuan),
                             find_yuan)


# 奇門排局置閏除虫用
def qimen_ju_name_zhirun_raw(year, month, day, hour, minute):
    Jieqi = jq(year, month, day, hour, minute)
    jlist = split_list(jiazi, 5)
    new_jq_list = new_list(jieqi_name, Jieqi)
    new_jq = new_jq_list[1]
    new_jq1 = new_jq_list[0]
    new_jq2 = new_jq_list[-1]
    jlist = [tuple(i) for i in jlist]
    fuhead = dict(zip(jlist, jiazi[0::5]))
    yy = {tuple(new_list(jieqi_name, "冬至")[0:12]): "陽遁",
          tuple(new_list(jieqi_name, "夏至")[0:12]): "陰遁"}
    yin_yang = multi_key_dict_get(yy, new_jq1)
    jieqi_code = jieqicode(year, month, day, hour, minute)
    dgz = gangzhi(year, month, day, hour, minute)[2]
    fd = multi_key_dict_get(fuhead, dgz)
    zftg = zhifu_tiangan(year, month, day, hour, minute)
    ju_day_dict = {tuple(["甲子", "甲午", "己卯", "己酉"]): "上元",
                   tuple(["甲寅", "甲申", "己巳", "己亥"]): "中元",
                   tuple(["甲辰", "甲戌", "己丑", "己未"]): "下元"}
    three_yuan = multi_key_dict_get(ju_day_dict, fd)
    jq_distance_ret = jq_distance(year, month, day, hour, minute)
    Jieqi_disance = jq_distance_ret[0].get(Jieqi)
    current = jq_distance_ret[1]
    current_ts = datetime.datetime.strptime(current, "%Y/%m/%d %H:%M:%S")
    jq_distance_ts = datetime.datetime.strptime(Jieqi_disance, "%Y/%m/%d %H:%M:%S")
    difference = (current_ts - jq_distance_ts).days
    kooks = {"上元": jieqi_code[0],
             "中元": jieqi_code[1],
             "下元": jieqi_code[2]}.get(three_yuan)
    jieqi_code1 = jieqicode_jq(new_jq)
    jieqi_code2 = jieqicode_jq(new_jq1)
    jieqi_code0 = jieqicode_jq(new_jq2)
    kooks1 = {"上元": jieqi_code1[0],
              "中元": jieqi_code1[1],
              "下元": jieqi_code1[2]}.get(three_yuan)
    kooks2 = {"上元": jieqi_code2[0],
              "中元": jieqi_code2[1],
              "下元": jieqi_code2[2]}.get(three_yuan)
    kooks3 = {"上元": jieqi_code0[0],
              "中元": jieqi_code0[1],
              "下元": jieqi_code0[2]}.get(three_yuan)
    lr = lunar_date_d(year, month, day)
    return {"日期時間": "{}年{}月{}日{}時{}分".format(year, month, day, hour, minute),
            "農曆": lr,
            "節氣": Jieqi,
            "距節氣差日數": difference,
            "三元": three_yuan,
            "當前節氣日期": Jieqi_disance,
            "值符天干": zftg,
            "節氣排局": jieqi_code2,
            "陰陽局": yin_yang,
            "當前排局": "{}{}局".format(yin_yang, kooks2),
            "超神接氣正授排局": "{}{}局".format(multi_key_dict_get(yy, new_jq), kooks1),
            "其他排局": "{}{}局".format(yin_yang, kooks3),
            "其他排局1": "{}{}局".format(multi_key_dict_get(yy, new_jq), kooks),
            }


# 生成阴遁阳遁表
def yinyangdun_dict(year, month, day, hour, minute):
    yinyangdun = {}

    # 阴遁阳遁表 - 大雪
    daxue_start = jq_start(year - 1, 12, 15, 12, 0)
    daxue_rizhu = gangzhi(daxue_start[0], daxue_start[1], daxue_start[2], 12, 0)[2]
    daxue_index = jiazi.index(daxue_rizhu)
    futou_index = (daxue_index // 15) * 15
    tdate = datetime.datetime(year=daxue_start[0], month=daxue_start[1], day=daxue_start[2])
    rizhu_index = daxue_index
    for i in range(daxue_index, futou_index + 15):
        yinyangdun[tdate.strftime('%Y%m%d')] = '大雪' + jiazi[rizhu_index]
        tdate += datetime.timedelta(days=1)
        rizhu_index = (rizhu_index + 1) % 60

    # 置闰 - 大雪
    jieqi_cur = '冬至'
    if daxue_index - futou_index >= 9:
        jieqi_cur = '大雪'

    # 阴遁阳遁表 - 到芒種
    jieqi_days = 0
    mangzhong_date = None
    for i in range(300):
        yinyangdun[tdate.strftime('%Y%m%d')] = jieqi_cur + jiazi[rizhu_index]
        tdate += datetime.timedelta(days=1)
        rizhu_index = (rizhu_index + 1) % 60
        jieqi_days += 1
        if jieqi_days == 15:
            jieqi_days = 0
            jieqi_cur = jieqi_name[(jieqi_name.index(jieqi_cur) + 1) % 24]
            if jieqi_cur == '芒種':
                mangzhong_date = tdate
                for j in range(15):
                    yinyangdun[tdate.strftime('%Y%m%d')] = jieqi_cur + jiazi[rizhu_index]
                    tdate += datetime.timedelta(days=1)
                    rizhu_index = (rizhu_index + 1) % 60
                break

    # 置闰 - 芒種
    mangzhong_start = jq_start(year, 6, 15, 12, 0)
    mangzhong_start_date = datetime.datetime(year=mangzhong_start[0], month=mangzhong_start[1], day=mangzhong_start[2])
    jieqi_cur = '夏至'
    if mangzhong_start_date > mangzhong_date + datetime.timedelta(days=9):
        jieqi_cur = '芒種'

    # 阴遁阳遁表 - 到大雪
    jieqi_days = 0
    daxue_date = None
    for i in range(300):
        yinyangdun[tdate.strftime('%Y%m%d')] = jieqi_cur + jiazi[rizhu_index]
        tdate += datetime.timedelta(days=1)
        rizhu_index = (rizhu_index + 1) % 60
        jieqi_days += 1
        if jieqi_days == 15:
            jieqi_days = 0
            jieqi_cur = jieqi_name[(jieqi_name.index(jieqi_cur) + 1) % 24]
            if jieqi_cur == '大雪':
                daxue_date = tdate
                for j in range(15):
                    yinyangdun[tdate.strftime('%Y%m%d')] = jieqi_cur + jiazi[rizhu_index]
                    tdate += datetime.timedelta(days=1)
                    rizhu_index = (rizhu_index + 1) % 60
                break

    # 置闰 - 大雪
    daxue_start = jq_start(year, 12, 15, 12, 0)
    daxue_start_date = datetime.datetime(year=daxue_start[0], month=daxue_start[1], day=daxue_start[2])
    jieqi_cur = '冬至'
    if daxue_start_date > daxue_date + datetime.timedelta(days=9):
        jieqi_cur = '大雪'

    # 阴遁阳遁表 - 到立春
    jieqi_days = 0
    for i in range(300):
        yinyangdun[tdate.strftime('%Y%m%d')] = jieqi_cur + jiazi[rizhu_index]
        tdate += datetime.timedelta(days=1)
        rizhu_index = (rizhu_index + 1) % 60
        jieqi_days += 1
        if jieqi_days == 15:
            jieqi_days = 0
            jieqi_cur = jieqi_name[(jieqi_name.index(jieqi_cur) + 1) % 24]
            if jieqi_cur == '立春':
                yinyangdun[tdate.strftime('%Y%m%d')] = jieqi_cur + jiazi[rizhu_index]
                break

    return yinyangdun


# 奇門排局置閏，正授，有超神，有閏奇，有接氣
def qimen_ju_name_zhirun(year, month, day, hour, minute):
    yinyangdun = yinyangdun_dict(year, month, day, hour, minute)
    date_str = '%04d%02d%02d' % (year, month, day)

    # 按23点子时为一天起点计算
    day_start_with_23 = True
    if day_start_with_23:
        tdate = datetime.datetime(year=year, month=month, day=day, hour=hour)
        tdate += datetime.timedelta(hours=1)
        date_str = tdate.strftime('%Y%m%d')

    jieqi_rizhu = yinyangdun[date_str]
    result_jieqi = jieqi_rizhu[:2]
    result_rizhu = jieqi_rizhu[2:]
    result_rizhu_index = jiazi.index(result_rizhu)
    result_futou = (result_rizhu_index // 15) * 15
    result_yuan_id = (result_rizhu_index - result_futou) // 5
    if result_yuan_id == 0:
        result_yuan = '上元'
    elif result_yuan_id == 1:
        result_yuan = '中元'
    else:
        result_yuan = '下元'
    result_jieqi_code = jieqi2ju[result_jieqi]
    return_ju = '%s遁%s局%s' % (result_jieqi_code[-1], result_jieqi_code[result_yuan_id], result_yuan)

    return return_ju


def qimen_ju_name_zhirun2(year, month, day, hour, minute):
    qdict = qimen_ju_name_zhirun_raw(year, month, day, hour, minute)
    jQ = qdict.get("節氣")
    d = qdict.get("距節氣差日數")
    tgft = qdict.get("值符天干")
    lunar_date = lunar_date_d(year, month, day)
    lunar_date_month = lunar_date.get("月")
    lunar_date_day = lunar_date.get("日")

    # 若距節氣差日數等於0或9天
    if d == 0 or d == 9:
        if lunar_date_month == 10:
            return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
        elif lunar_date_month == 11:
            return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))
        elif lunar_date_month == 12:
            return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))

    # 若距節氣差日數少或等於6天
    elif 0 < d <= 6:
        if lunar_date_month == 1 and tgft in list("戊己庚辛壬癸"):
            if lunar_date_day <= 26:
                return "{}{}".format(qdict.get('其他排局'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
        elif lunar_date_month < 9 and lunar_date_day >= 15:
            if tgft in list("戊己庚辛壬癸"):
                return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
        elif lunar_date_month <= 9 and tgft not in list("戊己庚辛壬癸"):
            return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
        elif 1 < lunar_date_month <= 9 and lunar_date_day < 10:
            if tgft in list("戊己庚辛壬癸"):
                return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('其他排局'), qdict.get('三元'))
        elif 9 <= lunar_date_month <= 10:
            if lunar_date_day < 15:
                return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('其他排局'), qdict.get('三元'))
        elif lunar_date_month == 11 and jQ == "冬至":
            if d < 3:
                return "{}{}".format(qdict.get('其他排局'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))
        elif lunar_date_month == 12:
            return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))

    elif 6 < d < 9:
        if 1 < lunar_date_month <= 6:
            if tgft not in list("戊己庚辛壬癸"):
                return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))
            elif lunar_date_day > 20:
                return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
            elif lunar_date_day > 10:
                return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
        elif lunar_date_month >= 7 and tgft in list("戊己庚辛壬癸"):
            return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
        if lunar_date_month <= 9:
            if lunar_date_day >= 15:
                if tgft in list("戊己庚辛壬癸"):
                    return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
                else:
                    return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
        elif lunar_date_month == 11 and tgft in list("戊己庚辛壬癸"):
            return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
        elif lunar_date_month == 12:
            return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))

    # 若距節氣差日數介於10至15天
    elif 10 <= d <= 15:
        if lunar_date_month == 1:
            if lunar_date_day < 15:
                return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('當前排局'), qdict.get('三元'))
        elif 2 <= lunar_date_month <= 9:
            if lunar_date_day < 15:
                return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
        elif lunar_date_month == 10:
            return "{}{}".format(qdict.get('其他排局'), qdict.get('三元'))
        elif lunar_date_month == 11:
            if d <= 12:
                return "{}{}".format(qdict.get('其他排局'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))
        elif lunar_date_month == 12:
            if jQ == "冬至":
                return "{}{}".format(qdict.get('其他排局1'), qdict.get('三元'))
            else:
                return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))

    return "{}{}".format(qdict.get('超神接氣正授排局'), qdict.get('三元'))


# 排值符
def zhifu_pai(qmju):
    yinyang = qmju[0]
    kook = qmju[2]
    pai = {"陽": {"一": "九八七一二三四五六",
                  "二": "一九八二三四五六七",
                  "三": "二一九三四五六七八",
                  "四": "三二一四五六七八九",
                  "五": "四三二五六七八九一",
                  "六": "五四三六七八九一二",
                  "七": "六五四七八九一二三",
                  "八": "七六五八九一二三四",
                  "九": "八七六九一二三四五"},
           "陰": {"九": "一二三九八七六五四",
                  "八": "九一二八七六五四三",
                  "七": "八九一七六五四三二",
                  "六": "七八九六五四三二一",
                  "五": "六七八五四三二一九",
                  "四": "五六七四三二一九八",
                  "三": "四五六三二一九八七",
                  "二": "三四五二一九八七六",
                  "一": "二三四一九八七六五"}}.get(yinyang).get(kook)
    yinlist = list(map(lambda x: x + pai, new_list_r(cnumber, kook)[0:6]))
    yanglist = list(map(lambda x: x + pai, new_list(cnumber, kook)[0:6]))
    return {"陰": dict(zip(jiazi[0::10], yinlist)),
            "陽": dict(zip(jiazi[0::10], yanglist))}.get(yinyang)


def zhishi_pai(qmju):
    yinyang = qmju[0]
    kook = qmju[2]
    new_kook = new_list(cnumber, kook)
    new_rkook = new_list_r(cnumber, kook)
    yanglist = "".join(new_kook) + "".join(new_kook) + "".join(new_kook)
    yinlist = "".join(new_rkook) + "".join(new_rkook) + "".join(new_rkook)
    yinlist1 = list(map(lambda i: i + yinlist[yinlist.index(i) + 1:][0:11], new_rkook[0:6]))
    yanglist1 = list(map(lambda i: i + yanglist[yanglist.index(i) + 1:][0:11], new_kook[0:6]))
    return {"陰": dict(zip(jiazi[0::10], yinlist1)),
            "陽": dict(zip(jiazi[0::10], yanglist1))}.get(yinyang)


# 八門
def pan_door(year, month, day, hour, minute, qmju):
    zfnzs = zhifu_n_zhishi(year, month, day, hour, minute, qmju)
    starting_door = zfnzs.get("值使門宮")[0]
    starting_gong = zfnzs.get("值使門宮")[1]
    rotate = {"陽": clockwise_eightgua,
              "陰": list(reversed(clockwise_eightgua))}.get(qmju[0])
    if starting_gong == "中":
        gong_reorder = new_list(rotate, "坤")
    else:
        gong_reorder = new_list(rotate, starting_gong)
    yydoor = {"陽": new_list(door_r, starting_door),
              "陰": new_list(list(reversed(door_r)), starting_door)}
    return dict(zip(gong_reorder, yydoor.get(qmju[0])))


# 九星
def pan_star(year, month, day, hour, minute, qmju):
    zhifunzhishi = zhifu_n_zhishi(year, month, day, hour, minute, qmju)
    star_r = list("蓬任沖輔英禽柱心")
    starting_star = zhifunzhishi.get("值符星宮")[0].replace("芮", "禽")
    starting_gong = zhifunzhishi.get("值符星宮")[1]
    rotate = {"陽": clockwise_eightgua,
              "陰": list(reversed(clockwise_eightgua))}.get(qmju[0])
    star_reorder = {"陽": new_list(star_r, starting_star),
                    "陰": new_list(list(reversed(star_r)), starting_star)}.get(qmju[0])
    if starting_gong == "中":
        gong_reorder = new_list(rotate, "坤")
    else:
        gong_reorder = new_list(rotate, starting_gong)
    return dict(zip(gong_reorder, star_reorder)), dict(zip(star_reorder, gong_reorder))


# 八神
def pan_god(year, month, day, hour, minute, qmju):
    zfzs = zhifu_n_zhishi(year, month, day, hour, minute, qmju)
    starting_gong = zfzs.get("值符星宮")[1]
    rotate = {"陽": clockwise_eightgua,
              "陰": list(reversed(clockwise_eightgua))}.get(qmju[0])
    if starting_gong == "中":
        gong_reorder = new_list(rotate, "坤")
    else:
        gong_reorder = new_list(rotate, starting_gong)
    return dict(zip(gong_reorder, {"陽": list("符蛇陰合勾雀地天"),
                                   "陰": list("符蛇陰合虎玄地天")}.get(qmju[0])))


# 找值符及值使
def zhifu_n_zhishi(year, month, day, hour, minute, qmju):
    gongs_code = dict(zip(cnumber, eight_gua))
    gz = gangzhi(year, month, day, hour, minute)
    hgan = dict(zip(tian_gan, range(0, 11))).get(gz[3][0])
    chour = multi_key_dict_get(liujiaxun, gz[3])
    eg = list("休死傷杜中開驚生景")
    eight_gods = list("蓬芮沖輔禽心柱任英")
    zspai_keys = list(zhishi_pai(qmju).keys())
    zspai_values = list(zhishi_pai(qmju).values())
    zf_keys = list(zhifu_pai(qmju).keys())
    zf_values = list(zhifu_pai(qmju).values())
    a = list(map(lambda i: dict(zip(cnumber, eg)).get(i[0]), zspai_values))
    b = list(map(lambda i: dict(zip(cnumber, eight_gods)).get(i[0]), zf_values))
    c = list(map(lambda i: gongs_code.get(i[hgan]), zf_values))
    d = list(map(lambda i: gongs_code.get(i[hgan]), zspai_values))
    door = dict(zip(zspai_keys, a)).get(chour)
    if door == "中":
        door = "死"
    return {"值符天干": [chour, jj.get(chour)],
            "值符星宮": [dict(zip(zf_keys, b)).get(chour), dict(zip(zf_keys, c)).get(chour)],
            "值使門宮": [door, dict(zip(zspai_keys, d)).get(chour)]}


def zhifu_tiangan(year, month, day, hour, minute):
    gz = gangzhi(year, month, day, hour, minute)
    jj = {"甲子": "戊", "甲戌": "己", "甲申": "庚", "甲午": "辛", "甲辰": "壬", "甲寅": "癸"}
    chour = multi_key_dict_get(liujiaxun, gz[3])
    return jj.get(chour)


def ecliptic_lon(jd_utc):
    s = ephem.Sun(jd_utc)
    equ = ephem.Equatorial(s.ra, s.dec, epoch=jd_utc)
    e = ephem.Ecliptic(equ)
    return e.lon


def sta(jd):
    e = ecliptic_lon(jd)
    n = int(e * 180.0 / math.pi / 15)
    return n


def iteration(jd, sta):
    s1 = sta(jd)
    s0 = s1
    dt = 1.0
    while True:
        jd += dt
        s = sta(jd)
        if s0 != s:
            s0 = s
            dt = -dt / 2
        if abs(dt) < 0.0000001 and s != s1:
            break
    return jd


def change(year, month, day, hour, minute):
    changets = ephem.Date("{}/{}/{} {}:{}:00".format(str(year).zfill(4),
                                                     str(month).zfill(2),
                                                     str(day).zfill(2),
                                                     str(hour).zfill(2),
                                                     str(minute).zfill(2)))
    return ephem.Date(changets - 24 * ephem.hour * 30)


def jq(year, month, day, hour, minute):
    current = ephem.Date("{}/{}/{} {}:{}:00".format(str(year).zfill(4),
                                                    str(month).zfill(2),
                                                    str(day).zfill(2),
                                                    str(hour).zfill(2),
                                                    str(minute).zfill(2)))
    jd = change(year, month, day, hour, minute)
    result = []
    e = ecliptic_lon(jd)
    n = int(e * 180.0 / math.pi / 15) + 1
    for i in range(3):
        if n >= 24:
            n -= 24
        jd = iteration(jd, sta)
        d = ephem.Date(jd + 1 / 3).tuple()
        dt = ephem.Date("{}/{}/{} {}:{}:00.00".format(d[0],
                                                      d[1],
                                                      d[2],
                                                      d[3],
                                                      d[4]).split(".")[0])
        time_info = {dt: jieqi_name[n]}
        n += 1
        result.append(time_info)
    j = [list(i.keys())[0] for i in result]
    if current > j[0] and current > j[1] and current > j[2]:
        return list(result[2].values())[0]
    if j[0] < current <= j[2] and current > j[1]:
        return list(result[1].values())[0]
    if j[1] <= current < j[2]:
        return list(result[1].values())[0]
    if current < j[1] and current < j[2]:
        return list(result[0].values())[0]


# 计算当前节气的起始日期
def jq_start(year, month, day, hour, minute):
    current = ephem.Date("{}/{}/{} {}:{}:00".format(str(year).zfill(4),
                                                    str(month).zfill(2),
                                                    str(day).zfill(2),
                                                    str(hour).zfill(2),
                                                    str(minute).zfill(2)))
    jd = change(year, month, day, hour, minute)
    result = []
    e = ecliptic_lon(jd)
    n = int(e * 180.0 / math.pi / 15) + 1
    for i in range(3):
        if n >= 24:
            n -= 24
        jd = iteration(jd, sta)
        d = ephem.Date(jd + 1 / 3).tuple()
        dt = ephem.Date("{}/{}/{} {}:{}:00.00".format(d[0], d[1], d[2], d[3], d[4]).split(".")[0])
        time_info = {dt: [d[0], d[1], d[2]]}
        n += 1
        result.append(time_info)
    j = [list(i.keys())[0] for i in result]
    if current > j[2]:
        return list(result[2].values())[0]
    elif current > j[1]:
        return list(result[1].values())[0]
    else:
        return list(result[0].values())[0]


def jq_distance(year, month, day, hour, minute):
    current = "{}/{}/{} {}:{}:00".format(str(year).zfill(4),
                                         str(month).zfill(2),
                                         str(day).zfill(2), str(hour).zfill(2),
                                         str(minute).zfill(2))
    jd = change(year, month, day, hour, minute)
    result = {}
    e = ecliptic_lon(jd)
    n = int(e * 180.0 / math.pi / 15) + 1
    for i in range(12):
        if n >= 24:
            n -= 24
        jd = iteration(jd, sta)
        d = ephem.Date(jd + 1 / 3).tuple()
        dt = "{}/{}/{} {}:{}:00.00".format(d[0], d[1], d[2],
                                           str(d[3]).zfill(2),
                                           str(d[4]).zfill(2)).split(".")[0]
        time_info = {jieqi_name[n]: dt}
        n += 1
        result.update(time_info)
    return result, current


if __name__ == '__main__':
    tic = time.perf_counter()
    year = 2020
    month = 9
    day = 10
    hour = 10
    minute = 23
    # print(jieqicode(year, month, day, hour, minute))
    # print(zhifu_pai(year, month, day, hour, minute, 1))
    # print(zhifu_pai(year, month, day, hour, minute, 2))
    # print(findyuan(year, month, day, hour, minute))
    # print(gangzhi1(year, month, day, hour, minute))
    # print(gangzhi(year, month, day, hour, minute))
    # print(find_lunar_month(year))
    # print(lunar_date_d(year, month, day))
    # print(daykong_shikong(year, month, day, hour, minute))
    # print(hourkong_minutekong(year, month, day, hour, minute))
    # print(qimen_ju_name_chaibu(year, month, day, hour, minute))
    # 值符
    # print(zhifu_pai(year, month, day, hour, minute, 1))
    # 值使
    # print(zhishi_pai(year, month, day, hour, minute, 1))
    # 门
    # print(pan_door(year, month, day, hour, minute, 1))
    # 星
    # print(pan_star(year, month, day, hour, minute, 1))
    # 神
    # print(pan_god(year, month, day, hour, minute, 1))
    # 符使
    # print(zhifu_n_zhishi(year, month, day, hour, minute, 1))
    # print(zhifu_tiangan(year, month, day, hour, minute))
    # print(change(year, month, day, hour, minute))
    # print(jq(year, month, day, hour, minute))
    # print(jq_distance(year, month, day, hour, minute))
    # print(gangzhi(year,month,day,hour,minute))
    # print(qimen_ju_name_chaibu(year,month,day,hour,minute))
    # print(xun(gz[1]))
    # print(daykong_shikong(year,month,day,hour,minute))
    # print(jq(year,month,day,hour,minute))
    # print({1:"拆補", 2:"置閏"}.get(option))
    # print(qimen_ju_name_zhirun_raw(year, month, day, hour, minute))

    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")
