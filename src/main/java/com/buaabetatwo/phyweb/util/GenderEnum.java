package com.buaabetatwo.phyweb.util;

public enum GenderEnum {

    male("男"),
    female("女"),
    secret("秘密");

    private String value;
    GenderEnum(String value) {
        this.value = value;
    }
    public String getValue() {
        return value;
    }
}
