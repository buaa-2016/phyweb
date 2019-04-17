package com.buaabetatwo.phyweb.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;
import com.buaabetatwo.phyweb.model.Report;

@Mapper
public interface ReportMapper {
	
	@Select("select id,experiment_id,experiment_name,prepare_link from reports")
	List<Report> findlist();
	
	@Select("select * from reports")
	List<Report> findAll();
 
	@Select("select * from reports where id = #{id}")
	Report findById(@Param("id") int id);
	
	@Insert("insert into reports(id,script_link,experiment_id,experiment_name,prepare_link,created_at,updated_at) values(#{id},#{script_link},#{experiment_id},#{experiment_name},#{prepare_link},#{created_at},#{updated_at})")
	void insertByReport(Report report);
 
	@Update("update reports set updated_at=#{updated_at} where id=#{id}")
	int update(Report report);
 
	@Delete("delete from reports where id=#{id}")
	int delete(int id);
}
