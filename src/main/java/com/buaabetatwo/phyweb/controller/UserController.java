package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.annotation.LocalLock;
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

import static com.buaabetatwo.phyweb.PhywebApplication.myToken;

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
        String email = user2.getEmail();
        User user = userMapper.getByEmail(email);
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
    public String postEditUserProfile(String name, String sex, String school, String introduction,
                                      String email, Model model, String oldPassword, String newPassword2) {
        if (oldPassword != null) {
            User user = userMapper.getByEmail(email);
            SimpleHash hash = new SimpleHash("md5", oldPassword);
            String Pw = (hash.toHex());
            if (user.getPassword().equals(Pw)) {
                SimpleHash hash2 = new SimpleHash("md5", newPassword2);
                String Pw2 = (hash2.toHex());
                userMapper.updateUserPw(Pw2, email);
                model.addAttribute("resetPwSuccessMessage", "修改成功，请重新登录");
                return "login";
            } else {
                model.addAttribute("user", user);
                model.addAttribute("failEditPassword", "原密码不正确，若忘记密码，可通过登录页面进行重置");
                return "edit-profile";
            }
        }
        userMapper.updateUserInfo(name, sex, school, introduction, email);
        User user = userMapper.getByEmail(email);
        model.addAttribute("user", user);
        return "user-center";
    }

    @GetMapping("/reset")
    public String getReset() {
        return "reset";
    }

    @LocalLock(key = "myToken")  //即使按钮禁用了，用户也能刷新来继续请求发送邮件。所以锁起来（60秒）
    @PostMapping("/reset-email")
    public String postResetEmail(String email, Model model) {
        if (myToken == 1) {
            User user = userMapper.getByEmail(email);
            verifyCode = mailService.verifyCodeGen();
            if (user == null) {
                model.addAttribute("failMessage", "账号不存在");
            } else {
                mailService.sendMail(email, "重置密码", verifyCode, 0);
                model.addAttribute("successMessage", "发送成功");
                model.addAttribute("useremail", email);
            }
        } else {
            model.addAttribute("successMessage", "已经发送，请勿刷新页面");
            model.addAttribute("useremail", email);
        }
        return "reset";
    }

    @GetMapping("/reset-email")
    public String getResetEmail() {
        return "reset";
    }

    @PostMapping("/reset")
    public String postResetCode(String resetCode, Model model, String resetemail) {

        if (resetemail.isEmpty()) {
            model.addAttribute("failMessage", "请填写邮箱");
            return "reset";
        }
        if (resetCode.equals(verifyCode)) {
            User user = userMapper.getByEmail(resetemail);
            if (user == null) {
                model.addAttribute("failMessage", "账号不存在");
                return "reset";
            }
            model.addAttribute("sucessResetMessage", "密码重置成功，请重新登录");
            String pw = mailService.passwordGen();
            mailService.sendMail(resetemail, "重置密码", pw, 1);
            SimpleHash hash = new SimpleHash("md5", pw);
            String newPw = (hash.toHex());
            userMapper.updateUserPw(newPw, resetemail);
        } else {
            model.addAttribute("failMessage", "验证码错误");
            return "reset";
        }
        model.addAttribute("resetPwSuccessMessage", "重置成功，密码已经发送至您的邮箱");
        return "login";
    }

}
