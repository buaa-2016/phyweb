package com.buaabetatwo.phyweb.mapper;

import com.buaabetatwo.phyweb.model.Question;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface QuestionUploadMapper {

    @Select("select * from question_upload where id = #{id}")
    Question findById(int id);

    @Select("select * from question_upload")
    List<Question> findAll();

    @Insert("insert into question_upload(title,A,B,C,D,answer,source,tag,other,hint,type) " +
            "values(#{title},#{A},#{B},#{C},#{D},#{answer},#{source},#{tag},#{other},#{hint},#{type})")
    void insertQuestion(Question question);

}
