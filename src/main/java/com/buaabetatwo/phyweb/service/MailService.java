package com.buaabetatwo.phyweb.service;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;

import javax.mail.internet.MimeMessage;
import java.util.Random;


@Service
public class MailService {

    @Autowired
    private JavaMailSender mailSender;


    @Autowired
    TemplateEngine templateEngine;

    @Async
    public void sendMail(String to, String subject, String verifyCode, int flag) {
        //创建邮件正文
        Context context = new Context();
        context.setVariable("resetCode", verifyCode);
        context.setVariable("email", to);
        //将模块引擎内容解析成html字符串
        String emailContent;
        if (flag == 0)
            emailContent = templateEngine.process("emailmodule", context);
        else
            emailContent = templateEngine.process("emailmodule2", context);
        MimeMessage message = mailSender.createMimeMessage();
        try {
            //true表示需要创建一个multipart message
            MimeMessageHelper helper = new MimeMessageHelper(message, true);
            helper.setFrom("asdfghpeter@foxmail.com");
            helper.setTo(to);
            helper.setSubject(subject);
            helper.setText(emailContent, true);
            mailSender.send(message);
        } catch (Exception e) {
            System.out.println("html格式邮件发送失败");
        }
    }

    public String verifyCodeGen() {
        String str = "";
        char[] ch = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

        Random random = new Random();
        for (int i = 0; i < 6; i++) {
            char num = ch[random.nextInt(ch.length)];
            str += num;
        }
        return str;
    }

    public String passwordGen() {
        String str = "";
        char[] ch = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        Random random = new Random();
        for (int i = 0; i < 8; i++) {
            char num = ch[random.nextInt(ch.length)];
            str += num;
        }
        return str;
    }
}
