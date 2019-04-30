package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.common.ShiroRealm;
import com.buaabetatwo.phyweb.mapper.UserMapper;
import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.credential.PasswordMatcher;
import org.apache.shiro.authc.credential.PasswordService;
import org.apache.shiro.crypto.hash.SimpleHash;
import org.apache.shiro.mgt.RealmSecurityManager;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class UserController {

    @Autowired
    private UserMapper userMapper;



    @GetMapping("/user-center")
    public String UserCenter(Model model) {
        User user2 = (User) SecurityUtils.getSubject().getPrincipal();
        String email =user2.getEmail();
        User user=userMapper.getByEmail(email);
        model.addAttribute("user", user);
        return "user-center";
    }

    @GetMapping("/edit-profile")
    public String getEditUserProfile(Model model) {
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        model.addAttribute("user", user);
        return "edit-profile";
    }

    @PostMapping("/edit-profile")
    public String postEditUserProfile(String name,String sex,String school,String introduction,String email,Model model) {
        /*
        if (oldPassword != null) {
            RealmSecurityManager sm = (RealmSecurityManager) SecurityUtils.getSecurityManager();
            ShiroRealm realm = (ShiroRealm) sm.getRealms().iterator().next();
            PasswordMatcher matcher = (PasswordMatcher) realm.getCredentialsMatcher();
            PasswordService passwordService = (PasswordService) matcher.getPasswordService();
            User currentUser = (User)SecurityUtils.getSubject().getPrincipal();
            if (!passwordService.passwordsMatch(oldPassword, currentUser.getPassword())) {
                model.addAttribute("message", "密码不匹配");
                model.addAttribute("messageType", "error");
                return "edit-profile";
            }
            model.addAttribute("message", "修改密码成功");
            model.addAttribute("messageType", "success");
            return "edit-profile#change-password";
        } else {
            return "edit-profile";
        }
        */
        userMapper.updateUserInfo(name,sex,school,introduction,email);
        User user=userMapper.getByEmail(email);
        model.addAttribute("user", user);
        return "user-center";
    }
}
