﻿
var labDoc3dot1415926;
 
function lab(index){
	this.index = index;
	this.dbId = getDbId(index);
	this.xmlTxt;
	this.inputkind;
	this.flush = function(){
		var kinds = document.getElementsByName("check_"+index);
		var i;
		for(i = 0; i < kinds.length; i++) {
			if (kinds[i].checked) {
				break;
			}
		}
		this.inputkind = i+1;
		this.xmlTxt=SetXMLDoc_lab(index.toString()+this.inputkind);
	}
	this.getIndex = function(){
		return this.index;
	}
	this.getXML = function(){
		if(this.xmlTxt!=null)return this.xmlTxt;
	}
	this.getDbId = function(){
		return this.dbId;
	}
	this.getKind = function () {
		return this.inputkind;
	}
}
function getDbId(index){
	return $('#'+index +' a[index='+index+']').attr('db-id');
}
function check(){
	if(browser()=="FF"){
		document.getElementById('firefox_pdf').style.display='block';
	}
	else if(browser()=="IE6"||browser()=="IE7"){
		eleDisable();
		alert("Please use the above version of IE8 or other browsers");
	}
	else {
		document.getElementById('chrom_pdf').style.display='block';
		cp('./prepare_pdf/phylab_test.pdf');
	}
}	
function eleDisable(){
	SetDisable('importBtn',true);
	SetDisable('selectBtn',true);
	SetDisable('exportBtn',true);
	SetDisable('InputLabIndex',true);
}
function eleEnable(){
	SetDisable('importBtn',false);
	//SetDisable('collectBtn',false);
	SetDisable('exportBtn',true);
}
function collectLab(ico_id,txt_id){
	var ico = document.getElementById(ico_id);
	var txt = document.getElementById(txt_id);
	var check = txt.innerHTML;
		if(check=="取消收藏"){
			ico.setAttribute("class","glyphicon glyphicon-star-empty");
			txt.innerHTML = "收藏";
			alert("已取消收藏")
		}
		else if(check=="收藏"){
			ico.setAttribute("class","glyphicon glyphicon-star");
			txt.innerHTML = "取消收藏";
			alert("已添加至个人收藏夹！");
		}
		else
			alert("Button text can not be [txt] when use this function!Please Use 收藏/取消收藏");
}

function SelectLab(index,ref){
	var lt = document.getElementById(ref);
		if((new RegExp("^10(11|12|21|22|31|41|42|51|61|62|71|81|82|91)$")).test(index)){
			labDoc3dot1415926 = new lab(index);
			lt.innerHTML = index;
			return true;
		}
		else{
			return false;
		}
}
	
//USE jquery version 2.1.4, bootstrap.min.js
function inputCheck(){
	var a = $.merge($("input.para"),$("input.var"));
	for(var i = 0; i<a.length; i++) a[i].setAttribute("value",a[i].getAttribute("aria-label"));
}
function labIndexInput(){
	if(event.keyCode==13) {
		if(SelectLab($('#InputLabIndex')[0].value,'LabText')){
			$('.alert').hide();
			$('#LabStatus')[0].innerHTML = "预览";
			changePdf('prepare',labDoc3dot1415926.getIndex()+".pdf");
			eleEnable();
			return false;
		}
		else $('.alert').show();
		return false;
	}
	else return true;
}
function selectBtnClick(){
		if(SelectLab($('#InputLabIndex')[0].value,'LabText')){
			$('.alert').hide();
			$('#LabStatus')[0].innerHTML = "预览";
			changePdf('prepare',labDoc3dot1415926.getIndex()+".pdf");
			eleEnable();
		}
		else{
			$('.alert').show();
		}
}
function importBtnClick(){
	$("#lab_table_"+labDoc3dot1415926.getIndex()).modal("toggle");
}
function collectBtnClick(){
	collectLab('collectIco','collectText');
}
function exportBtnClick(){
	eleDisable();
	try{
		Post_lab();
	}catch(e){
		error();
	}
}

$('a.lab_title').bind('click',function(){
	//USE reportCore.js, bootstrap.min.js
	if($('#InputLabIndex').attr("disabled")=="disabled")return;
	if(SelectLab(this.title,'LabText')){
		$('.alert').hide();
		$('#LabStatus')[0].innerHTML = "预览";
		changePdf('prepare',labDoc3dot1415926.getIndex()+".pdf");
		eleEnable();
	}
	else $('.alert').show();
});
$('a.lab_index').bind('click',function(){
	//USE reportCore.js, bootstrap.min.js
	if($('#InputLabIndex').attr("disabled")=="disabled")return;
	if(SelectLab(this.innerHTML,'LabText')){
		$('.alert').hide();
		$('#LabStatus')[0].innerHTML = "预览";
		changePdf('prepare',labDoc3dot1415926.getIndex()+".pdf");
		eleEnable();
	}
	else $('.alert').show();
});
$('input.para').bind('keyup',function(){
	if((new RegExp("^\\d+(.\\d+)?$")).test(this.value)==false) $(this).addClass("wrong-input");
	else $(this).removeClass("wrong-input")
})
$('input.var').bind('keyup',function(){
	if((new RegExp("(^\\d+(.\\d+)?$)|(^$)")).test(this.value)==false) $(this).addClass("wrong-input");
	else $(this).removeClass("wrong-input")
})	
$('button.btn-Save').bind('click',function(){
	var index = labDoc3dot1415926.getIndex();
	var paraArray,varArray;
	var labStr = "", wrong_count = 0, i = 1, ErrType = 1;
	while((tp=document.getElementById("check_"+index+"_"+i))!=null){
		if(tp.checked)labStr += "input.para"+"."+index+"_"+i+",";
		i++;
	}
	//get selected sublab
	labStr = labStr.substring(0,labStr.lastIndexOf(','));
	paraArray = $(labStr);
	labStr = labStr.replace(new RegExp("para","gm"),"var");
	varArray = $(labStr);
	//get data form input, para can't be null
	paraArray.each(function(){
		if($(this).hasClass("wrong-input")) wrong_count++;
		else if(this.value==""){
			wrong_count++;
			$(this).addClass("wrong-input");
		}
		//else if((new RegExp("(^\\d+(.\\d+)?$)")).test(this.value)==false){error();return false;}
	})
	varArray.each(function(){
		if($(this).hasClass("wrong-input")) wrong_count++;
		//else if((new RegExp("(^\\d+(.\\d+)?$)|(^$)")).test(this.value)==false){error();return false;}
	})
	//check data
	if(wrong_count==0){
		$("#lab_table_"+index).modal('toggle');
		if(labStr!=""){
			SetDisable('exportBtn',false);
			labDoc3dot1415926.flush();
		}//when no selected sublab exist, just close modal
	}
	else{
		document.getElementById("ErrorText_"+index).innerHTML = "有"+wrong_count+"处输入不合法，请检查标红输入框";
		setShowHide("btnError_"+index,"btnSave_"+index,5000);
	}
})	


// //USE pdfObject v1.2.20111123, xmlInteraction
function changePdf(type,pdfName){
		var path = ""
		if(type=="prepare"){
			path = "./prepare_pdf/";
		}
		else if(type=="tmp"){
			path = "./";
		}
		else if(type=="star"){
			path = "./star_pdf/"
		}
		console.log("changePdf(), uri:" + path + pdfName);
		PDFObject.embed(path + pdf, "#pdf-object");
}

function Post_lab(){
	var xmlString = labDoc3dot1415926.getXML();
	var dbId = labDoc3dot1415926.getDbId();
	var kind = labDoc3dot1415926.getKind();
	PostXMLDoc("/report",xmlString,dbId,kind,function(){
		if (this.readyState==4 && this.status==200){
			var jsonText = eval("(" + this.responseText + ")");
			//alert(this.responseText);
			//alert(jsonText["status"]);
			if(jsonText["status"]=='success'){
				changePdf('tmp',jsonText['link']);
				$('#LabStatus')[0].innerHTML = "终版";
				eleEnable();
			} else {
				alert("要请检查数据～")
			}
		} else if (this.readyState==4) {
			console.log("服务器出错");
			console.log(this.readyState);
			console.log(this.status);
			alert("服务器出错");
		} else {
			alert("要检查数据哦～");
		}
	});
}
$(document).ready(function() {
	PDFObject.embed("./prepare_pdf/物理实验选择策略.pdf", "#pdf-object");
})


$(".view-pdf").click(function() {
	let pdf = $(this).parent().data("prepare-pdf");
	PDFObject.embed("./prepare_pdf/" + pdf, "#pdf-object");
})