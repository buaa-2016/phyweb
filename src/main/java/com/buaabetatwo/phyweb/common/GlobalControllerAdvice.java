package com.buaabetatwo.phyweb.common;

import com.buaabetatwo.phyweb.model.User;
import com.buaabetatwo.phyweb.util.GravatarAPI;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.UnavailableSecurityManagerException;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ModelAttribute;

import java.util.HashMap;

@ControllerAdvice
public class GlobalControllerAdvice {

    /**
     * 自动将当前登录用户加入到每个请求中
     *
     * PS: 当用户未登录时，currentUser为null，
     * 可以配合shiro来判定用户是否登录。
     * @param model
     */
    @ModelAttribute
    public void addUserAttribute(Model model) {
        User user = null;
        try {
            user = (User) SecurityUtils.getSubject().getPrincipal();
        } catch (UnavailableSecurityManagerException ignored) {};
        if (user != null) {
            String avatar = GravatarAPI.emailToAvatarUrl(user.getEmail());
            model.addAttribute("userAvatar", avatar);
            model.addAttribute("currentUser", user);
        }
    }

}
