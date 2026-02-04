package com.xinguqe.xingque_api.config;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.Data;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Component;
import org.springframework.util.ClassUtils;

import java.io.*;
import java.lang.reflect.Type;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

@Data
@Configuration
//@Component
//@ConfigurationProperties(prefix = "sixlines")
public class SixLinesConfig {

    private Map<String,Map<String,Object>> gua = new HashMap<>();

    public SixLinesConfig() throws IOException {
        InputStream input =  ClassUtils.getDefaultClassLoader().getResourceAsStream("sixlines.json");
//        String path = this.getClass().getClassLoader().getResource("sixlines.json").getPath();
        assert input != null;
        InputStreamReader  isr = new InputStreamReader(input, StandardCharsets.UTF_8);
        BufferedReader bufferedReader = new BufferedReader(isr);
        String line;

        StringBuilder stringBuilder = new StringBuilder();
        while ((line = bufferedReader.readLine()) != null){
            stringBuilder.append(line);
        }
        bufferedReader.close();
        String json = stringBuilder.toString();

        ObjectMapper objectMapper = new ObjectMapper();

        this.gua = objectMapper.readValue(json, new TypeReference<Map<String, Map<String, Object>>>() {});
//        return config;
    }

}
