package com.xinguqe.xingque_api.controller;

import com.xinguqe.xingque_api.dto.JsonResponse;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/wechat")
public class WechatController {

    @PostMapping("/access_token")
    public JsonResponse getAccessToken(@RequestBody String code)
    {
        //通过code请求微信接口 获取access token

        return new JsonResponse().success();
    }
}
