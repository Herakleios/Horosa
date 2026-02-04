package com.xinguqe.xingque_api.service.impl;

import com.xinguqe.xingque_api.dto.admin.request.QuickLinkVO;
import com.xinguqe.xingque_api.entity.QuickLink;
import com.xinguqe.xingque_api.entity.QuickLinkExample;
import com.xinguqe.xingque_api.mapper.QuickLinkMapper;
import com.xinguqe.xingque_api.service.QuickLinkService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class QuickLinkServiceImpl implements QuickLinkService {

    @Autowired
    private QuickLinkMapper quickLinkMapper;

    public List<QuickLink> quickLinkList(){
        QuickLinkExample quickLinkExample = new QuickLinkExample();
        QuickLinkExample.Criteria criteria = quickLinkExample.createCriteria();
        criteria.andStatusEqualTo(1);

        return quickLinkMapper.selectByExampleWithBLOBs(quickLinkExample);
    }

    public int modify(QuickLinkVO quickLinkVO){
        QuickLink quickLink = new QuickLink();
        quickLink.setName(quickLinkVO.name);
        quickLink.setLogo(quickLinkVO.logo);
        quickLink.setSort(quickLinkVO.sort);
        quickLink.setId(quickLinkVO.id);

        return quickLinkMapper.updateByPrimaryKeySelective(quickLink);
    }
}
