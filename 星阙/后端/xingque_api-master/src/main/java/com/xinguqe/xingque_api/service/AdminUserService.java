package com.xinguqe.xingque_api.service;

import com.xinguqe.xingque_api.dto.admin.request.UserLoginVO;

public interface AdminUserService {
    Boolean login(UserLoginVO userLoginVO);
}
