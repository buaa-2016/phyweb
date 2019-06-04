package com.buaabetatwo.phyweb.controller;


import com.buaabetatwo.phyweb.mapper.QuestionMapper;
import com.buaabetatwo.phyweb.mapper.CommentMapper;
import com.buaabetatwo.phyweb.mapper.User_questionMapper;
import com.buaabetatwo.phyweb.model.Question;
import com.buaabetatwo.phyweb.model.Comment;
import com.buaabetatwo.phyweb.model.User;
import com.buaabetatwo.phyweb.model.User_question;
import org.apache.shiro.SecurityUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.sql.Timestamp;
import java.util.Date;
import java.util.List;

@Controller
public class QuestionController {

    @Autowired
    private QuestionMapper questionMapper;
    @Autowired
    private CommentMapper commentMapper;
    @Autowired
    private User_questionMapper user_questionMapper;
    
    @GetMapping("/question")
    public String getQuestion(Model model) {
        List<Question> questionList = questionMapper.findAll();
        processQuestion(questionList);
        model.addAttribute("questionList", questionList);
        
        int question_id = 1;
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        User_question userquestion = user_questionMapper.findById(user.getId());
        if (userquestion == null) {
            User_question userques = new User_question();
            userques.setId(user.getId());
            userques.setQuestion_id(1);
            user_questionMapper.insertByUser_question(userques);
            question_id = userques.getQuestion_id();
        }
        else {
            question_id = userquestion.getQuestion_id();
        }
        model.addAttribute("question_id", question_id);
        
        return "questionAll";
    }

    @GetMapping("/questionDetail")
    public String getQuestionDetail(@RequestParam(name = "id") int id, Model model) {
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        User_question userquestion = new User_question();
        userquestion.setId(user.getId());
        userquestion.setQuestion_id(id);
        user_questionMapper.updateuser_question(userquestion);
        
        String result = getModel(model, id);
        if (result != null) return result;
        return "questionDetail";
    }

    @PostMapping("/comment")
    public String insertComment(@RequestParam(name = "comment") String comment, @RequestParam(name = "id") int id , Model model) {
        Comment newCom = new Comment();
        newCom.setId(id);
        newCom.setContent(comment);
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        if (user == null) newCom.setName("匿名用户");
        else newCom.setName(user.getName());
        newCom.setTime(new Date());

        commentMapper.insertByComment(newCom);

        String result = getModel(model, id);
        if (result != null) return result;

        return "questionDetail";
    }
    
    @PostMapping("/comment_1")
    public String changeComment(@RequestParam(name = "content_id") String content_id,
            @RequestParam(name = "comment_co") String comment, 
            @RequestParam(name = "id") int id , Model model) {
        int num = 0;
        try {
            num = Integer.parseInt(content_id);
        }catch(NumberFormatException e){
            String result = getModel(model, id);
            if (result != null) return result;
        }
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        Comment newCom = new Comment();
        newCom.setId(id);
        newCom.setContent(comment);
        newCom.setName(user.getName());
        newCom.setContent_id(num);        
        commentMapper.changecomment(newCom);
        String result = getModel(model, id);
        if (result != null) return result;

        return "questionDetail";
    }

    private void processQuestion(List<Question> list) {
        for (Question ques : list) {
            if(ques.getTitle().length() <= 25) continue;
            ques.setTitle(ques.getTitle().substring(0,25) + "......");
        }
    }

    private String getModel(Model model, int id) {
        Question question = questionMapper.findById(id);
        List<Comment> commentList = commentMapper.findAllById(id);
        if (question == null) {
            return "forward:/question";
        }

        model.addAttribute("question", question);
        model.addAttribute("commentList", commentList);
        return null;
    }
    
}
