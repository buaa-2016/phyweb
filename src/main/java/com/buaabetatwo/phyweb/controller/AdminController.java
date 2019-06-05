package com.buaabetatwo.phyweb.controller;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class AdminController {
    private static Logger logger = LoggerFactory.getLogger(AdminController.class);

    @GetMapping("/editQuestion")
    public String EditQuestion() {
        return "editQuestion";
    }

}
