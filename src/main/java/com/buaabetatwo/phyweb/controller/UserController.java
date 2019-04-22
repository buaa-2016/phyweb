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

    @GetMapping("/index/userupdate")
    public String UserShow(Model model) {
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        model.addAttribute("user", user);
        return "userupdate";
    }

    @PostMapping("/index/userupdate")
    public String UserUpdate(String name,String email,String student_id,String password3,String introduction){
        if(password3==null) {
            userMapper.updateUserInfo(name, email, student_id,introduction);
        }
        else {
            SimpleHash hash = new SimpleHash("md5", password3);
            String newPw=(hash.toHex());
            userMapper.updateUserPw(newPw, student_id);
        }
       return "login";
    }

    @GetMapping("/user-center")
    public String UserCenter(Model model) {
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        model.addAttribute("user", user);
        return "user-center";
    }

    @GetMapping("/edit-profile")
    public String getEditUserProfile() {
        return "edit-profile";
    }

    @PostMapping("/edit-profile")
    public String postEditUserProfile(Model model, String nickName, String gender, String introduction, String oldPassword, String newPassword) {

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
    }
}
