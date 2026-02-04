package com.xinguqe.xingque_api.controller.admin;

import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.admin.request.DataTimeIntervalVO;
import com.xinguqe.xingque_api.entity.domain.UserBehaviorToolsCount;
import com.xinguqe.xingque_api.service.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/admin/data")
public class DataController {

    @Autowired
    private DataService dataService;

    @PostMapping("/tools_use")
    public JsonResponse<Map<String,UserBehaviorToolsCount>> toolsUse(@Validated @RequestBody DataTimeIntervalVO data){
        List<UserBehaviorToolsCount> res =  dataService.toolUse(data);

        Map<String,UserBehaviorToolsCount> rsp = new HashMap<>();
        for (UserBehaviorToolsCount u : res) {
            String k = u.getModule() + "-" + u.getOperate();
            rsp.put(k,u);
        }
        return new JsonResponse<Map<String,UserBehaviorToolsCount>>().success(rsp);
    }

    @PostMapping("/app_user")
    public JsonResponse<Map<String, Long>> appUser(@Validated @RequestBody DataTimeIntervalVO data){
        Map<String, Long> res =  dataService.appUser(data);
        return new JsonResponse<Map<String, Long>>().success(res);
    }

    @PostMapping("/user_region")
    public JsonResponse<Map<Integer,Double>> userRegion(@Validated @RequestBody DataTimeIntervalVO data){
        Map<Integer,Double> res =  dataService.userRegion(data);
        return new JsonResponse<Map<Integer,Double>>().success(res);
    }
}
