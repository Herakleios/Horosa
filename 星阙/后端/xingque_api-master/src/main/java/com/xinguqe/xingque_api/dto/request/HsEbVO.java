package com.xinguqe.xingque_api.dto.request;

import org.hibernate.validator.constraints.Length;

/**
 * 天干地支
 */
public class HsEbVO {

    @Length(min = 2,max = 2)
    public String year;

    @Length(min = 2,max = 2)
    public String month;

    @Length(min = 2,max = 2)
    public String day;

    @Length(min = 2,max = 2)
    public String hour;
}
