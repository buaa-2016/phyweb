package com.buaabetatwo.phyweb.mapper;

import com.buaabetatwo.phyweb.model.User;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import java.util.List;

public interface UserMapper {

    @Select("SELECT * from users")
    List<User> getAll();

    @Select("SELECT * FROM users WHERE id = #{id}")
    User getById(int id);

    @Select("SELECT * FROM users WHERE email=#{email}")
    User getByEamil(String email);
}
