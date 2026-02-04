package com.xinguqe.xingque_api.service;

import com.xinguqe.xingque_api.dto.request.PageVO;
import com.xinguqe.xingque_api.dto.request.TrigramBookVO;
import com.xinguqe.xingque_api.dto.response.PageDataRsp;
import com.xinguqe.xingque_api.entity.UserTrigramBook;
import com.xinguqe.xingque_api.exception.HorosaException;

import java.util.List;

public interface TrigramBookService {
    PageDataRsp<List<UserTrigramBook>> listPage(PageVO pageVO,int userId);
    int add(TrigramBookVO trigramBookVO, int userId) throws HorosaException;
    int modify(TrigramBookVO trigramBookVO,int userId);
    int del(int id,int userId);
}
