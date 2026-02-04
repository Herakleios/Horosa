package com.xinguqe.xingque_api.exception;

import com.xinguqe.xingque_api.dto.JsonResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.validation.BindException;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.Arrays;
import java.util.Map;

@Slf4j
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(HorosaException.class)
    public JsonResponse<Void> handleHorosaException(HorosaException ex){
        JsonResponse<Void> rsp = new JsonResponse<>();
        return rsp.fail(ex.getCode(),ex.getMessage());
    }

    @ExceptionHandler(BindException.class)
    public JsonResponse<String> bindException(BindException ex){
        BindingResult bindingResult = ex.getBindingResult();
        String errorMessage = "";
        for (FieldError fieldError : bindingResult.getFieldErrors()) {
            errorMessage = fieldError.getField() + fieldError.getDefaultMessage();
            break;
        }
        JsonResponse<String> rsp = new JsonResponse<>();
        return rsp.fail(10400,errorMessage);
    }

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public JsonResponse<String> bindException(MethodArgumentNotValidException ex){
        BindingResult eRes = ex.getBindingResult();
        String errorMessage = "";
        for (FieldError fieldError : eRes.getFieldErrors()) {
            errorMessage = fieldError.getField() + fieldError.getDefaultMessage();
            break;
        }
        JsonResponse<String> rsp = new JsonResponse<>();
        return rsp.fail(10400,errorMessage);
    }


    /**
     * 其他未知异常(拦截的是全局最底层异常,兜底)
     */
    @ExceptionHandler(value=Exception.class)
    public JsonResponse<Void> handleException(Exception ex) {
        JsonResponse<Void> rsp = new JsonResponse<>();
        log.error(ex.getMessage());
        StackTraceElement[] errs = ex.getStackTrace();
        for (StackTraceElement err : errs){
//            log.error(err.toString());
        }
        return rsp.fail(10500,"服务器错误，请稍后重试");
    }
}
