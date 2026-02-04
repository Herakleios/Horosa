package com.xinguqe.xingque_api.interceptor;

import com.auth0.jwt.interfaces.Claim;
import com.xinguqe.xingque_api.exception.HorosaException;
import com.xinguqe.xingque_api.utils.jwt.JwtUtils;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

@Slf4j
@Component
public class LoginInterceptor implements HandlerInterceptor {

    @Autowired
    private JwtUtils jwtUtils;

    private static final String[] ALLOW_URI = new String[]{"/trigram/sixline","/trigram/qimen","/trigram/liuren","/user/register","/user/login"};

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
//        request.setAttribute("userId", 1);

        String uri = request.getRequestURI();

        String token = request.getHeader("Authorization");
        log.error(token);
        if (token == null || token.isEmpty()) {
            if (Arrays.asList(ALLOW_URI).contains(uri)) {
                request.setAttribute("userId", 0);
                return true;
            }else {
                throw new HorosaException(10401, "token验证失败");
            }
        }
        Map<String, Claim> claims = jwtUtils.verifyToken(token);

//        request.setAttribute("userId", claims.get("id").asInt());
        request.setAttribute("userId",  claims.get("id").asInt());

        return true;
    }
}
