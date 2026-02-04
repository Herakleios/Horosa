package com.xinguqe.xingque_api.entity.domain;

import lombok.Data;

@Data
public class UserBehaviorToolsCount {
    private String module;
    private String operate;
    private long count;
}
