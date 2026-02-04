package com.xinguqe.xingque_api.constant;

import java.util.HashMap;
import java.util.Map;

public class LiuRen {
    public static final String TIANPAN = "地转天盘";
    public static final String TIANGAN = "地转天干";
    public static final String TIANJIANG = "地转天将";
    public static final String TIANDIPAN = "天地盘";
    public static final String SIKE = "四课";
    public static final String SANCHUAN = "三传";
    public static final String GEJU = "格局";
    public static final String YUEJIANG = "月将";

    private static final String C_CHUCHUAN = "初传";
    private static final String C_ZHONGCHUAN = "中传";
    private static final String C_MOCHUAN = "末传";

    private static final String KE_YIKE = "一课";
    private static final String KE_ERKE = "二课";
    private static final String KE_SANKE = "三课";
    private static final String KE_SIKE = "四课";

    public static final Map<String,String> LIU_REN_PAN = new HashMap<String,String>(){{
        put(TIANDIPAN,"dipan");
        put(TIANPAN,"tianpan");
        put(TIANJIANG,"tianjiang");
        put(SIKE,"sike");
        put(SANCHUAN,"sanchuan");
        put(GEJU,"geju");
        put(YUEJIANG,"yuejiang");
        put(TIANGAN,"tiangan");
    }};

    public static final String[] LIU_REN_KEEP_KEY = new String[]{
            TIANDIPAN,TIANJIANG,TIANPAN,GEJU,YUEJIANG, TIANGAN
    };

    public static final Map<String,String> LIU_REN_SANCHUAN = new HashMap<String,String>(){{
        put(C_CHUCHUAN,"1");
        put(C_ZHONGCHUAN,"2");
        put(C_MOCHUAN,"3");
    }};

    public static final Map<String,String> LIU_REN_SIKE = new HashMap<String,String>(){{
        put(KE_YIKE,"1");
        put(KE_ERKE,"2");
        put(KE_SANKE,"3");
        put(KE_SIKE,"4");
    }};

    public static final Map<Integer,Integer> HUOSHI = new HashMap<Integer,Integer>(){{
        put(1,0);
        put(2,2);
        put(3,4);
        put(4,6);
        put(5,8);
        put(6,10);
        put(7,12);
        put(8,14);
        put(9,16);
        put(10,18);
        put(11,20);
        put(0,22);
    }};
    public static final Map<Integer,String> HUOSHI_ZHI = new HashMap<Integer,String>(){{
        put(1,"子");
        put(2,"丑");
        put(3,"寅");
        put(4,"卯");
        put(5,"辰");
        put(6,"巳");
        put(7,"午");
        put(8,"未");
        put(9,"申");
        put(10,"酉");
        put(11,"戌");
        put(0,"亥");
    }};
}
