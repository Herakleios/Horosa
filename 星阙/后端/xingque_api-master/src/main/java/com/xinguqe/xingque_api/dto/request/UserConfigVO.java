package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import org.hibernate.validator.constraints.Range;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserConfigVO {


     @NotNull
     @Range(min = 1,max = 2)
     public Integer apparentSolarTime;


     @NotNull
     @Range(min = 1,max = 2)
     public Integer qimenType;

     @NotNull
     @Range(min = 1,max = 2)
     public Integer liurenType;
}
