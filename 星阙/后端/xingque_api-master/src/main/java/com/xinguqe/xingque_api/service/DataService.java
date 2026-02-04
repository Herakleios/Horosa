package com.xinguqe.xingque_api.service;

import com.xinguqe.xingque_api.dto.admin.request.DataTimeIntervalVO;
import com.xinguqe.xingque_api.entity.domain.UserBehaviorToolsCount;

import java.util.List;
import java.util.Map;

public interface DataService {
    List<UserBehaviorToolsCount> toolUse(DataTimeIntervalVO datetimeIntervalVO);
    Map<String, Long> appUser(DataTimeIntervalVO datetimeIntervalVO);
    Map<Integer,Double> userRegion(DataTimeIntervalVO datetimeIntervalVO);
}
