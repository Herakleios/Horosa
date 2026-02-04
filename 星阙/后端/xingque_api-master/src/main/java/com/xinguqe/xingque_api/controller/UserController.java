package com.xinguqe.xingque_api.controller;


import com.fasterxml.jackson.core.JsonProcessingException;
import com.xinguqe.xingque_api.dto.BO.WechatAccessTokenBO;
import com.xinguqe.xingque_api.dto.BO.WechatUserBO;
import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.request.*;
import com.xinguqe.xingque_api.entity.User;
import com.xinguqe.xingque_api.entity.UserConfig;
import com.xinguqe.xingque_api.exception.HorosaException;
import com.xinguqe.xingque_api.service.UserService;
import com.xinguqe.xingque_api.service.WechatService;
import com.xinguqe.xingque_api.utils.jwt.JwtUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/user")
public class UserController extends BasicController {

    @Autowired
    private UserService userService;

    @Autowired
    private WechatService wechatService;

    @Autowired
    private JwtUtils jwtUtils;

    @PostMapping("/login/wechat")
    public JsonResponse<Map<String,String>> LoginWechat(@RequestBody LoginWechatVO code) throws JsonProcessingException {
        WechatAccessTokenBO accessToken = wechatService.getAccessToken(code.code);
        WechatUserBO wechatUser = wechatService.getUserInfo(accessToken);

        User user = userService.AddOrUpdateUser(accessToken,wechatUser);
        String token = jwtUtils.createToken(user);

        Map<String,String> res = new HashMap<>();
        res.put("token",token);

        JsonResponse<Map<String,String>> rsp = new JsonResponse<>();
        return rsp.success(res);
    }

    @PostMapping("/info")
    public JsonResponse<User> info(HttpServletRequest request) {
        //userid
        int userId = (int) request.getAttribute("userId");
        User u = userService.info(userId);
        u.setWxOpenid("");
        u.setWxUnionid("");
        return new JsonResponse<User>().success(u);
    }

    @PostMapping("/modify")
    public JsonResponse<Void> modifyInfo(HttpServletRequest request, @Validated @RequestBody UserVO userVO) {
        //userid
        int userId = (int) request.getAttribute("userId");
        int r = userService.modifyInfo(userVO,userId);
        return new JsonResponse<Void>().success();
    }

    @PostMapping("/config/set")
    public JsonResponse<Void> setConfig(HttpServletRequest request, @Validated @RequestBody UserConfigVO param) {
        int userId = (int) request.getAttribute("userId");
        int id = userService.setConfig(param, userId);
        if (id > 0) {
            return new JsonResponse<Void>().success();
        }
        return new JsonResponse<Void>().fail("设置失败");
    }

    @PostMapping("/config/get")
    public JsonResponse<UserConfig> getConfig(HttpServletRequest request) {
        int userId = (int) request.getAttribute("userId");
        UserConfig data = userService.getConfig(userId);
        JsonResponse<UserConfig> rsp = new JsonResponse<>();
        return rsp.success(data);
    }

    @PostMapping("/suggest")
    public JsonResponse<Void> suggest(HttpServletRequest request, @Validated @RequestBody SuggestVO suggestVO){
        int userId = (int) request.getAttribute("userId");
        int res = userService.suggest(suggestVO,userId);
        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }

    @PostMapping("/behavior")
    public JsonResponse<Void> behavior(HttpServletRequest request, @Validated @RequestBody UserBehaviorVO data){
        int userId = (int) request.getAttribute("userId");
        int res = userService.addBehavior(data,userId);
        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }

    @PostMapping("/register")
    public JsonResponse<Void> register(HttpServletRequest request, @Validated @RequestBody UserRegisterVO userVO) throws HorosaException {
        if (!userVO.password.equals(userVO.confirmPassword)){
            return new JsonResponse<Void>().fail(1001,"两次密码输入不一致");
        }

        userService.register(userVO);
        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }

    @PostMapping("/login")
    public JsonResponse<Map<String,String>> login(HttpServletRequest request, @Validated @RequestBody UserLoginVO userVO) throws HorosaException {

        User user = userService.login(userVO);

        String token = jwtUtils.createToken(user);

        Map<String,String> res = new HashMap<>();
        res.put("token",token);

        JsonResponse<Map<String,String>> rsp = new JsonResponse<>();
        return rsp.success(res);
    }

    @PostMapping("/cancel_user")
    public JsonResponse<Void> Del(HttpServletRequest request,@Validated @RequestBody UserDelVO userDelVO) throws HorosaException {
        userDelVO.userId= (int) request.getAttribute("userId");
        userService.Del(userDelVO);
        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }

}
