package com.buaabetatwo.phyweb.mapper;

import com.buaabetatwo.phyweb.model.Role;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;


@Mapper
public interface RoleMapper {

    @Select("select * from role where userName = #{userName}")
    Role getRoleByName(@Param("userName") String userName);

}
