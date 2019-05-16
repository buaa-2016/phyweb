package com.buaabetatwo.phyweb.controller;


import com.buaabetatwo.phyweb.mapper.QuestionMapper;
import com.buaabetatwo.phyweb.mapper.CommentMapper;
import com.buaabetatwo.phyweb.model.Question;
import com.buaabetatwo.phyweb.model.Comment;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@Controller
public class QuestionController {

    @Autowired
    private QuestionMapper questionMapper;
    @Autowired
    private CommentMapper commentMapper;

    @GetMapping("/question")
    public String getQuestion(Model model) {
        List<Question> questionList = questionMapper.findAll();
        processQuestion(questionList);
        model.addAttribute("questionList", questionList);
        return "questionAll";
    }

    @GetMapping("/questionDetail")
    public String getQuestionDetail(@RequestParam(name = "id") int id, Model model) {
        Question question = questionMapper.findById(id);
        List<Comment> commentList = commentMapper.findAllById(id);
        if (question == null) {
            return "forward:/question";
        }

        model.addAttribute("question", question);
        model.addAttribute("commentList", commentList);
        return "questionDetail";
    }

    @PostMapping("/comment")
    public String insertComment(@RequestParam(name = "comment") String comment, @RequestParam(name = "id") int id , Model model) {


        return "questionDetail";
    }

    private void processQuestion(List<Question> list) {
        for (Question ques : list) {
            ques.setTitle(ques.getTitle().substring(0,25) + "......");
        }
    }
    
}
