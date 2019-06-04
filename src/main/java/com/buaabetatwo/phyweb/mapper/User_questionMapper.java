package com.buaabetatwo.phyweb.mapper;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import com.buaabetatwo.phyweb.model.User_question;

public interface User_questionMapper {
    
    @Insert("insert into user_questions(id,question_id) values(#{id},#{question_id})")
    void insertByUser_question(User_question user_question);
    
    @Select("select * from user_questions where id = #{id}")
    User_question findById(int id);
    
    @Update("update user_questions set question_id=#{question_id} where id=#{id}")
    int updateuser_question(User_question user_question);
    
}
