package com.xinguqe.xingque_api.controller.admin;

import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.admin.response.PageDataRsp;
import com.xinguqe.xingque_api.dto.admin.request.PageVO;
import com.xinguqe.xingque_api.entity.User;
import com.xinguqe.xingque_api.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/admin/consumer")
public class AdminConsumerController {

    @Autowired
    private UserService userService;

    @PostMapping("/list")
    public JsonResponse<PageDataRsp<List<User>>> list(@Validated @RequestBody PageVO pageVO) {
        PageDataRsp<List<User>> res = userService.listByAdd(pageVO);
        return new JsonResponse<PageDataRsp<List<User>>>().success(res);
    }

}
