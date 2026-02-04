package com.xinguqe.xingque_api.dto.request;

import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@JsonNaming(PropertyNamingStrategies.SnakeCaseStrategy.class)
public class UserRegisterVO {

    @NotEmpty
    public String username;

    @NotEmpty
    public String password;

    @NotEmpty
    public String confirmPassword;
}


