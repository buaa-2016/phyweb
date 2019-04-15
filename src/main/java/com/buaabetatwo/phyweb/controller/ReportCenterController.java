package com.buaabetatwo.phyweb.controller;

import com.buaabetatwo.phyweb.mapper.ReportMapper;
import com.buaabetatwo.phyweb.model.Report;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

@Controller
public class ReportCenterController {
    private static Logger logger = LoggerFactory.getLogger(ReportCenterController.class);

    @Value("${phyweb.scriptsPath}")
    private String scriptsPath;

    @Autowired
    private ReportMapper reportMapper;

    @GetMapping("/report-center")
    public String getReportCenter(Model model) {
        List<Report> reports = reportMapper.findAll();
        model.addAttribute("reportTemplates", reports);
        return "report-center";
    }

    public String getScriptPath(String filename) {
        return Paths.get(scriptsPath.trim(), filename).toAbsolutePath().toString();
    }

    public String getWorkingDirectory() {
        return Paths.get(scriptsPath.trim()).toAbsolutePath().toString();
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
        String randomLatexFilename = UUID.randomUUID().toString() + ".tex";
        String randomPdfFilename = randomLatexFilename.replace(".text", ".pdf");

        String xmlLabDataPath = getScriptPath(randomXmlFilename);
        String createScriptPath = getScriptPath("create.sh");
        String pythonScriptPath = getScriptPath(report.getScript_link());
        String latexDocumentPath = getScriptPath(randomLatexFilename);

        // write xml data to file
        Files.write(Paths.get(xmlLabDataPath), xmlData.getBytes());

        // step 3: execute command
        String cmd = createScriptPath + " " + getWorkingDirectory() + " " + pythonScriptPath + " " + xmlLabDataPath + " " + latexDocumentPath;
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