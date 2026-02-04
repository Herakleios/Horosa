package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.Range;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserVO {
    public String avatar;

    @NotEmpty
    @Length(min = 2,max = 20)
    public String name;

    @NotNull
    @Range(max = 2,min = 1)
    public Integer sex;
    public String birthday;


    @NotNull
    public Integer residenceProvinceId;

    @NotNull
    @JsonProperty("residence_city_id")
    public Integer residenceCityId;

//    @NotEmpty
    @NotNull
    public Integer residenceDistrictId;

//    @NotEmpty
    @NotNull
    public Integer birthProvinceId;

//    @NotEmpty
    @NotNull
    public Integer birthCityId;

//    @NotEmpty
    @NotNull
    public Integer birthDistrictId;
}
