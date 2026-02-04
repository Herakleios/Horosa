package com.xinguqe.xingque_api.service.impl;

import com.xinguqe.xingque_api.dto.admin.request.DataTimeIntervalVO;
import com.xinguqe.xingque_api.entity.UserBehaviorExample;
import com.xinguqe.xingque_api.entity.UserExample;
import com.xinguqe.xingque_api.entity.domain.UserBehaviorToolsCount;
import com.xinguqe.xingque_api.entity.domain.UserRegionStatistics;
import com.xinguqe.xingque_api.mapper.UserBehaviorMapper;
import com.xinguqe.xingque_api.mapper.UserMapper;
import com.xinguqe.xingque_api.service.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.text.DecimalFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class DataServiceImpl implements DataService {

    @Autowired
    private UserBehaviorMapper userBehaviorMapper;

    @Autowired
    private UserMapper userMapper;

    public List<UserBehaviorToolsCount> toolUse(DataTimeIntervalVO datetimeIntervalVO) {
        UserBehaviorExample userBehaviorExample = new UserBehaviorExample();
        UserBehaviorExample.Criteria criteria = userBehaviorExample.createCriteria();
        criteria.andModuleEqualTo("trigram");
        criteria.andCreateTimeBetween(datetimeIntervalVO.startTime, datetimeIntervalVO.endTime);

        return userBehaviorMapper.selectToolsCountByExample(userBehaviorExample);
    }

    public Map<String, Long> appUser(DataTimeIntervalVO datetimeIntervalVO) {
        UserBehaviorExample userBehaviorExample = new UserBehaviorExample();
        UserBehaviorExample.Criteria criteria = userBehaviorExample.createCriteria();
        criteria.andModuleEqualTo("app").andOperateEqualTo("open").andCreateTimeBetween(datetimeIntervalVO.startTime, datetimeIntervalVO.endTime);
        long open = userBehaviorMapper.countByExample(userBehaviorExample);

        criteria.andUserIdNotEqualTo(0);
        long openUser = userBehaviorMapper.countByExample(userBehaviorExample);

        UserExample userExample = new UserExample();
        UserExample.Criteria criteria2 = userExample.createCriteria();
        criteria2.andStatusEqualTo(1);
        long users = userMapper.countByExample(userExample);

        criteria2.andCreateTimeBetween(datetimeIntervalVO.startTime, datetimeIntervalVO.endTime);
        long addUser = userMapper.countByExample(userExample);

        Map<String, Long> data = new HashMap<String, Long>();
        data.put("open", open);
        data.put("users", users);
        data.put("addUser", addUser);
        data.put("openUser", openUser);

        return data;
    }

    public Map<Integer,Double> userRegion(DataTimeIntervalVO datetimeIntervalVO) {
        UserExample userExample = new UserExample();
        UserExample.Criteria criteria = userExample.createCriteria();
        criteria.andStatusEqualTo(1).andCreateTimeBetween(datetimeIntervalVO.startTime, datetimeIntervalVO.endTime);

        long count = userMapper.countByExample(userExample);

        criteria.andResidenceProvinceIdNotEqualTo(0);

        List<UserRegionStatistics> userRegion = userMapper.selectRegionCountByExample(userExample);


        Map<Integer,Double> res = new HashMap<>();
        for (UserRegionStatistics s : userRegion) {
            double rate = ((double) s.getCount() / count) * 100;

            rate = Math.round(rate * 100) / 100.00;
            res.put(s.getProvinceId(), rate);
        }

        return res;
    }
}
