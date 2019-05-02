package com.buaabetatwo.phyweb;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.buaabetatwo.phyweb.mapper")
public class PhywebApplication {
    public  static int myToken=0;
    public static void main(String[] args) {
        SpringApplication.run(PhywebApplication.class, args);
    }

}
