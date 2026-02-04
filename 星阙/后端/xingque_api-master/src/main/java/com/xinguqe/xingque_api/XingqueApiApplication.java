package com.xinguqe.xingque_api;

import org.mybatis.generator.api.MyBatisGenerator;
import org.mybatis.generator.config.Configuration;
import org.mybatis.generator.config.xml.ConfigurationParser;
import org.mybatis.generator.internal.DefaultShellCallback;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
@MapperScan("com.xinguqe.xingque_api.mapper")
public class XingqueApiApplication  {

    public static void main(String[] args) {
        SpringApplication.run(XingqueApiApplication.class, args);
    }

//    @Override
//    public void run(ApplicationArguments args) throws Exception {
//        generator();
//    }
//
//    public void generator () throws Exception{
//
//        List<String> warnings = new ArrayList<String>();
//        boolean overwrite = true;
////        File configFile = new File("generatorConfig.xml");
//        ConfigurationParser cp = new ConfigurationParser(warnings);
//
//        Configuration config = cp.parseConfiguration(this.getClass().getResourceAsStream("/generatorConfig.xml"));
//        DefaultShellCallback callback = new DefaultShellCallback(overwrite);
//
//        MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config,callback,warnings);
//        myBatisGenerator.generate(null);
//    }
}
