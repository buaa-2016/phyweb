package com.buaabetatwo.phyweb.mapper;

import com.buaabetatwo.phyweb.model.Comment;

import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

public interface CommentMapper {
    
    @Insert("insert into comments(id,name,content) values(#{id},#{name},#{content})")
    void insertByComment(Comment comment);
    
    @Update("update comments set content=#{content} where id=#{id} and content_id=#{content_id}")
    int changecomment(Comment comment);
    
    @Delete("delete from comments where id=#{id} and content_id=#{content_id}")
    int delete(int id,int content_id);
    
    /*@Select("select * from comments where id = #{id}")
    Comment findById(int id);*/
    
    @Select("select * from comments where id = #{id}")
    List<Comment> findAllById(int id);
    
}
