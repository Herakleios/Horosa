package com.xinguqe.xingque_api.controller.admin;

import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.admin.request.UserLoginVO;
import com.xinguqe.xingque_api.entity.User;
import com.xinguqe.xingque_api.service.AdminUserService;
import com.xinguqe.xingque_api.utils.jwt.JwtUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/admin/user")
public class AdminUserController {

    @Autowired
    private AdminUserService userService;

    @Autowired
    private JwtUtils jwtUtils;

    @PostMapping("/login")
    public JsonResponse<Object> login(@Validated @RequestBody UserLoginVO userLoginVO) {
        Boolean res = userService.login(userLoginVO);
        if (!res){
            return new JsonResponse<>().fail(10401,"用户名或密码错误");
        }
        User user = new User();
        user.setId(1);
        user.setName("horosaSuper");
        String token = jwtUtils.createToken(user);
        Map<String,String> rsp = new HashMap<>();
        rsp.put("token",token);
        return new JsonResponse<>().success(rsp);
    }
}
