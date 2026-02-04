package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

import javax.validation.constraints.NotEmpty;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserBehaviorVO {

    @NotEmpty
    public String module;

    @NotEmpty
    public String operate;
}
