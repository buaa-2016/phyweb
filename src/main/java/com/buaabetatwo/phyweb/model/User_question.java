package com.buaabetatwo.phyweb.model;

public class User_question {
    
    private int id;
    //private String name;
    private int question_id;
    
    public int getId() {
        return id;
    }
    
    public void setId(int id) {
        this.id = id;
    }

    /*public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }*/
    
    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                //", name='" + name + '\'' +
                ", question_id='" + question_id + '\'' +
                '}';
    }

    
    public int getQuestion_id() {
        return question_id;
    }
    
    public void setQuestion_id(int question_id) {
        this.question_id = question_id;
    }
}
