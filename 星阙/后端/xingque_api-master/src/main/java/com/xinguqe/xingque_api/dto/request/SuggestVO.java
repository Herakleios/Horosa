package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import org.hibernate.validator.constraints.Length;

import javax.validation.constraints.NotEmpty;
import java.util.List;
@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)

public class SuggestVO {

    @NotEmpty
    @Length(max = 300)
    public String content;
    public String images;
}
