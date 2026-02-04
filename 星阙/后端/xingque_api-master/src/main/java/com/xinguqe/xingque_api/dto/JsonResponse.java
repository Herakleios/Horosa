package com.xinguqe.xingque_api.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class JsonResponse<T> {
    private Integer code;

    private String msg;

    private T data;

    public JsonResponse<Void> fail(){
        return new JsonResponse<>(500, "操作失败,请稍后重试", null);
    }

    public JsonResponse<T> fail(String msg){
        return new JsonResponse<>(500, msg, null);
    }

    public JsonResponse<T> fail(Integer code){
        return new JsonResponse<>(code, "操作失败,请稍后重试", null);
    }

    public JsonResponse<T> fail(Integer code,String msg){
        return new JsonResponse<>(code, msg, null);
    }

    public JsonResponse<T> success(){
        return new JsonResponse<T>(0,"success",null);
    }

    public JsonResponse<T> success(T data){
        return new JsonResponse<>(0, "success", data);
    }
}
