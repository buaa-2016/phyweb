package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.UserMapper;
import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.subject.Subject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;

@Controller
public class IndexController {
    @Autowired
    private UserMapper userMapper;
    private Logger logger = LoggerFactory.getLogger(IndexController.class);

    @RequestMapping(value={"/", "/index"})
    public String index(Model model){
        User user = (User) SecurityUtils.getSubject().getPrincipal();
            logger.info(user.toString());
            model.addAttribute("user", user);
        return "index";
    }
}