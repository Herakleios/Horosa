package com.xinguqe.xingque_api.dto.request;


import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import org.hibernate.validator.constraints.Length;
import org.hibernate.validator.constraints.Range;
import org.springframework.validation.annotation.Validated;

import javax.validation.Valid;
import javax.validation.constraints.Digits;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

//@Validated
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class SixLineVO {

//    @NotNull(message = "不能为空")
//    @NotEmpty(message = "不能为空")
    @Range(min = 1, max = 3)
    public Integer guaType;

    @Length(max = 6)
    public String lines;

    @JsonProperty("gua_time")
    public DatetimeVO datetimeVO;

    @NotEmpty
    public String inputKey;

    @NotNull
    public String jieqi;

    @NotNull
    public int isSave;

    public String address;

    public String question;

    public String country;

    public HsEbVO hseb;
}
