package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.UserMapper;
import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.crypto.hash.SimpleHash;
import org.apache.shiro.subject.Subject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class AuthController {
    private static Logger logger = LoggerFactory.getLogger(AuthController.class);
    @Autowired
    private UserMapper userMapper;

    @GetMapping("/register")
    public String getRegister() {
        logger.info("get");
        return "register";
    }

    @PostMapping("/register")
    public String postRegister(User user, Model model) {
        SimpleHash hash = new SimpleHash("md5", user.getPassword());
        String encryptedPassword = hash.toHex();
        user.setPassword(hash.toHex());
        if(userMapper.getByStudentId(user.getStudent_id())==null&&
        userMapper.getByEmail(user.getEmail())==null){
            userMapper.insertByUser(user);
            model.addAttribute("successmessage", "注册成功，请登录！");
            return "login";
        }
        else{
            model.addAttribute("message", "注册失败，邮箱已存在！");
        }
        return "register";
    }


    @GetMapping("/login")
    public String Login() {
        if (SecurityUtils.getSubject().isAuthenticated()) {
            return "redirect:/index";
        }
        return "login";
    }

    /**
     * Login by post
     * @param username
     * @param password
     * @param model
     * @return
     */
    @PostMapping("/login")
    public Object login(String username, String password, Model model) {
        Subject user = SecurityUtils.getSubject();
        UsernamePasswordToken token = new UsernamePasswordToken(username, password);
        try {
            // doGetAuthenticationInfo()接收一个token,
            // 这个Token将传给ShiroRealm.doGetAuthenticationInfo()
            // doGetAuthenticationInfo取出token中的username, 然后从数据库中
            // 取出密码，构造一个AuthenticationInfo对象。
            user.login(token);
            return "redirect:/index";
        } catch (UnknownAccountException e) {
            model.addAttribute("message", "登陆失败：账号不存在！");
        } catch (DisabledAccountException e) {
            model.addAttribute("message", "登陆失败：账号未启用！");
        } catch (IncorrectCredentialsException e) {
            model.addAttribute("message", "登陆失败：密码错误！");
        } catch (Throwable e) {
            model.addAttribute("message", "登陆失败：未知错误！");
        }
        return "login";
    }
    /**
     * Logout
     * @return
     */
    @RequestMapping("/logout")
    public String logout(Model model) {
        SecurityUtils.getSubject().logout();
        model.addAttribute("loginoutmessage","已成功注销！");
        return "login";
    }

}
