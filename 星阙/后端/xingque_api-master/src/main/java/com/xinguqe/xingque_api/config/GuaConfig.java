package com.xinguqe.xingque_api.config;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.Data;
import org.springframework.context.annotation.Configuration;
import org.springframework.util.ClassUtils;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

@Data
@Configuration
//@Component
//@ConfigurationProperties(prefix = "sixlines")
public class GuaConfig {

    private Map<String,Map<String, JsonNode>> gua = new HashMap<>();

    public GuaConfig() throws IOException {
        InputStream input =  ClassUtils.getDefaultClassLoader().getResourceAsStream("gua.json");
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

        this.gua = objectMapper.readValue(json, new TypeReference<Map<String, Map<String, JsonNode>>>() {});
//        return config;
    }

}
