package com.xinguqe.xingque_api.dto.response;

import lombok.Data;

@Data
public class PageDataRsp<T> {
    private long total;
    private T data;
}
