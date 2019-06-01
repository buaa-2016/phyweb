package com.buaabetatwo.phyweb.mapper;

import com.buaabetatwo.phyweb.model.Question;
import com.buaabetatwo.phyweb.model.Report;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface QuestionMapper {

    @Select("select * from questions where id = #{id}")
    Question findById(int id);

    @Select("select * from questions")
    List<Question> findAll();

    @Insert("insert into questions(title,A,B,C,D,answer,source,tag,other,hint,type) " +
            "values(#{title},#{A},#{B},#{C},#{D},#{answer},#{source},#{tag},#{other},#{hint},#{type})")
    void insertQuestion(Question question);

}
