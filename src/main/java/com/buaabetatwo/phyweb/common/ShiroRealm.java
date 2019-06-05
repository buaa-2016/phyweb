package com.buaabetatwo.phyweb.common;

import com.buaabetatwo.phyweb.mapper.RoleMapper;
import com.buaabetatwo.phyweb.mapper.UserMapper;
import com.buaabetatwo.phyweb.model.Role;
import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.*;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;


/**
 * shiro框架 用户登录与权限控制类继承自AuthorizingRealm
 * 重写其中的 doGetAuthorizationInfo(PrincipalCollection principals) 权限控制
 * doGetAuthenticationInfo(AuthenticationToken token) 登录控制
 */

public class ShiroRealm extends AuthorizingRealm {
    private static final Logger logger = LoggerFactory.getLogger(ShiroRealm.class);

    @Autowired
    private UserMapper userMapper;

    @Autowired
    private RoleMapper roleMapper;

    /**
     * 认证：通过账号密码判断是不是用户
     *
     * @param authenticationToken
     * @return
     * @throws AuthenticationException
     */
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken authenticationToken) throws AuthenticationException {
        logger.info("doGetAuthenticationInfo");
        UsernamePasswordToken token = (UsernamePasswordToken) authenticationToken;
        logger.info("用户名:{}", token.getUsername());
        logger.info("密码:{}", token.getPassword());

        String email_or_student_id = token.getUsername();
        // 先尝试用邮箱查找用户
        User user = userMapper.getByEmail(email_or_student_id);
        // 再尝试用学号查找用户
        if (user == null)
            user = userMapper.getByStudentId(email_or_student_id);
        if (user == null) {
            return null;
        }
        logger.info(user.toString());
        String salt = String.valueOf(user.getId());
        logger.info("email:{}", user.getEmail());
        logger.info("username:{}", user.getName());
        logger.info("password:{}", user.getPassword());
        // 这里传递一个user作为pricipal，登陆成功后，通过SecurityUtils.getSubject().getPrincipal()
        // 就可以获取到用户对象User
        // 这里为什么没有传递username ???
        return new SimpleAuthenticationInfo(user, user.getPassword(), getName());
    }


    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principalCollection) {
        logger.info("doGetAuthorizationInfo+" + principalCollection.toString());

        SimpleAuthorizationInfo info = new SimpleAuthorizationInfo();

        User user = (User) principalCollection.getPrimaryPrincipal();

        Role role = roleMapper.getRoleByName(user.getName());

        //目前权限仅有简单的管理者或者普通人
        //所以权限设置为Admin
        if (role != null) {
            info.addRole(role.getRole());
            info.addStringPermission(role.getRole());
        }

        return info;
    }
}
