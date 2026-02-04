package com.xinguqe.xingque_api.utils.http;

import okhttp3.OkHttpClient;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class HttpClientUtils {

    @Bean
    public OkHttpClient okHttpClient() {
        return new OkHttpClient();
    }
}
