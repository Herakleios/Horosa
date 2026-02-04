package com.xinguqe.xingque_api.service.impl;

import com.github.pagehelper.PageHelper;
import com.xinguqe.xingque_api.dto.request.PageVO;
import com.xinguqe.xingque_api.dto.request.TrigramBookVO;
import com.xinguqe.xingque_api.dto.response.PageDataRsp;
import com.xinguqe.xingque_api.entity.UserTrigramBook;
import com.xinguqe.xingque_api.entity.UserTrigramBookExample;
import com.xinguqe.xingque_api.exception.HorosaException;
import com.xinguqe.xingque_api.mapper.UserTrigramBookMapper;
import com.xinguqe.xingque_api.service.TrigramBookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TrigramBookServiceImpl implements TrigramBookService {

    @Autowired
    private UserTrigramBookMapper userTrigramBookMapper;

    public PageDataRsp<List<UserTrigramBook>> listPage(PageVO pageVO,int userId) {
        UserTrigramBookExample userTrigramBookExample = new UserTrigramBookExample();
        UserTrigramBookExample.Criteria criteria = userTrigramBookExample.createCriteria();
        criteria.andUserIdEqualTo(userId);
        long count = userTrigramBookMapper.countByExample(userTrigramBookExample);
        PageHelper.startPage(pageVO.page, pageVO.pageSize);

        userTrigramBookExample.setOrderByClause("modified_time desc");

        List<UserTrigramBook> books = userTrigramBookMapper.selectByExample(userTrigramBookExample);

        PageDataRsp<List<UserTrigramBook>> data = new PageDataRsp<>();
        data.setData(books);
        data.setTotal(count);

        return data;
    }

    public int add(TrigramBookVO trigramBookVO, int userId) throws HorosaException {
        //查询是否超过30个
        UserTrigramBookExample userTrigramBookExample = new UserTrigramBookExample();
        UserTrigramBookExample.Criteria criteria = userTrigramBookExample.createCriteria();
        criteria.andUserIdEqualTo(userId).andStatusEqualTo(1);

        long count = userTrigramBookMapper.countByExample(userTrigramBookExample);
        if (count >= 30) {
            //大于 30 抛出异常
            throw new HorosaException(10405, "数据超过已达上限，请删除其他数据重新添加");
        }


        UserTrigramBook userTrigramBook = new UserTrigramBook();
        userTrigramBook.setUserId(userId);
        userTrigramBook.setName(trigramBookVO.name);
        userTrigramBook.setSex(trigramBookVO.sex);
        userTrigramBook.setBirthday(trigramBookVO.birthday);
        userTrigramBook.setResidenceProvinceId(trigramBookVO.residenceProvinceId);
        userTrigramBook.setResidenceCityId(trigramBookVO.residenceCityId);
        userTrigramBook.setResidenceDistrictId(trigramBookVO.residenceDistrictId);
        userTrigramBook.setBirthProvinceId(trigramBookVO.birthProvinceId);
        userTrigramBook.setBirthCityId(trigramBookVO.birthCityId);
        userTrigramBook.setBirthDistrictId(trigramBookVO.birthDistrictId);
        userTrigramBook.setRelation(trigramBookVO.relation);

        userTrigramBookMapper.insertSelective(userTrigramBook);
        return userTrigramBook.getId();
    }

    public int modify(TrigramBookVO trigramBookVO, int userId) {
        UserTrigramBook userTrigramBook = new UserTrigramBook();
        userTrigramBook.setId(trigramBookVO.id);
        userTrigramBook.setName(trigramBookVO.name);
        userTrigramBook.setSex(trigramBookVO.sex);
        userTrigramBook.setBirthday(trigramBookVO.birthday);
        userTrigramBook.setResidenceProvinceId(trigramBookVO.residenceProvinceId);
        userTrigramBook.setResidenceCityId(trigramBookVO.residenceCityId);
        userTrigramBook.setResidenceDistrictId(trigramBookVO.residenceDistrictId);
        userTrigramBook.setBirthProvinceId(trigramBookVO.birthProvinceId);
        userTrigramBook.setBirthCityId(trigramBookVO.birthCityId);
        userTrigramBook.setBirthDistrictId(trigramBookVO.birthDistrictId);
        userTrigramBook.setRelation(trigramBookVO.relation);

        return userTrigramBookMapper.updateByPrimaryKeySelective(userTrigramBook);
    }

    public int del(int id,int userId){
        UserTrigramBookExample userTrigramBookExample = new UserTrigramBookExample();
        UserTrigramBookExample.Criteria criteria = userTrigramBookExample.createCriteria();
        criteria.andUserIdEqualTo(userId).andIdEqualTo(id);

        return userTrigramBookMapper.deleteByExample(userTrigramBookExample);
    }
}
