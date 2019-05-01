package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.common.ShiroRealm;
import com.buaabetatwo.phyweb.mapper.UserMapper;
import com.buaabetatwo.phyweb.model.User;
import com.buaabetatwo.phyweb.service.MailService;
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

    @Autowired
    private MailService mailService;

    private String verifyCode;

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

    @GetMapping("/reset")
    public String getReset(){
        return "reset";
    }

    @PostMapping("/reset-email")
    public String postResetEmail(String email, Model model,String resetCode ) {
        User user=userMapper.getByEmail(email);
        verifyCode=mailService.verifyCodeGen();
        if(user==null){
            model.addAttribute("failMessage", "账号不存在");
        }
        else{
            mailService.sendMail(email,"重置密码",verifyCode,0);
            model.addAttribute("successMessage", "发送成功");
            model.addAttribute("useremail",email);
        }
        return"reset";
    }
    @PostMapping("/reset")
    public String postResetCode(String resetCode,Model model,String resetemail){

        if(resetCode.equals(verifyCode)){
            model.addAttribute("sucessResetMessage","密码重置成功，请重新登录");
            String pw=mailService.passwordGen();
            mailService.sendMail(resetemail,"重置密码",pw,1);
            SimpleHash hash = new SimpleHash("md5", pw);
            String newPw=(hash.toHex());
            userMapper.updateUserPw(newPw, resetemail);
        }

        return "login";
    }


    
}
