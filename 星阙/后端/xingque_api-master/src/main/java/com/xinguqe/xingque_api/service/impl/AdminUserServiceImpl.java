package com.xinguqe.xingque_api.service.impl;

import com.xinguqe.xingque_api.dto.admin.request.UserLoginVO;
import com.xinguqe.xingque_api.service.AdminUserService;
import org.springframework.stereotype.Service;

@Service
public class AdminUserServiceImpl implements AdminUserService {

    public Boolean login(UserLoginVO userLoginVO){
        return userLoginVO.username.equals("horosaSuper") && userLoginVO.password.equals("H05-50j.126-@t0");
    }

}
