import time
import itertools
from kinqimen import config


class Qimen:
    """奇門函數"""

    def __init__(self, year, month, day, hour, minute, option):
        """option 1:拆補 2:置閏"""
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.option = option
        if self.option == 1:
            self.qmju = config.qimen_ju_name_chaibu(self.year, self.month, self.day, self.hour, self.minute)
        else:
            self.qmju = config.qimen_ju_name_zhirun(self.year, self.month, self.day, self.hour, self.minute)

    def year_yuan(self):
        """搵上中下元"""
        yuan_list = [(i * 60) + 4 for i in range(22, 100)]
        three_yuan = itertools.cycle([i + "元甲子" for i in list("上中下")])
        for yuan in yuan_list:
            if self.year < yuan:
                break
            yuan1 = dict(zip(yuan_list, three_yuan)).get(yuan_list[yuan_list.index(yuan) - 1])
            return [yuan1, yuan_list[yuan_list.index(yuan) - 1]]
        return None

    def qimen_ju_day(self):
        """奇門局日"""
        ju_day_dict = {tuple(list("甲己")): "甲己日",
                       tuple(list("乙庚")): "乙庚日",
                       tuple(list("丙辛")): "丙辛日",
                       tuple(list("丁壬")): "丁壬日",
                       tuple(list("戊癸")): "戊癸日"}
        gz = config.gangzhi(self.year, self.month, self.day, self.hour, self.minute)
        try:
            find_d = config.multi_key_dict_get(ju_day_dict, gz[2][0])
        except TypeError:
            find_d = config.multi_key_dict_get(ju_day_dict, gz[2][1])
        return find_d

    # 值符
    def hourganghzi_zhifu(self):
        """時干支值符"""
        gz = config.gangzhi(self.year, self.month, self.day, self.hour, self.minute)
        jz = config.jiazi
        a = list(map(lambda x: config.new_list(jz, x)[0:10], jz[0::10]))
        b = list(map(lambda x: jz[0::10][x] + config.tian_gan[4:10][x], list(range(0, 6))))
        d = dict(zip(list(map(lambda x: tuple(x), a)), b))
        return config.multi_key_dict_get(d, gz[3])

    # 地盤
    def pan_earth(self):
        """時家奇門地盤設置"""
        return dict(zip(list(map(lambda x: dict(zip(config.cnumber, config.eight_gua)).get(x),
                                 config.new_list(config.cnumber, self.qmju[2]))),
                        {"陽遁": list("戊己庚辛壬癸丁丙乙"),
                         "陰遁": list("戊乙丙丁癸壬辛庚己")}.get(self.qmju[0:2])))

    # 逆地盤
    def pan_earth_r(self):
        """時家奇門地盤(逆)設置"""
        earth = self.pan_earth()
        pan_earth_v = list(earth.values())
        pan_earth_k = list(earth.keys())
        return dict(zip(pan_earth_v, pan_earth_k))

    # 天盤
    def pan_sky(self):
        rotate = {
            "陽": config.clockwise_eightgua,
            "陰": list(reversed(config.clockwise_eightgua))
        }.get(self.qmju[0])
        earth = self.pan_earth()
        earth_r = self.pan_earth_r()
        zhifu_n_zhishi = config.zhifu_n_zhishi(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.qmju)
        fu_head = self.hourganghzi_zhifu()[2]
        gz = config.gangzhi(self.year, self.month, self.day, self.hour, self.minute)
        fu_location = earth_r.get(gz[3][0])
        fu_head_location = zhifu_n_zhishi.get("值符星宮")[1]
        fu_head_location2 = earth_r.get(fu_head)
        gan_head = zhifu_n_zhishi.get("值符天干")[1]
        zhifu = zhifu_n_zhishi["值符星宮"][0]
        gong_reorder = config.new_list(rotate, "坤")
        a = list()
        if fu_head_location == "中":
            try:
                a = list(map(earth.get, rotate))
                gan_reorder = config.new_list(a, fu_head)
                gong_reorder = config.new_list(rotate, fu_head_location)
                return dict(zip(gong_reorder, gan_reorder))
            except ValueError:
                if config.pan_god(self.year, self.month, self.day, self.hour, self.minute, self.qmju).get("坤") != "符":
                    a = list(map(earth.get, rotate))
                    return dict(zip(gong_reorder, config.new_list(a, earth.get("坤"))))
                if earth.get("坤") == gan_head:
                    a = list(map(earth.get, rotate))
                    return dict(zip(gong_reorder, config.new_list(a, list(reversed(a))[0])))
                else:
                    try:
                        return dict(zip(gong_reorder, config.new_list(a, gan_head)))
                    except ValueError:
                        return dict(zip(gong_reorder, config.new_list(a, earth.get("坤"))))

        if fu_head_location != "中" and zhifu != "禽" and fu_head_location2 != "中":
            newlist = list(map(earth.get, rotate))
            gan_reorder = config.new_list(newlist, fu_head)
            gong_reorder = config.new_list(rotate, fu_head_location)
            if fu_head not in gan_reorder:
                start = dict(zip(config.cnumber, gan_reorder)).get(self.qmju[2])
                rgan_reorder = config.new_list(gan_reorder, start)
                rgong_reorder = config.new_list(gong_reorder, fu_location)
                aa = dict(zip(rgong_reorder, rgan_reorder))
                bb = dict(zip(rgan_reorder, rgong_reorder))
                return aa, bb
            if fu_head in gan_reorder:
                if fu_location is None:
                    return earth
                return {**dict(zip(gong_reorder, gan_reorder)),
                        **{"中": earth.get("中")}}
        if fu_head_location != "中" and zhifu == "禽" and fu_head_location2 == "中":
            gg = list(map(earth.get, rotate))
            gan_reorder = config.new_list(gg, earth.get("坤"))
            gong_reorder = config.new_list(rotate, fu_head_location)
            if fu_head not in gan_reorder:
                rgong_reorder = config.new_list(gong_reorder, fu_location)
                return dict(zip(rgong_reorder, gan_reorder))
            return {**dict(zip(gong_reorder, gan_reorder)),
                    **{"中": earth[0].get("中")}}

    def pan(self):
        """時家奇門起盤綜合"""
        gz = config.gangzhi(self.year, self.month, self.day, self.hour, self.minute)
        gzd = "{}年{}月{}日{}時".format(gz[0], gz[1], gz[2], gz[3])
        xunhead = config.xun(gz[2])
        xunkong = config.daykong_shikong(self.year, self.month, self.day, self.hour, self.minute)
        j_q = config.jq(self.year, self.month, self.day, self.hour, self.minute)
        zfzs = config.zhifu_n_zhishi(self.year, self.month, self.day, self.hour, self.minute, self.qmju)
        pan_star_result = config.pan_star(self.year, self.month, self.day, self.hour, self.minute, self.qmju)
        star = pan_star_result[0]
        door = config.pan_door(self.year, self.month, self.day, self.hour, self.minute, self.qmju)
        god = config.pan_god(self.year, self.month, self.day, self.hour, self.minute, self.qmju)

        return {
            "排盤方式": {1: "拆補", 2: "置閏"}.get(self.option),
            "干支": gzd,
            "旬首": xunhead,
            "旬空": xunkong,
            "局日": self.qimen_ju_day(),
            "排局": self.qmju,
            "節氣": j_q,
            "值符值使": zfzs,
            "天盤": self.pan_sky(),
            "地盤": self.pan_earth(),
            "門": door,
            "星": star,
            "神": god,
        }

    def overall(self):
        """整體奇門起盤綜合"""
        return {"時家奇門": self.pan()}


if __name__ == '__main__':
    tic = time.perf_counter()
    # start_datetime = datetime(2024, 5, 1, 0, 0)
    # end_datetime = datetime(2024, 5, 30, 23, 0)  # Adjust as needed
    # print(test_qimen(start_datetime, end_datetime))

    # qtext = Qimen(2000,9,10,10,20,1).pan()
    # qtext = Qimen(2024, 7, 11, 18, 0, 2).pan()
    # print(qtext)

    # qtext = Qimen(2022, 12, 22, 5, 0, 2).pan()
    # qtext = Qimen(2022, 12, 22, 6, 0, 2).pan()
    # qtext = Qimen(2022, 12, 21, 6, 0, 2).pan()
    # qtext = Qimen(2022, 12, 23, 6, 0, 2).pan()
    # qtext = Qimen(2022, 12, 26, 23, 0, 2).pan()
    # qtext = Qimen(2022, 12, 31, 22, 0, 2).pan()
    # qtext = Qimen(2022, 12, 31, 23, 0, 2).pan()
    # qtext = Qimen(2023, 1, 1, 4, 0, 2).pan()
    # qtext = Qimen(2023, 1, 1, 6, 0, 2).pan()
    # qtext = Qimen(2024, 1, 15, 22, 0, 2).pan()
    qtext = Qimen(2024, 1, 15, 23, 1, 2).pan()
    # qtext = Qimen(2024, 1, 20, 22, 1, 2).pan()
    print(qtext)

    complete_star_zhifu = {'禽':'天禽', '柱':'天柱', '心':'天心', '英':'天英', '蓬':'天蓬', '輔':'天辅', '沖':'天冲', '任':'天任', '芮':'天芮'}
    complete_star = {'禽':'芮禽', '柱':'天柱', '心':'天心', '英':'天英', '蓬':'天蓬', '輔':'天辅', '沖':'天冲', '任':'天任', '芮':'芮禽'}
    complete_door = {'休':'休门', '生':'生门', '傷':'伤门', '開':'开门', '杜':'杜门', '驚':'惊门', '死':'死门', '景':'景门'}
    complete_godd = {'玄':'玄武', '地':'九地', '天':'九天', '虎':'白虎', '符':'值符', '合':'六合', '陰':'太阴', '蛇':'螣蛇', '雀':'玄武', '勾':'白虎'}

    print('———————————————————————————————')
    print('　' + qtext.get('干支').replace('年', '　').replace('月', '　').replace('日', '　').replace('時', '　'))
    print('　　　%s　%s　%s' % (''.join(qtext.get('值符值使').get('值符天干')), qtext.get('旬空').get('日空'), qtext.get('旬空').get('時空')))
    print('%s　%s　%s' % (qtext.get('排局').replace('陽', '阳').replace('陰', '阴'), complete_star_zhifu.get(qtext.get('值符值使').get('值符星宮')[0]), complete_door.get(qtext.get('值符值使').get('值使門宮')[0])))
    print('———————————————————————————————')
    print('  %s %s  |  %s %s  |  %s %s' % (qtext.get("天盤").get('巽'), complete_star.get(qtext.get("星").get('巽')), qtext.get("天盤").get('離'), complete_star.get(qtext.get("星").get('離')), qtext.get("天盤").get('坤'), complete_star.get(qtext.get("星").get('坤'))))
    print('  　 %s  |  　 %s  |  　 %s' % (complete_door.get(qtext.get("門").get('巽')), complete_door.get(qtext.get("門").get('離')), complete_door.get(qtext.get("門").get('坤'))))
    print('  %s %s  |  %s %s  |  %s %s' % (qtext.get("地盤").get('巽'), complete_godd.get(qtext.get("神").get('巽')), qtext.get("地盤").get('離'), complete_godd.get(qtext.get("神").get('離')), qtext.get("地盤").get('坤'), complete_godd.get(qtext.get("神").get('坤'))))
    print('———————————————————————————————')
    print('  %s %s  |  　 　　  |  %s %s' % (qtext.get("天盤").get('震'), complete_star.get(qtext.get("星").get('震')), qtext.get("天盤").get('兌'), complete_star.get(qtext.get("星").get('兌'))))
    print('  　 %s  |  　 　　  |  　 %s' % (complete_door.get(qtext.get("門").get('震')), complete_door.get(qtext.get("門").get('兌'))))
    print('  %s %s  |  %s 　　  |  %s %s' % (qtext.get("地盤").get('震'), complete_godd.get(qtext.get("神").get('震')), qtext.get("地盤").get('中'), qtext.get("地盤").get('兌'), complete_godd.get(qtext.get("神").get('兌'))))
    print('———————————————————————————————')
    print('  %s %s  |  %s %s  |  %s %s' % (qtext.get("天盤").get('艮'), complete_star.get(qtext.get("星").get('艮')), qtext.get("天盤").get('坎'), complete_star.get(qtext.get("星").get('坎')), qtext.get("天盤").get('乾'), complete_star.get(qtext.get("星").get('乾'))))
    print('  　 %s  |  　 %s  |  　 %s' % (complete_door.get(qtext.get("門").get('艮')), complete_door.get(qtext.get("門").get('坎')), complete_door.get(qtext.get("門").get('乾'))))
    print('  %s %s  |  %s %s  |  %s %s' % (qtext.get("地盤").get('艮'), complete_godd.get(qtext.get("神").get('艮')), qtext.get("地盤").get('坎'), complete_godd.get(qtext.get("神").get('坎')), qtext.get("地盤").get('乾'), complete_godd.get(qtext.get("神").get('乾'))))
    print('———————————————————————————————')

    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")
