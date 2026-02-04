package com.xinguqe.xingque_api.controller.admin;

import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.admin.request.DelSuggestVO;
import com.xinguqe.xingque_api.dto.admin.response.PageDataRsp;
import com.xinguqe.xingque_api.dto.admin.request.PageVO;
import com.xinguqe.xingque_api.entity.UserSuggest;
import com.xinguqe.xingque_api.service.AdminSuggestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/admin/suggest")
public class AdminSuggestController {

    @Autowired
    private AdminSuggestService adminSuggestService;

    @PostMapping("/list")
    public JsonResponse<PageDataRsp<List<UserSuggest>>> list(@Validated @RequestBody PageVO pageVO) {
        PageDataRsp<List<UserSuggest>> res = adminSuggestService.listPage(pageVO);
        return new JsonResponse<PageDataRsp<List<UserSuggest>>>().success(res);
    }

    @PostMapping("/del")
    public JsonResponse<Integer> del(@Validated @RequestBody DelSuggestVO param) {
        int res = adminSuggestService.del(param);
        return new JsonResponse<Integer>().success(res);
    }
}
