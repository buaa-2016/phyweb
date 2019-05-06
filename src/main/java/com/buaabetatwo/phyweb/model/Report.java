package com.buaabetatwo.phyweb.model;

import java.util.Date;

public class Report {
    private int id;
    private String script_link;
    private int experiment_id;
    private String experiment_name;
    private String prepare_link;
    private java.util.Date created_at;
    private java.util.Date updated_at;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getScript_link() {
        return script_link;
    }

    public void setScript_link(String script_link) {
        this.script_link = script_link;
    }

    public int getExperiment_id() {
        return experiment_id;
    }

    public void setExperiment_id(int experiment_id) {
        this.experiment_id = experiment_id;
    }

    public String getExperiment_name() {
        return experiment_name;
    }

    public void setExperiment_name(String experiment_name) {
        this.experiment_name = experiment_name;
    }

    public String getPrepare_link() {
        return prepare_link;
    }

    public void setPrepare_link(String prepare_link) {
        this.prepare_link = prepare_link;
    }

    public Date getCreated_at() {
        return created_at;
    }

    public void setCreated_at(Date created_at) {
        this.created_at = created_at;
    }

    public Date getUpdated_at() {
        return updated_at;
    }

    public void setUpdated_at(Date updated_at) {
        this.updated_at = updated_at;
    }

    @Override
    public String toString() {
        return "Report{" +
                "id=" + id +
                ", script_link='" + script_link + '\'' +
                ", experiment_id=" + experiment_id +
                ", experiment_name='" + experiment_name + '\'' +
                ", prepare_link='" + prepare_link + '\'' +
                ", created_at=" + created_at +
                ", updated_at=" + updated_at +
                '}';
    }
}
