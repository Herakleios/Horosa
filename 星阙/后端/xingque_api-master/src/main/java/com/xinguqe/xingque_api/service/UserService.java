package com.xinguqe.xingque_api.service;

import com.xinguqe.xingque_api.dto.BO.WechatAccessTokenBO;
import com.xinguqe.xingque_api.dto.BO.WechatUserBO;
import com.xinguqe.xingque_api.dto.admin.response.PageDataRsp;
import com.xinguqe.xingque_api.dto.admin.request.PageVO;
import com.xinguqe.xingque_api.dto.request.*;
import com.xinguqe.xingque_api.entity.User;
import com.xinguqe.xingque_api.entity.UserConfig;
import com.xinguqe.xingque_api.exception.HorosaException;

import java.util.List;

public interface UserService {

//    void login();
    User login(UserLoginVO userLoginVO) throws HorosaException;
    User info(int userId);
    int modifyInfo(UserVO userVO, int userId);
    User AddOrUpdateUser(WechatAccessTokenBO accessToken, WechatUserBO wechatUser);

    UserConfig getConfig(int userId);

    int setConfig(UserConfigVO userConfigVO,int userId);
    int suggest(SuggestVO suggest, int userId);
    int addBehavior(UserBehaviorVO data, int userId);
    PageDataRsp<List<User>> listByAdd(PageVO pageVO);
    int register(UserRegisterVO userRegisterVO) throws HorosaException;
    int Del(UserDelVO userDelVO);
}
