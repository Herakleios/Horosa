package com.xinguqe.xingque_api.service.impl;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.xinguqe.xingque_api.dto.BO.WechatAccessTokenBO;
import com.xinguqe.xingque_api.dto.BO.WechatUserBO;
import com.xinguqe.xingque_api.service.WechatService;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.Objects;

@Service
public class WechatServiceImpl implements WechatService {

    private static final String wechatApi = "https://api.weixin.qq.com/sns";
    private static final String wechatAppId = "wx8559b476b39e28d1";
    private static final String wechatAppSecret = "f6c847cb20558ac8dc1b7fc4397616cd";

    @Autowired
    private OkHttpClient okHttpClient;

    @Override
    public WechatAccessTokenBO getAccessToken(String code) throws JsonProcessingException {

        //refresh token 未过期则重新请求
//        String refreshToken = "";
//        String queryRefresh = String.format("appid=%s&grant_type=refresh_token&refresh_token=%s",wechatAppId,refreshToken);
//        JsonNode rspRefresh = reqWechatApi("/oauth2/refresh_token",queryRefresh);

        //refresh token如果过期则用refresh token 刷新
        //通过code请求微信接口 获取access token
        String query = String.format("appid=%s&secret=%s&code=%s&grant_type=authorization_code",wechatAppId,wechatAppSecret,code);
        String rsp = reqWechatApi("/oauth2/access_token",query);
        ObjectMapper objectMapper = new ObjectMapper();

        return objectMapper.readValue(rsp, WechatAccessTokenBO.class);
    }

    @Override
    public WechatUserBO getUserInfo(WechatAccessTokenBO accessToken) throws JsonProcessingException {
//        String openid = "";

        String query = String.format("access_token=%s&openid=%s",accessToken.accessToken,accessToken.openid);
        String rsp = reqWechatApi("/userinfo",query);
        ObjectMapper objectMapper = new ObjectMapper();

        return objectMapper.readValue(rsp, WechatUserBO.class);
    }

    private  String reqWechatApi(String router, String query) {
        String url = String.format("%s%s?%s",wechatApi,router,query);

        Request request = new Request.Builder().url(url).build();
        try (Response response = okHttpClient.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new IOException("Req wechat fail : Unexpected code " + response);
            }
            assert response.body() != null;
            //            ObjectMapper mapper = new ObjectMapper();
            return Objects.requireNonNull(response.body().string());
        }catch (IOException exception){
            throw new RuntimeException(exception);
        }
    }
}
