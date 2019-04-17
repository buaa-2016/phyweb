package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.ReportMapper;
import com.buaabetatwo.phyweb.model.Report;
import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.apache.commons.codec.digest.DigestUtils;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

@Controller
public class ReportCenterController {
    private static Logger logger = LoggerFactory.getLogger(ReportCenterController.class);

    public static final String path = System.getProperty("user.dir") + "/target/classes/static/script/";

    @Autowired
    private ReportMapper reportMapper;

    @GetMapping("/report-center")
    public String getReportCenter(Model model) {
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        List<Report> reports = reportMapper.findAll();
        model.addAttribute("reportTemplates", reports);
        model.addAttribute("pic_hash", "http://www.gravatar.com/avatar/"+DigestUtils.md5Hex(user.getEmail())+"?s=55?d=monsterid");
        model.addAttribute("name",user.getName());
        return "report-center";
    }

    public String readLastLineFromStream(InputStream in) {
        Scanner sc = new Scanner(in);
        String lastLine = null;
        while (sc.hasNext()) {
            lastLine = sc.nextLine();
            logger.info(lastLine);
        }
        return lastLine;
    }

    @ResponseBody
    @PostMapping("/report")
    public Map createReport(@RequestParam("xml") String xmlData, @RequestParam("id") int id) throws IOException, InterruptedException {

        Report report = reportMapper.findById(id);
        Map<String, String> jsonResponse = new HashMap<>();

        String randomXmlFilename = UUID.randomUUID().toString() + ".xml";
        String randomPdfFilename = UUID.randomUUID().toString() + ".pdf";

        String xmlLabDataPath = path + "xml/" + randomXmlFilename;

        String pdfPath = path + "pdf/" + randomPdfFilename;

        logger.info("pythonScriptPath: {}", xmlLabDataPath);

        // write xml data to file
        Files.write(Paths.get(xmlLabDataPath), xmlData.getBytes());

        // step 3: execute command
        String cmd = "python3 handler.py " + report.getScript_link() + " " + xmlLabDataPath
                 + " " + pdfPath + " " + path;
        logger.info("command: {}", cmd);
        Process child = Runtime.getRuntime().exec(cmd);
        int exitValue = child.waitFor();
        String output = readLastLineFromStream(child.getInputStream());
        logger.info("exit value: {}", exitValue);
        logger.info("output: {}", output);

        if (exitValue != 0 || !output.equals("{\"status\":\"success\"}")) {
            jsonResponse.put("status", "fail");
            return jsonResponse;
        }

        jsonResponse.put("status", "success");
        jsonResponse.put("link", randomPdfFilename);
        jsonResponse.put("experimentId", String.valueOf(report.getExperiment_id()));
        return jsonResponse;
    }


}