package com.xinguqe.xingque_api.config;

import com.xinguqe.xingque_api.service.TrigramService;
import com.xinguqe.xingque_api.service.impl.TrigramServiceImpl;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.Formatter;

@Configuration
public class TrigramServiceConfig {

    @Value("${trigram-service.protocol}")
    public String protocol;

    @Value("${trigram-service.host}")
    public String host;

    @Value("${trigram-service.port}")
    public String port;


//    @Bean
//    public TrigramService trigramService() {
//        return new TrigramServiceImpl();
//    }

    public String getUrl(String api){
        Formatter formatter = new Formatter();
        return formatter.format("%s://%s:%s/%s",protocol,host,port,api).toString();
    }
}
