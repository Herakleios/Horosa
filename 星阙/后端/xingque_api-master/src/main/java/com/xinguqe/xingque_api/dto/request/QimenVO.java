package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class QimenVO {

    @NotEmpty
    public String inputKey;

    @NotNull
    public int isSave;

    public Integer guaType;

    @JsonProperty("gua_time")
    public DatetimeVO datetimeVO;

    public String address;

    public String question;

    public String country;
}
