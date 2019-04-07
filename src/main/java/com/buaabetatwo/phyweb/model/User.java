package com.buaabetatwo.phyweb.model;


import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.io.Serializable;


@Getter
@Setter
@ToString
public class User {

    private int id;
    private String name;
    private String email;
    private String student_id;
    private String password;

}