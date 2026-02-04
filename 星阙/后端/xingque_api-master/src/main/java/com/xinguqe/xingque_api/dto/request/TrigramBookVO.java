package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class TrigramBookVO {
    public int id;
    public String name;
    public Integer sex;
    public String birthday;

    public Integer residenceProvinceId;
    public Integer residenceCityId;
    public Integer residenceDistrictId;

    public Integer birthProvinceId;
    public Integer birthCityId;
    public Integer birthDistrictId;

    public String relation;
}
