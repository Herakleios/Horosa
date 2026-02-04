package com.xinguqe.xingque_api.service.impl;

import com.github.pagehelper.PageHelper;
import com.xinguqe.xingque_api.dto.admin.request.DelSuggestVO;
import com.xinguqe.xingque_api.dto.admin.response.PageDataRsp;
import com.xinguqe.xingque_api.dto.admin.request.PageVO;
import com.xinguqe.xingque_api.entity.UserSuggest;
import com.xinguqe.xingque_api.entity.UserSuggestExample;
import com.xinguqe.xingque_api.mapper.UserSuggestMapper;
import com.xinguqe.xingque_api.service.AdminSuggestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AdminSuggestServiceImpl implements AdminSuggestService {

    @Autowired
    private UserSuggestMapper userSuggestMapper;

    public PageDataRsp<List<UserSuggest>> listPage(PageVO pageVO) {

        UserSuggestExample example = new UserSuggestExample();
        UserSuggestExample.Criteria criteria = example.createCriteria();
        criteria.andStatusEqualTo(1);
        example.setOrderByClause("id desc");

        long count = userSuggestMapper.countByExample(example);

        PageHelper.startPage(pageVO.page,pageVO.pageSize);
        List<UserSuggest> list = userSuggestMapper.selectByExample(example);

        PageDataRsp<List<UserSuggest>> pageDataRsp = new PageDataRsp<>();
        pageDataRsp.setData(list);
        pageDataRsp.setTotal(count);

        return pageDataRsp;
    }

    public int del(DelSuggestVO param){
        UserSuggestExample example = new UserSuggestExample();
        UserSuggestExample.Criteria criteria = example.createCriteria();

        return userSuggestMapper.deleteByPrimaryKey(param.id);
    }
}
