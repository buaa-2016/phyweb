package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.ReportMapper;
import com.buaabetatwo.phyweb.model.Report;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class ReportCenterController {
    @Autowired
    private ReportMapper reportMapper;

    @GetMapping("/report-center")
    public String getReportCenter(Model model) {
        List<Report> reports = reportMapper.findAll();
        model.addAttribute("reportTemplates", reports);
        return "report-center";
    }

}