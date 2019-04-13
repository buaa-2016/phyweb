package com.buaabetatwo.phyweb.controller;


import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.List;

import javax.servlet.http.HttpServletResponse;

import org.apache.ibatis.annotations.Param;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.buaabetatwo.phyweb.mapper.ReportMapper;
import com.buaabetatwo.phyweb.model.Report;

@RestController
public class ReportController {
    private static Logger logger = LoggerFactory.getLogger(ReportController.class);
    @Autowired
    private ReportMapper reportMapper;

    @GetMapping("/report")
    public String ReportLists() {
        return reportMapper.findlist().toString();
    }

    @RequestMapping("/findById")
    public String findById(@RequestParam("id") int id) {
        return reportMapper.findById(id).toString();
    }



}

