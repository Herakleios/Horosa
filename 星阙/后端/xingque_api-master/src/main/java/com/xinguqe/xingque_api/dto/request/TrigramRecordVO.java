package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Null;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class TrigramRecordVO {

    @NotEmpty
    public String inputKey;

    @NotNull
    public int type;

    @NotNull
    public JsonNode input;

    @NotNull
    public JsonNode output;

    @NotNull
    public JsonNode extras;
}
