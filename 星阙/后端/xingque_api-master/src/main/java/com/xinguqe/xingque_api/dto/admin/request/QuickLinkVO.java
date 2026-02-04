package com.xinguqe.xingque_api.dto.admin.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

import javax.validation.constraints.Max;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class QuickLinkVO {
    @NotNull
    public Integer id;

    @NotEmpty
    public String name;

    @NotEmpty
    public String logo;

    @NotNull
    @Max(10)
    public Integer sort;
}
