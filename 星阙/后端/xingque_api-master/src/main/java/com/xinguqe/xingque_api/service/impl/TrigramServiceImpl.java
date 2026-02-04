package com.xinguqe.xingque_api.service.impl;

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.github.pagehelper.PageHelper;
import com.xinguqe.xingque_api.config.GuaConfig;
import com.xinguqe.xingque_api.config.QimenConfig;
import com.xinguqe.xingque_api.config.SixLinesConfig;
import com.xinguqe.xingque_api.config.TrigramServiceConfig;
import com.xinguqe.xingque_api.constant.LiuRen;
import com.xinguqe.xingque_api.constant.Qimen;
import com.xinguqe.xingque_api.constant.SixLines;
import com.xinguqe.xingque_api.dto.request.LiuRenVO;
import com.xinguqe.xingque_api.dto.request.PageVO;
import com.xinguqe.xingque_api.dto.request.QimenVO;
import com.xinguqe.xingque_api.dto.request.SixLineVO;
import com.xinguqe.xingque_api.dto.response.PageDataRsp;
import com.xinguqe.xingque_api.entity.*;
import com.xinguqe.xingque_api.mapper.QuickLinkMapper;
import com.xinguqe.xingque_api.mapper.UserTrigramRecordMapper;
import com.xinguqe.xingque_api.service.TrigramService;
import com.xinguqe.xingque_api.utils.md5.Md5Utils;
import lombok.extern.slf4j.Slf4j;
import okhttp3.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.*;

@Slf4j
@Service

public class TrigramServiceImpl implements TrigramService {

    @Autowired
    private OkHttpClient okhttpClient;

    @Autowired
    private TrigramServiceConfig trigramServiceConfig;

    @Autowired
    private SixLinesConfig sixLinesConfig;

    @Autowired
    private QimenConfig qimenConfig;

    @Autowired
    private GuaConfig guaConfig;

    @Autowired
    private UserTrigramRecordMapper userTrigramRecordMapper;

    public Map<String, Object> reqSixLine(SixLineVO data) throws Exception {

        //请求数据
        String url = trigramServiceConfig.getUrl("/liuyao");
        ObjectMapper mapper = new ObjectMapper();
        String dataStr = mapper.writeValueAsString(data);
        JsonNode rsp = this.request(url, dataStr);

        Map<String, Object> res = new HashMap<>();

        // 解析json数据 拼装返回
        if (data.guaType == 1 || data.guaType == 2) {
            rsp.fields().forEachRemaining(entry -> {
                String key = entry.getKey();
                JsonNode item = entry.getValue();

                Map<String, Object> gua = new HashMap<>();

                if (key.equals("本卦") || key.equals("之卦")) {

                    item.fields().forEachRemaining(entry2 -> {
                        String key2 = entry2.getKey();
                        JsonNode item2 = entry2.getValue();

                        //是否是需要的key
                        if (Arrays.asList(SixLines.SIX_LIENS_GUA_INFO_KEY).contains(key2)) {
                            gua.put(SixLines.SIX_LIENS_GUA_INFO.get(key2), item2);
                        } else if (key2.equals(SixLines.NAME)) {
                            //世应爻  卦  宫 特殊处理  预定义配置文件
                            String value = item.get(SixLines.VALUE).asText();
                            String newValue = value.replace("9", "7").replace("6", "8");
                            System.out.println(sixLinesConfig.getGua().get("888888"));
                            Map<String, Object> config = sixLinesConfig.getGua().get(newValue);
                            gua.putAll(config);

                        } else if (key2.equals(SixLines.FUSHEN)) {
                            List<Map<String, Object>> fuArr = new ArrayList<>();
                            for (JsonNode fu : item2) {
                                Integer i = fu.get("伏神排爻数字").asInt();
                                String yao = fu.get("伏神爻").asText();
                                Map<String, Object> fuItem = new HashMap<String, Object>() {{
                                    put("index", i);
                                    put("name", yao.substring(0, 3));
                                }};
                                fuArr.add(fuItem);
                            }
                            gua.put(SixLines.SIX_LIENS_GUA_INFO.get(key2), fuArr);
                        }

                    });
                    gua.put("tiangan",sixLineGan(gua.get("value").toString(),data.jieqi));

                    res.put(SixLines.SIX_LIENS_GUA.get(key), gua);
                }

            });
        } else if (data.guaType == 3) {
            String guaValue = rsp.get("本卦").get("value").asText().replace("9", "7").replace("6", "8");
            res.put("gua", new HashMap<String, Object>() {{
                put("value", guaValue);
                putAll(sixLinesConfig.getGua().get(guaValue));
            }});

            if (rsp.get("之卦") != null) {
                String v = rsp.get("之卦").get("value").asText();
                res.put("change_gua", new HashMap<String, Object>() {{
                    put("value", v);
                    putAll(sixLinesConfig.getGua().get(v));
                }});
            } else {
                res.put("change_gua", new HashMap<String, Object>() {{
                    put("value", guaValue);
                    putAll(sixLinesConfig.getGua().get(guaValue));
                }});
            }

            String huGua = String.valueOf(guaValue.charAt(1)) + guaValue.charAt(2) + guaValue.charAt(3) + guaValue.charAt(2) + guaValue.charAt(3) + guaValue.charAt(4);
            String cuoGua = guaValue.replace("7", "9").replace("8", "7").replace("9", "8");
            String zGua = String.valueOf(guaValue.charAt(5)) + guaValue.charAt(4) + guaValue.charAt(3) + guaValue.charAt(2) + guaValue.charAt(1) + guaValue.charAt(0);
            res.put("hu_gua", new HashMap<String, Object>() {{
                put("value", huGua);
                putAll(sixLinesConfig.getGua().get(huGua));
            }});
            res.put("cuo_gua", new HashMap<String, Object>() {{
                put("value", cuoGua);
                putAll(sixLinesConfig.getGua().get(cuoGua));
            }});
            res.put("zong_gua", new HashMap<String, Object>() {{
                put("value", zGua);
                putAll(sixLinesConfig.getGua().get(zGua));
            }});
        }

        //todo 处理天干 拆分上下两卦

        return res;
    }

    private List<String> sixLineGan(String gua , String jieqi) {
        List<String> res = new ArrayList<>();

        String up =  gua.substring(1,4).replace("9", "7").replace("6", "8");
        String down = gua.substring(4,7).replace("9", "7").replace("6", "8");

        Map<String, JsonNode> upGua = guaConfig.getGua().get(up);
        Map<String, JsonNode> downGua = guaConfig.getGua().get(down);

        JsonNode upGan = upGua.get("up");
        JsonNode downGan = downGua.get("down");

        if (upGua.get("gua").asText().contains("乾") || upGua.get("gua").asText().contains("坤")){
            int change = najia(jieqi);
            if (change == 2){
                upGan =  upGua.get("down");;
            }
        }

        if (downGua.get("gua").asText().contains("乾") || downGua.get("gua").asText().contains("坤")){
            int change = najia(jieqi);
            if (change == 2){
                downGan =  downGua.get("up");;
            }
        }

        for (JsonNode u : upGan){
            res.add(u.asText());
        }
        for (JsonNode u : downGan){
            res.add(u.asText());
        }

        return res;
    }

    // 计算 乾 坤 两卦是否要反转 节气在 1： 冬至-夏至 2： 夏至-冬至
    private int najia(String jieqi)
    {
        return SixLines.JIEQI.get(jieqi);
    }

    public Map<String, Object> reqLiuRen(LiuRenVO data) throws Exception {

        //活时处理
        int r = 0;
        if (data.hourNum != 0){
            r = Math.floorMod(data.hourNum, 12);
            data.datetimeVO.hour = LiuRen.HUOSHI.get(r);
        }

        //请求数据
        String url = trigramServiceConfig.getUrl("/liuren");
        ObjectMapper mapper = new ObjectMapper();
        String dataStr = mapper.writeValueAsString(data);
        log.error(dataStr);
        JsonNode rsp = this.request(url, dataStr);

        //处理数据
        Map<String, Object> res = new HashMap<>();

        rsp.fields().forEachRemaining(entry -> {
            //地转天盘  地转天将 格局
            String key = entry.getKey();
            JsonNode item = entry.getValue();

            if (Arrays.asList(LiuRen.LIU_REN_KEEP_KEY).contains(key)) {
                res.put(LiuRen.LIU_REN_PAN.get(key), item);
            } else if (key.equals(LiuRen.SIKE)) {
                // 处理四课
                Map<String, String> sike = new HashMap<>();
                item.fields().forEachRemaining(entry2 -> {
                    String key2 = entry2.getKey();
                    JsonNode item2 = entry2.getValue();

                    String value = item2.get(1).asText() + item2.get(0).asText();
                    sike.put(LiuRen.LIU_REN_SIKE.get(key2), value);
                });

                res.put(LiuRen.LIU_REN_PAN.get(key), sike);

            } else if (key.equals(LiuRen.SANCHUAN)) {
                //处理三传
                Map<String, String> sanchuan = new HashMap<>();
                item.fields().forEachRemaining(entry2 -> {
                    String key2 = entry2.getKey();
                    JsonNode item2 = entry2.getValue();

                    String value = item2.get(2).asText() + item2.get(3).asText() + item2.get(0).asText() + item2.get(1).asText();

                    sanchuan.put(LiuRen.LIU_REN_SANCHUAN.get(key2), value);
                });

                res.put(LiuRen.LIU_REN_PAN.get(key), sanchuan);

            }
        });
        if (data.hourNum != 0){
            res.put("huoshi", LiuRen.HUOSHI_ZHI.get(r));
        }
        return res;
    }

    public Map<String, Object> reqQimen(QimenVO data) throws Exception {

        log.error("start qimen");
        //请求数据
        String url = trigramServiceConfig.getUrl("/qimen");
        ObjectMapper mapper = new ObjectMapper();
        String dataStr = mapper.writeValueAsString(data);
        JsonNode rsp = this.request(url, dataStr);

        //处理数据
        Map<String, Object> res = new HashMap<>();
        Map<String, Object> gua = qimenConfig.getGua().get("gua");
        rsp.fields().forEachRemaining(entry -> {
            String key = entry.getKey();
            JsonNode item = entry.getValue();

            if (Arrays.asList(Qimen.QIMEN_KEY_KEEP_KEY).contains(key)) {
                if (key.equals(Qimen.XUNKONG)){

                    Map<String,Object> xunkong = new HashMap<>();

                    Map<String,Object> dipan = qimenConfig.getGua().get("dipan");
                    item.fields().forEachRemaining(entry2 -> {
                        String key2 = entry2.getKey();
                        JsonNode item2 = entry2.getValue();
                        String item2Str = item2.asText();

                        String s1 = item2Str.substring(0,1);
                        String s2 = item2Str.substring(1,2);

                        xunkong.put(key2,new HashSet<>(Arrays.asList(dipan.get(s1),dipan.get(s2))));
                    });
                    res.put(Qimen.QIMEN_PAN.get(key), xunkong);
                }else {
                    res.put(Qimen.QIMEN_PAN.get(key), item);
                }
            } else if (Arrays.asList(Qimen.QIMEN_DICT_KEY).contains(key)) {
                Map<String, Object> dictKey = new HashMap<>();
                if (Qimen.QIMEN_DICT_KEY_MAP.containsKey(key)) {
                    Map<String, Object> dict = qimenConfig.getGua().get(Qimen.QIMEN_DICT_KEY_MAP.get(key));
                    item.fields().forEachRemaining(entry2 -> {
                        String key2 = entry2.getKey();
                        JsonNode item2 = entry2.getValue();

                        dictKey.put(gua.get(key2).toString(), item2.asText());
                    });
                } else {
                    item.fields().forEachRemaining(entry2 -> {
                        String key2 = entry2.getKey();
                        JsonNode item2 = entry2.getValue();

                        dictKey.put(gua.get(key2).toString(), item2.asText());
                    });
                }
                res.put(Qimen.QIMEN_PAN.get(key), dictKey);
            } else if (key.equals(Qimen.ZHIFUSHI)) {

                Map<String, String> zhi = new HashMap<>();

                //值符值使
                String zhiFu = item.get("值符星宫").get(0).asText();
                String zhiShi = item.get("值使门宫").get(0).asText();
//                log.error("start qimen " + qimenConfig.getGua().get("jiuxing"));
                zhi.put("xing", qimenConfig.getGua().get("jiuxing").get(zhiFu).toString());
                zhi.put("shi", qimenConfig.getGua().get("bamen").get(zhiShi).toString());

                res.put(Qimen.QIMEN_PAN.get(key), zhi);
            }
        });

        res.put("dipan_map",qimenConfig.getGua().get("dipan"));

        return res;

    }

    public PageDataRsp<List<UserTrigramRecordWithBLOBs>> recordList(PageVO pageVO,int userId){
        UserTrigramRecordExample userTrigramRecordExample = new UserTrigramRecordExample();
        UserTrigramRecordExample.Criteria criteria = userTrigramRecordExample.createCriteria();
        criteria.andUserIdEqualTo(userId);

        long count = userTrigramRecordMapper.countByExample(userTrigramRecordExample);
        PageHelper.startPage(pageVO.page, pageVO.pageSize);
        userTrigramRecordExample.setOrderByClause("modified_time desc");
        List<UserTrigramRecordWithBLOBs> userTrigramRecord = userTrigramRecordMapper.selectByExampleWithBLOBs(userTrigramRecordExample);

        PageDataRsp<List<UserTrigramRecordWithBLOBs>> data = new PageDataRsp<>();
        data.setTotal(count);
        data.setData(userTrigramRecord);
        return data;
    }

    public <T> Integer addRecord(int userId,String inputKey,int type,T req,T rsp,T extrasData,int saveTpe) throws JsonProcessingException {
        UserTrigramRecordWithBLOBs userTrigramRecord = new UserTrigramRecordWithBLOBs();

        ObjectMapper objectMapper = new ObjectMapper();
        String input = objectMapper.writeValueAsString(req);
        String output = objectMapper.writeValueAsString(rsp);
        String extras = objectMapper.writeValueAsString(extrasData);

//        Integer userId = 1;

//        String inputKey = Md5Utils.encryptMD5(input);

        //userid
        userTrigramRecord.setUserId(userId);
        userTrigramRecord.setStatus(1);
        userTrigramRecord.setType(type);
        userTrigramRecord.setSaveType(saveTpe);
        userTrigramRecord.setInputKey(inputKey);
        userTrigramRecord.setInput(input);
        userTrigramRecord.setOutput(output);
        userTrigramRecord.setExtras(extras);

        //查询是否存在
        UserTrigramRecordExample recordExistExample = new UserTrigramRecordExample();
        UserTrigramRecordExample.Criteria criteriaExist = recordExistExample.createCriteria();
        criteriaExist.andUserIdEqualTo(userId).andTypeEqualTo(type).andInputKeyEqualTo(inputKey);
        List<UserTrigramRecord> recordExist = userTrigramRecordMapper.selectByExample(recordExistExample);
        //如果存在就修改
        if (!recordExist.isEmpty()){
            UserTrigramRecord recordData = recordExist.get(0);
            userTrigramRecord.setId(recordData.getId());

            userTrigramRecordMapper.updateByPrimaryKeyWithBLOBs(userTrigramRecord);

            return  recordData.getId();
        }
        //不存在则新增
        else {
            //查询是否超过100
//        userTrigramRecord.withUserId(userId);
            UserTrigramRecordExample userTrigramRecordExample = new UserTrigramRecordExample();
            UserTrigramRecordExample.Criteria criteria = userTrigramRecordExample.createCriteria();
            userTrigramRecordExample.setOrderByClause("id desc");
            criteria.andUserIdEqualTo(userId);
            List<Integer> ids = userTrigramRecordMapper.selectIdByExample(userTrigramRecordExample);
            //超过100 删除数据
            if (ids.size() > 100){
                //每个用户每个保存方式最多100条 删除多余数据
                int i = 1;
                List<Integer> delId = new ArrayList<>();
                for (Integer id : ids){
                    if (i > 99){
                        delId.add(id);
                    }
                    i++;
                }
                criteria.andIdIn(delId);
                userTrigramRecordMapper.deleteByExample(userTrigramRecordExample);
            }
            userTrigramRecordMapper.insert(userTrigramRecord);
            return userTrigramRecord.getId();
        }
    }

    public int delRecord(int userId,int recordId){
        UserTrigramRecordExample userTrigramRecordExample = new UserTrigramRecordExample();
        UserTrigramRecordExample.Criteria criteria = userTrigramRecordExample.createCriteria();
        criteria.andUserIdEqualTo(userId).andIdEqualTo(recordId);

        return userTrigramRecordMapper.deleteByExample(userTrigramRecordExample);
    }

    private JsonNode request(String url, String data) throws Exception {

        RequestBody requestBody = RequestBody.create(data, MediaType.parse("application/json;charset=utf-8"));

        Request request = new Request.Builder().post(requestBody).url(url).build();

        try (Response response = okhttpClient.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new IOException("Unexpected code " + response);
            }
            assert response.body() != null;

            String str = Objects.requireNonNull(response.body().string());
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readTree(str);
        }
    }

}
