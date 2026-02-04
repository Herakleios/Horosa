package com.xinguqe.xingque_api.dto.BO;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class WechatAccessTokenBO {
    public String accessToken;
    public Integer expiresIn;

    public String refreshToken;
    public String openid;

    public String scope;

    public String unionid;
}
