package com.buaabetatwo.phyweb.controller;


import com.buaabetatwo.phyweb.mapper.QuestionMapper;
import com.buaabetatwo.phyweb.model.Question;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class QuestionController {

    @Autowired
    private QuestionMapper questionMapper;

    @GetMapping("/question")
    public String getQuestion(Model model) {
        List<Question> questionList = questionMapper.findAll();
        processQuestion(questionList);
        model.addAttribute("questionList", questionList);
        return "questionAll";
    }

    @GetMapping("/questionDetail")
    public String getQuestionDetail(Model model) {
//        Question question = questionMapper.findById(id);
//        model.addAttribute("question", question);
        return "questionDetail";
    }

    private void processQuestion(List<Question> list) {
        for (Question ques : list) {
            ques.setTitle(ques.getTitle().substring(0,25) + "......");
        }
    }
}
