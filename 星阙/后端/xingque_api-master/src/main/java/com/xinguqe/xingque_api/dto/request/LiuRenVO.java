package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class LiuRenVO {
    @NotEmpty
    public String inputKey;

    @NotNull
    public int isSave;

    public String Jieqi;

    public String month;

    public Integer guaType;

    @JsonProperty("gua_time")
    public DatetimeVO datetimeVO;

    public String address;

    public String question;

    public int hourNum = 0;

    public String country;

    public HsEbVO hseb;
}
