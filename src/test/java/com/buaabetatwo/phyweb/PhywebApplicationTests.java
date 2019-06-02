package com.buaabetatwo.phyweb;


import com.buaabetatwo.phyweb.mapper.QuestionMapper;
import com.buaabetatwo.phyweb.model.Question;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class PhywebApplicationTests {

    @Autowired
    private QuestionMapper questionMapper;

    @Test
    public void insertQues() {
        Question ques = new Question();
        ques.setTitle("运动物体通过路径的___________叫做路程");
        ques.setAnswer("轨迹长度");
        ques.setType("BLANK");
        questionMapper.insertQuestion(ques);
    }

    @Test
    public void contextLoads() {
        System.out.println("Test Success!");
    }

}
