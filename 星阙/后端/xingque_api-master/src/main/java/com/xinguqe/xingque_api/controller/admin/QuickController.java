package com.xinguqe.xingque_api.controller.admin;

import com.xinguqe.xingque_api.dto.JsonResponse;
import com.xinguqe.xingque_api.dto.admin.request.QuickLinkVO;
import com.xinguqe.xingque_api.entity.QuickLink;
import com.xinguqe.xingque_api.service.QuickLinkService;
import com.xinguqe.xingque_api.service.TrigramService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/admin/quick_link")
public class QuickController {

    @Autowired
    private QuickLinkService quickLinkService;

    @PostMapping("/list")
    public JsonResponse<List<QuickLink>> list(){
        List<QuickLink> data =  quickLinkService.quickLinkList();
        return new JsonResponse<List<QuickLink>>().success(data);
    }

    @PostMapping("/modify")
    public JsonResponse<Void> modify(@Validated @RequestBody QuickLinkVO quickLinkVO){
        int res = quickLinkService.modify(quickLinkVO);
        return new JsonResponse<Void>().success();
    }
}
