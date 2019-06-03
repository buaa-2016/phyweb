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

    //@Test
    public void insertQues() {
        //添加填空题的测试

        //下方三项内容为填空题必填内容
        Question ques = new Question();
        ques.setTitle("运动物体通过路径的___________叫做路程");
        ques.setAnswer("轨迹长度");
        //其中Blank必填，作为判断该题是填空题的标准
        ques.setType("BLANK");
        questionMapper.insertQuestion(ques);
    }

    //@Test
    public void insertQuesAnswer() {
        Question ques = new Question();
        //下方三项内容为简答题必填内容
        ques.setTitle("在游泳池边向池底看去，感觉池水并不深，下水后才知道不是这么回事，试分析：为什么池水深度看起来比实际的浅？");

        ques.setAnswer("光从一种介质斜射入另一种介质时要发生折射，人从空气看河底，实际看到的是河底的虚像，虚像的位置比实际河底的位置浅");

        ques.setType("ANSWER");

        questionMapper.insertQuestion(ques);
    }

    @Test
    public void contextLoads() {
        System.out.println("Test Success!");
    }

}
