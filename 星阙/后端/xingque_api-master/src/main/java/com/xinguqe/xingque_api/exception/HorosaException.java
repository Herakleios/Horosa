package com.xinguqe.xingque_api.exception;


import lombok.Data;

@Data
public class HorosaException extends Exception {
    private int code;
    private String message;

    public HorosaException(int code){
        this.code = code;
    }

    public HorosaException(int code,String msg){
        this.code = code;
        this.message = msg;
    }
}
