package com.xinguqe.xingque_api.controller;

import com.github.pagehelper.Page;
import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.request.PageVO;
import com.xinguqe.xingque_api.dto.request.TrigramBookVO;
import com.xinguqe.xingque_api.dto.response.PageDataRsp;
import com.xinguqe.xingque_api.entity.UserTrigramBook;
import com.xinguqe.xingque_api.exception.HorosaException;
import com.xinguqe.xingque_api.service.TrigramBookService;
import org.apache.ibatis.annotations.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/trigram_book")
@Validated
public class TrigramBookController {

    @Autowired
    private TrigramBookService trigramBookService;

    @PostMapping("/list")
    public JsonResponse<PageDataRsp<List<UserTrigramBook>>> listPage(HttpServletRequest request, @Validated @RequestBody PageVO pageVO){
        int userId = (int) request.getAttribute("userId");
        PageDataRsp<List<UserTrigramBook>> res = trigramBookService.listPage(pageVO,userId);
        JsonResponse<PageDataRsp<List<UserTrigramBook>>> rsp = new JsonResponse<>();
        return rsp.success(res);
    }

    @PostMapping("/add")
    public JsonResponse<Map<String,Integer>> add(HttpServletRequest request, @Validated @RequestBody TrigramBookVO trigramBookVO) throws HorosaException {
        int userId = (int) request.getAttribute("userId");
        int id = trigramBookService.add(trigramBookVO,userId);
        
        JsonResponse<Map<String,Integer>> rsp = new JsonResponse<>();

        Map<String,Integer> res = new HashMap<String,Integer>(){{ put("id",id); }};

        return rsp.success(res);
    }

    @PostMapping("/modify")
    public JsonResponse<Void> modify(HttpServletRequest request, @Validated @RequestBody TrigramBookVO trigramBookVO){
        int userId = (int) request.getAttribute("userId");
        trigramBookService.modify(trigramBookVO,userId);

        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }

    @PostMapping("/del")
    public JsonResponse<Void> modify(HttpServletRequest request, @RequestParam("id") int id){
        int userId = (int) request.getAttribute("userId");
        trigramBookService.del(id,userId);

        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.success();
    }
}
