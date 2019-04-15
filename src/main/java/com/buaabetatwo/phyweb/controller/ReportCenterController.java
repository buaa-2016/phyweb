package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.ReportMapper;
import com.buaabetatwo.phyweb.model.Report;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

@Controller
public class ReportCenterController {
    @Value("${phyweb.baseDir}")
    private String baseDir;
    @Value("${phyweb.scriptsPath")
    private String scriptsPath;

    @Autowired
    private ReportMapper reportMapper;

    @GetMapping("/report-center")
    public String getReportCenter(Model model) {
        List<Report> reports = reportMapper.findAll();
        model.addAttribute("reportTemplates", reports);
        return "report-center";
    }

    @PostMapping("/report")
    public Map createReport() throws IOException {

        String testScript = Paths.get(baseDir, scriptsPath, "test.sh").toString();
        String cmd = testScript + " " + "gakki";
        Process child = Runtime.getRuntime().exec(cmd);
        Scanner sc = new Scanner(child.getInputStream());
        int exitValue = child.exitValue();
        System.out.printf("exit value: %d%n", exitValue);
        System.out.println(sc.nextLine());

        Map<String, String> json = new HashMap<>();
        json.put("status", "testing");
        return json;
    }

}