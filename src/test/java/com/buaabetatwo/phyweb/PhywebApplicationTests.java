package com.buaabetatwo.phyweb;

import com.buaabetatwo.phyweb.controller.ReportCenterController;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class PhywebApplicationTests {

    @Test
    public void contextLoads() {
        System.out.println("Test Success!");
    }

    @Test
    public void TestPath() {
        System.out.println(ReportCenterController.path);
    }

}
