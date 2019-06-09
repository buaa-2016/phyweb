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

	function changeComment(){

		var params = {
			"content_id": document.getElementById("commentUpdate_1").value,
			"comment_co": document.getElementById("commentUpdate_2").value,
			"id":document.getElementById("questionId").textContent
		};

		httpPost("/comment_1", params);
	}
	
	function judgeAnswerQuestion() {
		$('div#answer').collapse('show');
	}

	function judgeBlankQuestion() {
		const ans = $('input#blank_answer').val().replace(' ', '');
		if (ans === questionDetail.answer) {
			$('div#answer-correct').collapse('show');
		} else {
			$('div#answer-incorrect').collapse('show');
		}
	}

	function insertQuestion() {
		var params = {
			"id":document.getElementById("questionId").textContent
		};

		httpPost("/editQuestionDetail",params)
	}

	function judgeChoiceQuestion() {
		var ans = document.getElementById("questionAns").textContent;
		//获取ans的值
		if(ans == 'A') document.getElementById("chooseA").style.backgroundColor="#21ba45";
		else if(ans == 'B') document.getElementById("chooseB").style.backgroundColor="#21ba45";
		else if(ans == 'C') document.getElementById("chooseC").style.backgroundColor="#21ba45";
		else if(ans == 'D') document.getElementById("chooseD").style.backgroundColor="#21ba45";

		if (document.getElementById("A").checked == true && ans != 'A') {
			document.getElementById("chooseA").style.backgroundColor="#f2711c";
		} else if (document.getElementById("B").checked == true && ans != 'B') {
			document.getElementById("chooseB").style.backgroundColor="#f2711c";
		} else if (document.getElementById("C").checked == true && ans != 'C') {
			document.getElementById("chooseC").style.backgroundColor="#f2711c";
		} else if (document.getElementById("D").checked == true && ans != 'D') {
			document.getElementById("chooseD").style.backgroundColor="#f2711c";
		}
	}

	function judgeAns() {
		switch (questionDetail.type) {
			case 'BLANK': judgeBlankQuestion(); break;
			case 'CHOICE': judgeChoiceQuestion(); break;
			case 'ANSWER': judgeAnswerQuestion(); break;
			default: console.log("error"); break;
		}
		return;
	}


	$(document).ready(function(){
		$("#passwordButton").click(function(){
			$("#messageDiv").hide();
			$("#passwordDiv").show();
		});

		$("#messageButton").click(function(){
			$("#messageDiv").show();
			$("#passwordDiv").hide();
		});
	});
	function check(input) {
		if (input.value != document.getElementById('newPassword1').value) {
			input.setCustomValidity('两次输入的密码必须一致');
		} else {
			// input is valid -- reset the error message
			input.setCustomValidity('');
		}
	}



	$(function () {
		//点击发送验证码
		$('body').on('click', '#btnSend', function () {
			$('body').off('click', '#btnSend');
			var form= document.getElementById("myForm");
			form.submit();
			LockButton('#btnSend', 60);
		})

		//读取cookie
		if ($.cookie("djsendtime") != undefined && !isNaN($.cookie("djsendtime"))) {  //读取到了cookie值
			var djsendtime = $.cookie("djsendtime");
			var now = new Date().getTime();  //当前时间戳
			var locksecends = parseInt((djsendtime - now) / 1000);
			if (locksecends <= 0) {
				$.cookie("djsendtime", null);
			} else {
				LockButton('#btnSend', locksecends);
			}
		}

	})

	// 按钮倒计时
	var LockButton = function (btnObjId, locksecends) {
		//1.获取当前系统时间
		//2.获取 locksecends 后的系统时间
		//3.用cookie保存到期时间
		//4.每次加载后获取cookie中保存的时间
		//5.用到期时间减去当前时间获取倒计时
		var djsendtime = $.cookie("djsendtime");
		if (djsendtime == null || djsendtime == undefined || djsendtime == 'undefined' || djsendtime == 'null') {
			var now = new Date().getTime();  //当前时间戳
			var endtime = locksecends * 1000 + now;  //结束时间戳
			$.cookie("djsendtime", endtime);  //将结束时间保存到cookie
		}
		$(btnObjId).addClass('disabled').attr('disabled', 'disabled').text('(' + locksecends + ')秒后重新获取');
		$('body').off('click', '#btnSendSMS');
		var timer = setInterval(function () {
			locksecends--;
			$(btnObjId).text('(' + locksecends + ')秒后重新获取');
			if (locksecends <= 0) {
				//倒计时结束清除cookie值
				$.cookie("djsendtime", null);
				$(btnObjId).removeClass('disabled').removeAttr('disabled').text('重新获取');
				$('body').on('click', '#btnSend', function () {
					$('body').off('click', '#btnSend');
					LockButton('#btnSend', 60);
				})
				clearInterval(timer);
			}
		}, 1000);
	};