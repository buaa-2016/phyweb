package com.buaabetatwo.phyweb.model;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class Report {
	private int id;
    private String script_link;
    private int experiment_id;
    private String experiment_name;
    private String prepare_link;
    private java.util.Date created_at;
    private java.util.Date updated_at;
    
    public int get_id() {
    	return id;
    }
    
    public void set_id(int id) {
    	this.id = id;
    }
    
    public String get_script_link() {
    	return script_link;
    }
    
    public void set_script_link(String script_link) {
    	this.script_link = script_link;
    }
    
    public int get_experiment_id() {
    	return experiment_id;
    }
    
    public void set_experiment_id(int experiment_id) {
    	this.experiment_id = experiment_id;
    }
    
    public String get_experiment_name() {
    	return experiment_name;
    }
    
    public void set_experiment_name(String experiment_name) {
    	this.experiment_name = experiment_name;
    }
    
    public String get_prepare_link() {
    	return prepare_link;
    }
    
    public void set_prepare_link(String prepare_link) {
    	this.prepare_link = prepare_link;
    }
    
    public java.util.Date get_created_at() {
    	return created_at;
    }
    
    public void set_created_at(java.util.Date created_at) {
    	this.created_at = created_at;
    }
    
    public java.util.Date get_updated_at() {
    	return updated_at;
    }
    
    public void set_updated_at(java.util.Date updated_at) {
    	this.updated_at = updated_at;
    }
    
    public String toString(){
    	  return "编号："+id+" 实验编号："+experiment_id+" 实验名称："+experiment_name+" 预习链接："+prepare_link;
    }
}
