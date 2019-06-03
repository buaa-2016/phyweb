package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.QuestionMapper;
import com.buaabetatwo.phyweb.model.Question;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.Map;

//用户上传题目后端接口，目前打算全部写在该文件中
@Controller
public class UploadQuestion {
    private static Logger logger = LoggerFactory.getLogger(UploadQuestion.class);

    @Autowired
    private QuestionMapper questionMapper;

    @GetMapping("/questionUpload")
    public String getQuestionUpload() {
        return "questionUpload";
    }

    @PostMapping("/questionUpload")
    public String postQuestionUpload(Question question, Model model) {
        System.out.println(question.toString());
        try {
            questionMapper.insertQuestion(question);
            model.addAttribute("message_success", "上传成功！");
        } catch (Exception e) {
            logger.error("插入题目错误！错误为：" + e.toString());
            model.addAttribute("message_error", "插入题目出错: " + e.toString());
        }
        return "questionUpload";
    }

    //插入题目控制器
    @ResponseBody
    @PostMapping("/insertQues")
    public Map insertQues(@RequestBody Question question) {
        Map<String,String> ans = new HashMap<>();
        try {
            questionMapper.insertQuestion(question);
        } catch (Exception e) {
            logger.error("插入题目错误！错误为：" + e.toString());
            ans.put("result","fail");
        }
        ans.put("result","success");
        return ans;
    }

}
