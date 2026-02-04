package com.xinguqe.xingque_api.service;

import com.xinguqe.xingque_api.dto.admin.request.DelSuggestVO;
import com.xinguqe.xingque_api.dto.admin.response.PageDataRsp;
import com.xinguqe.xingque_api.dto.admin.request.PageVO;
import com.xinguqe.xingque_api.entity.UserSuggest;

import java.util.List;

public interface AdminSuggestService {
    PageDataRsp<List<UserSuggest>> listPage(PageVO pageVO);
    int del(DelSuggestVO param);
}
