package com.xinguqe.xingque_api.config;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Configuration;
import org.springframework.util.ClassUtils;

import java.io.*;
import java.nio.Buffer;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

@Slf4j
@Data
@Configuration
//@Component
//@ConfigurationProperties(prefix = "sixlines")
public class QimenConfig {

    private Map<String,Map<String,Object>> gua;

    public QimenConfig() throws IOException {
        InputStream input =  ClassUtils.getDefaultClassLoader().getResourceAsStream("qimen.json");
//        String path = this.getClass().getClassLoader().getResource("qimen.json").getPath();
        assert input != null;
        InputStreamReader  isr = new InputStreamReader(input, StandardCharsets.UTF_8);
        String line;

        BufferedReader bufferedReader = new BufferedReader(isr);

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
