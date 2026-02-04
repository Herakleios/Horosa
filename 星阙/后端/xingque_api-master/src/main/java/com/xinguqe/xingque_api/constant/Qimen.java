package com.xinguqe.xingque_api.constant;

import java.util.HashMap;
import java.util.Map;

public class Qimen {
    public static final String XUNKONG = "旬空";
    public static final String PAIJU = "排局";
    public static final String ZHIFUSHI = "值符值使";
    public static final String TIANPAN = "天盘";
    public static final String DIPAN = "地盘";
    public static final String MEN = "门";
    public static final String XING = "星";
    public static final String SHEN = "神";

    public static final Map<String,String> QIMEN_PAN = new HashMap<String,String>(){{
        put(XUNKONG,"xunkong");
        put(PAIJU,"paiju");
        put(ZHIFUSHI,"zhifushi");
        put(TIANPAN,"tianpan");
        put(DIPAN,"dipan");
        put(MEN,"men");
        put(XING,"xing");
        put(SHEN,"shen");
    }};

    public static final String[] QIMEN_KEY_KEEP_KEY = new String[]{
      XUNKONG,PAIJU
    };

    public static final String[] QIMEN_DICT_KEY = new String[]{
      TIANPAN,DIPAN,MEN,XING,SHEN
    };

    public static final Map<String,String> QIMEN_DICT_KEY_MAP = new HashMap<String,String>(){{
       put(MEN,"bamen");
       put(XING,"jiuxing");
       put(SHEN,"bashen");
    }};
}
