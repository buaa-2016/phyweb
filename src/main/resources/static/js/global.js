	function browser(){
		var userAgent = navigator.userAgent; 
		var isOpera = userAgent.indexOf("Opera") > -1;
		var browser_name=navigator.appName
		var b_version=navigator.appVersion
		var version=b_version.split(";");
		var trim_Version=version.length>1?version[1].replace(/[ ]/g,""):"UPON"; 
		if (isOpera) {
		return "Opera"
		}
		else if (userAgent.indexOf("Firefox") > -1) {
		return "FF";
		}
		else if (userAgent.indexOf("Chrome") > -1){
		return "Chrome";
		}
		else if (userAgent.indexOf("Safari") > -1) {
		return "Safari";
		}
		else if(browser_name=="Microsoft Internet Explorer"){
			if (trim_Version=="MSIE6.0") {
				return "IE6"; 
			} else if (trim_Version=="MSIE7.0") {
				return "IE7";
			} else if (trim_Version=="MSIE8.0") {
				return "IE8";
			} else {
				return "IE9+";
			}
		}
	}
	
	function SetDisable(index,if_disable){
		var item = document.getElementById(index);
		if(if_disable)
			item.setAttribute("disabled","disabled");
		else
			item.removeAttribute("disabled")
	}
	
	function setShowHide(show_index,hide_index,time_offset){
		var show_item = document.getElementById(show_index);
		var hide_item = document.getElementById(hide_index);
		show_item.style.display = "block";
		hide_item.style.display = "none";
		if(time_offset<0)return;
		else setTimeout(_setShowHide(hide_index,show_index),time_offset);
	}
	function _setShowHide(show_index,hide_index){
		return function(){
			setShowHide(show_index,hide_index,-1)
		}
	}
	
	function error(){
		alert("你是不是做坏事了");
		alert("崩溃了哦");
		alert("滚吧！");
		window.location = "http://www.taobao.com/"
	}


	function httpPost(URL, PARAMS) {
		var temp = document.createElement("form");
		temp.action = URL;
		temp.method = "post";
		temp.style.display = "none";

		for (var x in PARAMS) {
			var opt = document.createElement("textarea");
			opt.name = x;
			opt.value = PARAMS[x];
			temp.appendChild(opt);
		}

		document.body.appendChild(temp);
		temp.submit();

		return temp;
	}

	function insertComment(){

		var params = {
			"comment": document.getElementById("commentInput").value,
			"id":document.getElementById("questionId").textContent
		};

		httpPost("/comment", params);
	}

