package com.buaabetatwo.phyweb.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class indexController {
    @RequestMapping("")
    public String simple(ModelMap map){
        map.addAttribute("temp","helloWorld");
        return "index";
    }
}