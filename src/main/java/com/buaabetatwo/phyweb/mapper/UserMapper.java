package com.buaabetatwo.phyweb.mapper;

import com.buaabetatwo.phyweb.model.User;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Result;
import org.apache.ibatis.annotations.Results;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface UserMapper {

    @Select("SELECT * from users")
    List<User> getAll();

    @Select("SELECT * FROM users WHERE id = #{id}")
    User getById(int id);

    @Select("SELECT * FROM users WHERE email=#{email}")
    User getByEmail(String email);

    @Select("SELECT * FROM users WHERE student_id=#{student_id}")
    User getByStudentId(String student_id);

    @Insert("INSERT INTO users(name, email, student_id, password) VALUES(#{name}, #{email}, #{student_id}, #{password})")
    void insertByUser(User user);

    @Insert("UPDATE  users SET name=#{name}  , email=#{email}   WHERE student_id=#{student_id}")
    void updateUserInfo(String name ,String email,String student_id );

    @Insert("UPDATE  users SET password=#{password} WHERE student_id=#{student_id}")
    void updateUserPw(String password,String student_id);

    @Update("UPDATE  users SET email=#{email} WHERE id=#{id}")
    void updateUserMail(String email, int id);


}
