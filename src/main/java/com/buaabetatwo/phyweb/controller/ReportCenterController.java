package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.ReportMapper;
import com.buaabetatwo.phyweb.model.Report;
import com.buaabetatwo.phyweb.model.User;
import org.apache.shiro.SecurityUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

@Controller
public class ReportCenterController {
    private static Logger logger = LoggerFactory.getLogger(ReportCenterController.class);

    private static final String path = System.getProperty("user.dir") + "/classes/static/script/";

    private static HashMap<String,String> reportMap = new HashMap<>();
    static {
        reportMap.put("10111","1010113");
        reportMap.put("10112","1010212");
        reportMap.put("10211","1020113");
        reportMap.put("10212","1020212");
        reportMap.put("10311","1030113");
        reportMap.put("10611","1060111");
        reportMap.put("10612","1060213");
        reportMap.put("10711","1070212");
        reportMap.put("10712","1070312");
        reportMap.put("10811","1080114");
        reportMap.put("10821","1080215");
        reportMap.put("10822","1080225");
        reportMap.put("10911","1090114");
        reportMap.put("10912","1090212");
        reportMap.put("10913","1090312");
    }

    @Autowired
    private ReportMapper reportMapper;

    @GetMapping("/report-center")
    public String getReportCenter(Model model) {
        User user = (User) SecurityUtils.getSubject().getPrincipal();
        List<Report> reports = reportMapper.findAll();
        model.addAttribute("reportTemplates", reports);
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
    public Map createReport(@RequestParam("xml") String xmlData, @RequestParam("id") int id, @RequestParam("kind") int kind) throws IOException, InterruptedException {

        Report report = reportMapper.findById(id);
        Map<String, String> jsonResponse = new HashMap<>();

        String randomXmlFilename = UUID.randomUUID().toString() + ".xml";
        String randomPdfFilename = UUID.randomUUID().toString();

        String pdfPath = path + "pdf/" + randomPdfFilename;


        // write xml data to file
        String xmlLabDataPath = path + "/xml/"+ randomXmlFilename;
        Files.write(Paths.get(xmlLabDataPath), xmlData.getBytes());

        // step 3: execute command
        String cmd = "python2 " + path +"handler.py " + reportMap.get(String.valueOf(report.getExperiment_id()) + kind) + " " + xmlLabDataPath
                 + " " + pdfPath;
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
        jsonResponse.put("link", randomPdfFilename+".pdf");
        jsonResponse.put("experimentId", String.valueOf(report.getExperiment_id()));
        return jsonResponse;
    }

}