package com.buaabetatwo.phyweb.common;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.nio.file.Paths;

@Configuration
public class StaticResourceConfig implements WebMvcConfigurer {
    @Value("${phyweb.scriptsPath}")
    private String scriptsPath;

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        String path = Paths.get(scriptsPath.trim()).toAbsolutePath().toString();
        registry.addResourceHandler("/**").addResourceLocations(path);
    }
}