package com.buaabetatwo.phyweb.model;

import java.sql.Timestamp;

public class Comment {
    private int id;
    private String name;
    private Timestamp time;
    private String content;
    private int content_id;
    
    public int getId() {
        return id;
    }
    
    public int getContent_id() {
        return content_id;
    }
        
    public Timestamp getTime() {
        return time;
    }
    
    public void setTime(Timestamp time) {
        this.time = time;
    }
    
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    
    public void setId(int id) {
        this.id = id;
    }
    
    public void setContent_id(int content_id) {
        this.content_id = content_id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    @Override
    public String toString() {
        return "Comment{" +
                "content_id=" + content_id +
                ", id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", time='" + time + '\'' +
                ", content='" + content + '\'' +
                '}';
    }
}
