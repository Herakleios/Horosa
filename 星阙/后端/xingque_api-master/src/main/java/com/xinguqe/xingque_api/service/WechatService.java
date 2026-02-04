package com.xinguqe.xingque_api.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.xinguqe.xingque_api.dto.BO.WechatAccessTokenBO;
import com.xinguqe.xingque_api.dto.BO.WechatUserBO;

public interface WechatService {
    public WechatAccessTokenBO getAccessToken(String code) throws JsonProcessingException;

    public WechatUserBO getUserInfo(WechatAccessTokenBO accessToken) throws JsonProcessingException;
}
