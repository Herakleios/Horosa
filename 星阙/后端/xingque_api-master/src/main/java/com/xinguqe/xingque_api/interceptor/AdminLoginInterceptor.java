package com.xinguqe.xingque_api.interceptor;

import com.auth0.jwt.interfaces.Claim;
import com.xinguqe.xingque_api.exception.HorosaException;
import com.xinguqe.xingque_api.utils.jwt.JwtUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Map;

@Component
public class AdminLoginInterceptor implements HandlerInterceptor {

    @Autowired
    private JwtUtils jwtUtils;

//    private static final String[] ALLOW_URI = new String[]{"login"};

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
//        request.setAttribute("adminUserId", 1);

        String token = request.getHeader("Authorization");
        if (token == null || token.isEmpty()) {
            throw new HorosaException(10401, "token验证失败");
        }
        Map<String, Claim> claims = jwtUtils.verifyToken(token);

        request.setAttribute("adminUserId", claims.get("id").asInt());

        return true;
    }
}
