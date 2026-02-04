package com.xinguqe.xingque_api.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.request.*;
import com.xinguqe.xingque_api.dto.response.PageDataRsp;
import com.xinguqe.xingque_api.entity.QuickLink;
import com.xinguqe.xingque_api.entity.UserTrigramRecordWithBLOBs;
import com.xinguqe.xingque_api.service.QuickLinkService;
import com.xinguqe.xingque_api.service.TrigramService;
import com.xinguqe.xingque_api.service.UserService;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/trigram")
@Validated
public class TrigramController extends BasicController {

//    @Autowired
    private final TrigramService trigramService;
    private final UserService userService;
    private final QuickLinkService quickLinkService;

    public TrigramController(TrigramService trigramService,UserService userService,QuickLinkService quickLinkService) {
        this.trigramService = trigramService;
        this.userService = userService;
        this.quickLinkService = quickLinkService;
    }


    @PostMapping("/sixline")
    public JsonResponse<Map<String, Object>> sixLine(HttpServletRequest request, @Validated @RequestBody SixLineVO param) throws Exception {
        Map<String, Object> res = trigramService.reqSixLine(param);

        JsonResponse<Map<String, Object>> rsp = new JsonResponse<>();
        //写入mysql
        int userId = (int) request.getAttribute("userId");
        if(param.isSave != 2 && userId != 0){
            int id = trigramService.addRecord(userId, param.inputKey,2, param, res, new HashMap<>(),1);
            res.put("record_id", id);
        }
        UserBehaviorVO userBehaviorVO = new UserBehaviorVO();
        userBehaviorVO.module = "trigram";
        userBehaviorVO.operate = "liuyao";
        userService.addBehavior(userBehaviorVO,userId);
        return rsp.success(res);
    }

    @PostMapping("/liuren")
    public JsonResponse<Map<String, Object>> liuren(HttpServletRequest request, @RequestBody LiuRenVO param) throws Exception {
        Map<String, Object> res = trigramService.reqLiuRen(param);

        JsonResponse<Map<String, Object>> rsp = new JsonResponse<>();
        //写入mysql
        int userId = (int) request.getAttribute("userId");
        if (param.isSave != 2 && userId != 0){
            int id = trigramService.addRecord(userId, param.inputKey,3, param, res, new HashMap<>(),1);
            res.put("record_id", id);
        }
        UserBehaviorVO userBehaviorVO = new UserBehaviorVO();
        userBehaviorVO.module = "trigram";
        userBehaviorVO.operate = "liuren";
        userService.addBehavior(userBehaviorVO,userId);
        return rsp.success(res);
    }

    @PostMapping("/qimen")
    public JsonResponse<Map<String, Object>> qimen(HttpServletRequest request, @RequestBody QimenVO param) throws Exception {
        Map<String, Object> res = trigramService.reqQimen(param);

        JsonResponse<Map<String, Object>> rsp = new JsonResponse<>();
        //写入mysql
        int userId = (int) request.getAttribute("userId");

        if (param.isSave != 2 && userId != 0){
            int id = trigramService.addRecord(userId, param.inputKey,4, param, res, new HashMap<>(),1);
            res.put("record_id", id);
        }

        UserBehaviorVO userBehaviorVO = new UserBehaviorVO();
        userBehaviorVO.module = "trigram";
        userBehaviorVO.operate = "qimen";
        userService.addBehavior(userBehaviorVO,userId);
        return rsp.success(res);
    }

    @PostMapping("/add_record")
    public JsonResponse<Void> addRecord(HttpServletRequest request, @Validated @RequestBody TrigramRecordVO data) throws JsonProcessingException {
        int userId = (int) request.getAttribute("userId");
        if (userId != 0){
            trigramService.addRecord(userId, data.inputKey,data.type, data.input, data.output, data.extras,2);
        }
        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }

    @PostMapping("/del_record")
    public JsonResponse<Void> delRecord(HttpServletRequest request, @Validated @RequestBody Map<String,Integer> param) {
        int userId = (int) request.getAttribute("userId");
        trigramService.delRecord(userId, param.get("id"));
        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }

    @PostMapping("/record_list")
    public JsonResponse<PageDataRsp<List<UserTrigramRecordWithBLOBs>>> recordList(HttpServletRequest request, @Validated @RequestBody PageVO pageVO) {
        int userId = (int) request.getAttribute("userId");
        PageDataRsp<List<UserTrigramRecordWithBLOBs>> res = trigramService.recordList(pageVO, userId);

        JsonResponse<PageDataRsp<List<UserTrigramRecordWithBLOBs>>> rsp = new JsonResponse<>();
        return rsp.success(res);
    }

    @PostMapping("/quick_link")
    public JsonResponse<List<QuickLink>> quickLink(){
        List<QuickLink> data =  quickLinkService.quickLinkList();
        return new JsonResponse<List<QuickLink>>().success(data);
    }

}
