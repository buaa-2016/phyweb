package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Controller
public class indexController {

    @RequestMapping(value={"/", "/index"})
    public String simple(ModelMap map){
        map.addAttribute("temp","helloWorld");

        User user = (User) SecurityUtils.getSubject().getPrincipal();

        return "index";
    }
}