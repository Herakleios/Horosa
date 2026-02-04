package com.xinguqe.xingque_api.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.xinguqe.xingque_api.dto.request.LiuRenVO;
import com.xinguqe.xingque_api.dto.request.PageVO;
import com.xinguqe.xingque_api.dto.request.QimenVO;
import com.xinguqe.xingque_api.dto.request.SixLineVO;
import com.xinguqe.xingque_api.dto.response.PageDataRsp;
import com.xinguqe.xingque_api.entity.QuickLink;
import com.xinguqe.xingque_api.entity.UserTrigramRecordWithBLOBs;

import java.util.List;
import java.util.Map;

public interface TrigramService {
    Map<String,Object> reqSixLine(SixLineVO data) throws Exception;

    Map<String,Object> reqLiuRen(LiuRenVO data) throws Exception ;

    Map<String, Object> reqQimen(QimenVO data) throws Exception;
    <T> Integer addRecord(int userId,String inputKey,int type,T req,T rsp,T extrasData,int saveTpe) throws JsonProcessingException;
    int delRecord(int userId,int recordId);
    PageDataRsp<List<UserTrigramRecordWithBLOBs>> recordList(PageVO pageVO, int userId);

}
