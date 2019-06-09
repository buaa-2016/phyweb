package com.buaabetatwo.phyweb.controller;


import com.buaabetatwo.phyweb.mapper.QuestionMapper;
import com.buaabetatwo.phyweb.mapper.QuestionUploadMapper;
import com.buaabetatwo.phyweb.model.Question;
import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

import static com.buaabetatwo.phyweb.controller.QuestionController.processQuestion;

@Controller
public class AdminController {
    private static Logger logger = LoggerFactory.getLogger(AdminController.class);

    @Autowired
    private QuestionUploadMapper questionUploadMapper;

    @Autowired
    private QuestionMapper questionMapper;

    @GetMapping("/editQuestoinAll")
    public String EditQuestionAll(Model model) {

        List<Question> questionList = questionUploadMapper.findAll();
        processQuestion(questionList);
        model.addAttribute("questionList", questionList);

        return "questionUploadAll";
    }


    @GetMapping("/editQuestionDetail")
    public String getQuestionDetail(@RequestParam(name = "id") int id, Model model) {
        User user = (User) SecurityUtils.getSubject().getPrincipal();

        Question question = questionUploadMapper.findById(id);

        model.addAttribute("question", question);

        return "questionCheck";
    }

    @GetMapping("/editDetails")
    public String changeData(@RequestParam("id") int id) {
        Question question = questionUploadMapper.findById(id);
        questionMapper.insertQuestion(question);
        questionUploadMapper.deleteQuestionById(id);
        return "forward:/editQuestoinAll";
    }

    @GetMapping("/editQuestion")
    public String EditQuestion() {
        return "editQuestion";
    }

}
