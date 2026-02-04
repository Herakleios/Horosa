package com.xinguqe.xingque_api.constant;

import java.util.HashMap;
import java.util.Map;

public class SixLines {

//    private static final String GONG = "本卦";
    public static final String NAME = "卦";
    public static final String GUA = "世应卦";
    public static final String BEN_GUA = "本卦";
    public static final String ZHI_GUA = "之卦";
    public static final String LIUQIN = "六亲用神";
    public static final String LIUSHOU = "六兽";
    public static final String TIANGAN = "天干";
    public static final String DIZHI = "地支";
    public static final String FUSHEN = "伏神";
    public static final String SHIYING = "世应爻";
    public static final String VALUE = "value";

    public static final Map<String,Integer> JIEQI = new HashMap<String,Integer>(){{
       put("立春",1);
       put("雨水",1);
       put("惊蛰",1);
       put("春分",1);
       put("清明",1);
       put("谷雨",1);
       put("立夏",1);
       put("小满",1);
       put("芒种",1);
       put("夏至",1);
       put("小暑",2);
       put("大暑",2);
       put("立秋",2);
       put("处暑",2);
       put("白露",2);
       put("秋分",2);
       put("寒露",2);
       put("霜降",2);
       put("立冬",2);
       put("小雪",2);
       put("大雪",2);
       put("冬至",2);
       put("小寒",1);
       put("大寒",1);
    }};

    public static final Map<String,String> SIX_LIENS_GUA = new HashMap<String,String>(){{
        put(BEN_GUA,"gua");
        put(ZHI_GUA,"change_gua");
    }};

    public static final Map<String,String> SIX_LIENS_GUA_INFO = new HashMap<String,String>(){{
        put(NAME,"name");
        put(GUA,"gua");
        put(LIUQIN,"liuqin");
        put(LIUSHOU,"liushou");
        put(TIANGAN,"tiangan");
        put(DIZHI,"dizhi");
        put(FUSHEN,"fushen");
        put(SHIYING,"shiying");
        put(VALUE,"value");
    }};

    public static final String[] SIX_LIENS_GUA_INFO_KEY = new String[]{
            LIUQIN,LIUSHOU,TIANGAN,DIZHI,VALUE
    };

    public static final String[] SIX_LIENS_GUA_INFO_CHANGE = new String[]{
            NAME,GUA,SHIYING
    };
}
