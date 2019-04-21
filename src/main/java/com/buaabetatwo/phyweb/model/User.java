package com.buaabetatwo.phyweb.model;

import com.buaabetatwo.phyweb.util.GenderEnum;

import java.sql.Timestamp;


public class User {

    private int id;
    private String name;
    private String email;
    private String student_id;
    private String password;

    private String introduction;
    private Timestamp created_at;
    private String company;
    private GenderEnum sex;
    
    public int getId() {
        return id;
    }

    public Timestamp getCreated_at() {
        return created_at;
    }

    public void setCreated_at(Timestamp created_at) {
        this.created_at = created_at;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public String getIntroduction() {
        return introduction;
    }

    public void setIntroduction(String introduction) {
        this.introduction = introduction;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getStudent_id() {
        return student_id;
    }

    public void setStudent_id(String student_id) {
        this.student_id = student_id;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public GenderEnum getSex() {
        return sex;
    }

    public void setSex(GenderEnum sex) {
        this.sex = sex;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", student_id='" + student_id + '\'' +
                ", password='" + password + '\'' +
                ", introduction='" + introduction + '\'' +
                ", created_at=" + created_at +
                ", company='" + company + '\'' +
                ", sex='" + sex + '\'' +
                '}';
    }
}