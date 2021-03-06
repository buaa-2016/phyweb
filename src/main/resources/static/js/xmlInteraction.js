
function PostXMLDoc(url,xmlString,id,kind,cfunc){
	var xmlhttp;
		if (window.XMLHttpRequest)
		  {// code for IE7+, Firefox, Chrome, Opera, Safari
		  xmlhttp=new XMLHttpRequest();
		  }
		else
		  {// code for IE6, IE5
		  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
		  }
	xmlhttp.onreadystatechange=cfunc;
	xmlhttp.open("POST",url,true);
	xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
	xmlhttp.send("xml="+encodeURI(xmlString)+"&id="+id+"&kind="+kind);
}

function SetXMLDoc_lab(labnum){
	var str = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n";
	switch(labnum){
		case "10111":
			str += "<lab id=\"1010113\">\n"+
				"<table name=\"10111_1\" raw=\"1\" column=\"3\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1011_1_L').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_H').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_b').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1011_1_D1').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_D2').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_D3').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_D4').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_D5').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_D6').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('1011_1_m1').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_m2').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_m3').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_m4').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_m5').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_m6').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_m7').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_m8').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('1011_1_jia10').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jia12').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jia14').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jia16').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jia18').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jia20').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jia22').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jia24').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"5\">\n"+
				"<td>"+document.getElementById('1011_1_jian10').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jian12').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jian14').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jian16').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jian18').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jian20').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jian22').value+"</td>\n"+
				"<td>"+document.getElementById('1011_1_jian24').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;
	case "10112":
		str += "<lab id=\"1010212\">\n"+
			"<table name=\"10112_1\" raw=\"3\" column=\"4\">\n"+
			"<tr index=\"1\">\n"+
			"<td>"+document.getElementById('1011_2_myuanzhu').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_myuantong').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_mqiu').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_mxigan').value+"</td>\n"+
			"</tr>\n"+
			"<tr index=\"2\">\n"+
			"<td>"+document.getElementById('1011_2_chicunyuanzhu').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_wchicunmyuantong').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_nchicunyuantong').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_chicunqiu').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_chicunxigan').value+"</td>\n"+
			"</tr>\n"+
			"<tr index=\"3\">\n"+
			"</tr>\n"+
			"</table>\n"+
			"<table name=\"10112_2\" raw=\"5\" column=\"5\">\n"+
			"<tr index=\"1\">\n"+
			"<td>"+document.getElementById('1011_2_w1').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_w2').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_w3').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_w4').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_w5').value+"</td>\n"+
			"</tr>\n"+
			"<tr index=\"2\">\n"+
			"<td>"+document.getElementById('1011_2_pz1').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pz2').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pz3').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pz4').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pz5').value+"</td>\n"+
			"</tr>\n"+
			"<tr index=\"3\">\n"+
			"<td>"+document.getElementById('1011_2_pt1').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pt2').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pt3').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pt4').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_pt5').value+"</td>\n"+
			"</tr>\n"+
			"<tr index=\"4\">\n"+
			"<td>"+document.getElementById('1011_2_yq1').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_yq2').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_yq3').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_yq4').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_yq5').value+"</td>\n"+
			"</tr>\n"+
			"<tr index=\"5\">\n"+
			"<td>"+document.getElementById('1011_2_xcg1').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_xcg2').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_xcg3').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_xcg4').value+"</td>\n"+
			"<td>"+document.getElementById('1011_2_xcg5').value+"</td>\n"+
			"</tr>\n"+
			"</table>\n"+
			"</lab>";
			return str;

		case "10211":
			str += "<lab id=\"1020113\">\n"+
				"<table name=\"10211_1\" raw=\"1\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('mTong').value+"</td>\n"+
				"<td>"+document.getElementById('mBang').value+"</td>\n"+
				"<td>"+document.getElementById('mTongBang').value+"</td>\n"+
				"<td>"+document.getElementById('tAround1').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10211_2\" raw=\"20\" column=\"3\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('f60-1').value+"</td>\n"+
				"<td>"+document.getElementById('a15-1').value+"</td>\n"+
				"<td>"+document.getElementById('a60-1').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('f60-2').value+"</td>\n"+
				"<td>"+document.getElementById('a15-2').value+"</td>\n"+
				"<td>"+document.getElementById('a60-2').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('f60-3').value+"</td>\n"+
				"<td>"+document.getElementById('a15-3').value+"</td>\n"+
				"<td>"+document.getElementById('a60-3').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('f60-4').value+"</td>\n"+
				"<td>"+document.getElementById('a15-4').value+"</td>\n"+
				"<td>"+document.getElementById('a60-4').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"5\">\n"+
				"<td>"+document.getElementById('f60-5').value+"</td>\n"+
				"<td>"+document.getElementById('a15-5').value+"</td>\n"+
				"<td>"+document.getElementById('a60-5').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"6\">\n"+
				"<td>"+document.getElementById('f60-6').value+"</td>\n"+
				"<td>"+document.getElementById('a15-6').value+"</td>\n"+
				"<td>"+document.getElementById('a60-6').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"7\">\n"+
				"<td>"+document.getElementById('f60-7').value+"</td>\n"+
				"<td>"+document.getElementById('a15-7').value+"</td>\n"+
				"<td>"+document.getElementById('a60-7').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"8\">\n"+
				"<td>"+document.getElementById('f60-8').value+"</td>\n"+
				"<td>"+document.getElementById('a15-8').value+"</td>\n"+
				"<td>"+document.getElementById('a60-8').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"9\">\n"+
				"<td>"+document.getElementById('f60-9').value+"</td>\n"+
				"<td>"+document.getElementById('a15-9').value+"</td>\n"+
				"<td>"+document.getElementById('a60-9').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"10\">\n"+
				"<td>"+document.getElementById('f60-10').value+"</td>"+
				"<td>"+document.getElementById('a15-10').value+"</td>\n"+
				"<td>"+document.getElementById('a60-10').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"11\">\n"+
				"<td>"+document.getElementById('f60-11').value+"</td>"+
				"<td>"+document.getElementById('a15-11').value+"</td>\n"+
				"<td>"+document.getElementById('a60-11').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"12\">\n"+
				"<td>"+document.getElementById('f60-12').value+"</td>"+
				"<td>"+document.getElementById('a15-12').value+"</td>\n"+
				"<td>"+document.getElementById('a60-12').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"13\">\n"+
				"<td>"+document.getElementById('f60-13').value+"</td>"+
				"<td>"+document.getElementById('a15-13').value+"</td>\n"+
				"<td>"+document.getElementById('a60-13').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"14\">\n"+
				"<td>"+document.getElementById('f60-14').value+"</td>"+
				"<td>"+document.getElementById('a15-14').value+"</td>\n"+
				"<td>"+document.getElementById('a60-14').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"15\">\n"+
				"<td>"+document.getElementById('f60-15').value+"</td>"+
				"<td>"+document.getElementById('a15-15').value+"</td>\n"+
				"<td>"+document.getElementById('a60-15').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"16\">\n"+
				"<td>"+document.getElementById('f60-16').value+"</td>"+
				"<td>"+document.getElementById('a15-16').value+"</td>\n"+
				"<td>"+document.getElementById('a60-16').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"17\">\n"+
				"<td>"+document.getElementById('f60-17').value+"</td>"+
				"<td>"+document.getElementById('a15-17').value+"</td>\n"+
				"<td>"+document.getElementById('a60-17').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"18\">\n"+
				"<td>"+document.getElementById('f60-18').value+"</td>"+
				"<td>"+document.getElementById('a15-18').value+"</td>\n"+
				"<td>"+document.getElementById('a60-18').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"19\">\n"+
				"<td>"+document.getElementById('f60-19').value+"</td>"+
				"<td>"+document.getElementById('a15-19').value+"</td>\n"+
				"<td>"+document.getElementById('a60-19').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"20\">\n"+
				"<td>"+document.getElementById('f60-20').value+"</td>"+
				"<td>"+document.getElementById('a15-20').value+"</td>\n"+
				"<td>"+document.getElementById('a60-20').value+"</td>\n"+
				"</tr>"+
				"</table>\n"+
				"</lab>";
			return str;
		case "10212":
			str += "<lab id=\"1020212\">\n"+
				"<table name=\"10212_1\" raw=\"1\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('mNeitong').value+"</td>\n"+
				"<td>"+document.getElementById('mTotal').value+"</td>\n"+
				"<td>"+document.getElementById('v1').value+"</td>\n"+
				"<td>"+document.getElementById('v2').value+"</td>\n"+
				"<td>"+document.getElementById('tAround2').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10212_2\" raw=\"31\" column=\"1\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('r0').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('r1').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('r2').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('r3').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"5\">\n"+
				"<td>"+document.getElementById('r4').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"6\">\n"+
				"<td>"+document.getElementById('r5').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"7\">\n"+
				"<td>"+document.getElementById('r6').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"8\">\n"+
				"<td>"+document.getElementById('r7').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"9\">\n"+
				"<td>"+document.getElementById('r8').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"10\">\n"+
				"<td>"+document.getElementById('r9').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"11\">\n"+
				"<td>"+document.getElementById('r10').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"12\">\n"+
				"<td>"+document.getElementById('r11').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"13\">\n"+
				"<td>"+document.getElementById('r12').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"14\">\n"+
				"<td>"+document.getElementById('r13').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"15\">\n"+
				"<td>"+document.getElementById('r14').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"16\">\n"+
				"<td>"+document.getElementById('r15').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"17\">\n"+
				"<td>"+document.getElementById('r16').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"18\">\n"+
				"<td>"+document.getElementById('r17').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"19\">\n"+
				"<td>"+document.getElementById('r18').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"20\">\n"+
				"<td>"+document.getElementById('r19').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"21\">\n"+
				"<td>"+document.getElementById('r20').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"22\">\n"+
				"<td>"+document.getElementById('r21').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"23\">\n"+
				"<td>"+document.getElementById('r22').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"24\">\n"+
				"<td>"+document.getElementById('r23').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"25\">\n"+
				"<td>"+document.getElementById('r24').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"26\">\n"+
				"<td>"+document.getElementById('r25').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"27\">\n"+
				"<td>"+document.getElementById('r26').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"28\">\n"+
				"<td>"+document.getElementById('r27').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"29\">\n"+
				"<td>"+document.getElementById('r28').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"30\">\n"+
				"<td>"+document.getElementById('r29').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"31\">\n"+
				"<td>"+document.getElementById('r30').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;

		case "10311":
			str += "<lab id=\"1030113\">\n"+
				"<table name=\"10311_1\" raw=\"6\" column=\"3\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('chjiao1').value+"</td>\n"+
				"<td>"+document.getElementById('chzhong1').value+"</td>\n"+
				"<td>"+document.getElementById('chni1').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('yjiao1').value+"</td>\n"+
				"<td>"+document.getElementById('yzhong1').value+"</td>\n"+
				"<td>"+document.getElementById('yni1').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('chjiao2').value+"</td>\n"+
				"<td>"+document.getElementById('chzhong2').value+"</td>\n"+
				"<td>"+document.getElementById('chni2').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('yjiao2').value+"</td>\n"+
				"<td>"+document.getElementById('yzhong2').value+"</td>\n"+
				"<td>"+document.getElementById('yni2').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"5\">\n"+
				"<td>"+document.getElementById('chjiao3').value+"</td>\n"+
				"<td>"+document.getElementById('chzhong3').value+"</td>\n"+
				"<td>"+document.getElementById('chni3').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"6\">\n"+
				"<td>"+document.getElementById('yjiao3').value+"</td>\n"+
				"<td>"+document.getElementById('yzhong3').value+"</td>\n"+
				"<td>"+document.getElementById('yni3').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10311_2\" raw=\"2\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('f2').value+"</td>\n"+
				"<td>"+document.getElementById('y_1031_1').value+"</td>\n"+
				"<td>"+document.getElementById('v_1031_1').value+"</td>\n"+
				"<td>"+document.getElementById('t_1031_1').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('f4').value+"</td>\n"+
				"<td>"+document.getElementById('y_1031_2').value+"</td>\n"+
				"<td>"+document.getElementById('v_1031_2').value+"</td>\n"+
				"<td>"+document.getElementById('t_1031_2').value+"</td>\n"+
				"</tr>"+
				"</table>\n"+
				"<table name=\"10311_3\" raw=\"4\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('fy1').value+"</td>\n"+
				"<td>"+document.getElementById('fy2').value+"</td>\n"+
				"<td>"+document.getElementById('fy3').value+"</td>\n"+
				"<td>"+document.getElementById('fy4').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('fyfx1').value+"</td>\n"+
				"<td>"+document.getElementById('fyfx2').value+"</td>\n"+
				"<td>"+document.getElementById('fyfx3').value+"</td>\n"+
				"<td>"+document.getElementById('fyfx4').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('nx1').value+"</td>\n"+
				"<td>"+document.getElementById('nx2').value+"</td>\n"+
				"<td>"+document.getElementById('nx3').value+"</td>\n"+
				"<td>"+document.getElementById('nx4').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('ny1').value+"</td>\n"+
				"<td>"+document.getElementById('ny2').value+"</td>\n"+
				"<td>"+document.getElementById('ny3').value+"</td>\n"+
				"<td>"+document.getElementById('ny4').value+"</td>\n"+
				"</tr>"+
				"</table>\n"+
				"</lab>";
			return str;

		case "10611":
			str += "<lab id=\"1060111\">\n"+
				"<table name=\"10611_1\" raw=\"9\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('wt1_guangyuan1').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_guangping1').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_tutoujing11').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_tutoujing21').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('wt1_guangyuan2').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_guangping2').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_tutoujing12').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_tutoujing22').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('wt1_guangyuan3').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_guangping3').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_tutoujing13').value+"</td>\n"+
				"<td>"+document.getElementById('wt1_tutoujing23').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('wt2_guangyuan1').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_guangping1').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_tutoujing11').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_tutoujing21').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"5\">\n"+
				"<td>"+document.getElementById('wt2_guangyuan2').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_guangping2').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_tutoujing12').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_tutoujing22').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"6\">\n"+
				"<td>"+document.getElementById('wt2_guangyuan3').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_guangping3').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_tutoujing13').value+"</td>\n"+
				"<td>"+document.getElementById('wt2_tutoujing23').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"7\">\n"+
				"<td>"+document.getElementById('wt3_guangyuan1').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_guangping1').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_tutoujing11').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_tutoujing21').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"8\">\n"+
				"<td>"+document.getElementById('wt3_guangyuan2').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_guangping2').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_tutoujing12').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_tutoujing22').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"9\">\n"+
				"<td>"+document.getElementById('wt3_guangyuan3').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_guangping3').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_tutoujing13').value+"</td>\n"+
				"<td>"+document.getElementById('wt3_tutoujing23').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10611_2\" raw=\"3\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('wa_guangyuan1').value+"</td>\n"+
				"<td>"+document.getElementById('wa_tutoujing11').value+"</td>\n"+
				"<td>"+document.getElementById('wa_tutoujing21').value+"</td>\n"+
				"<td>"+document.getElementById('wa_guangping1').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('wa_guangping2').value+"</td>\n"+
				"<td>"+document.getElementById('wa_tutoujing12').value+"</td>\n"+
				"<td>"+document.getElementById('wa_tutoujing22').value+"</td>\n"+
				"<td>"+document.getElementById('wa_guangyuan2').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('wa_guangping3').value+"</td>\n"+
				"<td>"+document.getElementById('wa_tutoujing13').value+"</td>\n"+
				"<td>"+document.getElementById('wa_tutoujing23').value+"</td>\n"+
				"<td>"+document.getElementById('wa_guangyuan3').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;

		case "10612":
			str += "<lab id=\"1060213\">\n"+
				"<table name=\"10612_1\" raw=\"5\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('z_guangyuan1').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing11').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing21').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('z_guangyuan2').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing12').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing22').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('z_guangyuan3').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing13').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing23').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('z_guangyuan4').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing14').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing24').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"5\">\n"+
				"<td>"+document.getElementById('z_guangyuan5').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing15').value+"</td>\n"+
				"<td>"+document.getElementById('z_tutoujing25').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;
	case "10711":
		str += "<lab id=\"1070212\">\n"+
			"<table name=\"10711_1\" raw=\"5\" column=\"4\">\n"+
			"<tr index=\"1\">\n"+
			"<td>"+document.getElementById('a11').value+"</td>\n"+
			"<td>"+document.getElementById('a21').value+"</td>\n"+
			"<td>"+document.getElementById('b11').value+"</td>\n"+
			"<td>"+document.getElementById('b21').value+"</td>\n"+
			"</tr>"+
			"<tr index=\"2\">\n"+
			"<td>"+document.getElementById('a12').value+"</td>\n"+
			"<td>"+document.getElementById('a22').value+"</td>\n"+
			"<td>"+document.getElementById('b12').value+"</td>\n"+
			"<td>"+document.getElementById('b22').value+"</td>\n"+
			"</tr>"+
			"<tr index=\"3\">\n"+
			"<td>"+document.getElementById('a13').value+"</td>\n"+
			"<td>"+document.getElementById('a23').value+"</td>\n"+
			"<td>"+document.getElementById('b13').value+"</td>\n"+
			"<td>"+document.getElementById('b23').value+"</td>\n"+
			"</tr>"+
			"<tr index=\"4\">\n"+
			"<td>"+document.getElementById('a14').value+"</td>\n"+
			"<td>"+document.getElementById('a24').value+"</td>\n"+
			"<td>"+document.getElementById('b14').value+"</td>\n"+
			"<td>"+document.getElementById('b24').value+"</td>\n"+
			"</tr>"+
			"<tr index=\"5\">\n"+
			"<td>"+document.getElementById('a15').value+"</td>\n"+
			"<td>"+document.getElementById('a25').value+"</td>\n"+
			"<td>"+document.getElementById('b15').value+"</td>\n"+
			"<td>"+document.getElementById('b25').value+"</td>\n"+
			"</tr>"+
			"</table>\n"+
			"</lab>";
		return str;

		case "10712":
			str += "<lab id=\"1070312\">\n"+
				"<table name=\"10712_1\" raw=\"5\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('ra11').value+"</td>\n"+
				"<td>"+document.getElementById('rb11').value+"</td>\n"+
				"<td>"+document.getElementById('ra21').value+"</td>\n"+
				"<td>"+document.getElementById('rb21').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('ra12').value+"</td>\n"+
				"<td>"+document.getElementById('rb12').value+"</td>\n"+
				"<td>"+document.getElementById('ra22').value+"</td>\n"+
				"<td>"+document.getElementById('rb22').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('ra13').value+"</td>\n"+
				"<td>"+document.getElementById('rb13').value+"</td>\n"+
				"<td>"+document.getElementById('ra23').value+"</td>\n"+
				"<td>"+document.getElementById('rb23').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('ra14').value+"</td>\n"+
				"<td>"+document.getElementById('rb14').value+"</td>\n"+
				"<td>"+document.getElementById('ra24').value+"</td>\n"+
				"<td>"+document.getElementById('rb24').value+"</td>\n"+
				"</tr>"+
				"<tr index=\"5\">\n"+
				"<td>"+document.getElementById('ra15').value+"</td>\n"+
				"<td>"+document.getElementById('rb15').value+"</td>\n"+
				"<td>"+document.getElementById('ra25').value+"</td>\n"+
				"<td>"+document.getElementById('rb25').value+"</td>\n"+
				"</tr>"+
				"</table>\n"+
				"<table name=\"10712_2\">"+
				"<tr index=\"1\">"+
				"<td>"+document.getElementById('1070312_A').value+"</td>"+
				"<td>"+document.getElementById('1070312_uA').value+"</td>"+
				"<td>"+document.getElementById('1071_A').value+"</td>"+
				"<td>"+document.getElementById('1071_uA').value+"</td>"+
				"</tr>"+
				"</table>"+
				"</lab>";
			return str;

		case "10811":
			str += "<lab id=\"1080114\">\n"+
				"<table name=\"10811_1\" raw=\"1\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1081_kuoshu').value+"</td>\n"+
				"<td>"+document.getElementById('1081_shuangleng').value+"</td>\n"+
				"<td>"+document.getElementById('1081_guangyuan').value+"</td>\n"+
				"<td>"+document.getElementById('1081_xiaoxiang').value+"</td>\n"+
				"<td>"+document.getElementById('1081_daxiang').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10811_2\" raw=\"2\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1081_dzuo1').value+"</td>\n"+
				"<td>"+document.getElementById('1081_dyou1').value+"</td>\n"+
				"<td>"+document.getElementById('1081_dzuo2').value+"</td>\n"+
				"<td>"+document.getElementById('1081_dyou2').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1081_xzuo1').value+"</td>\n"+
				"<td>"+document.getElementById('1081_xyou1').value+"</td>\n"+
				"<td>"+document.getElementById('1081_xzuo2').value+"</td>\n"+
				"<td>"+document.getElementById('1081_xyou2').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10811_3\" raw=\"4\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1081_x1').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x2').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x3').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x4').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x5').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1081_x6').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x7').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x8').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x9').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x10').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('1081_x11').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x12').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x13').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x14').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x15').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('1081_x16').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x17').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x18').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x19').value+"</td>\n"+
				"<td>"+document.getElementById('1081_x20').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;


		case "10821":
			str += "<lab id=\"1080215\">\n"+
				"<table name=\"10821_1\" raw=\"1\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1082_1_xiafeng').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__mujing').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__shuangleng').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__L1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__L2').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10821_2\" raw=\"2\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1082_1__dzuo1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__dyou1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__dzuo2').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__dyou2').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1082_1__xzuo1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__xyou1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__xzuo2').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1__xyou2').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10821_3\" raw=\"4\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1082_1_x1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x2').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x3').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x4').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x5').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1082_1_x6').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x7').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x8').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x9').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x10').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('1082_1_x11').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x12').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x13').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x14').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x15').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('1082_1_x16').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x17').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x18').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x19').value+"</td>\n"+
				"<td>"+document.getElementById('1082_1_x20').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;

		case "10822":
			str += "<lab id=\"1080225\">\n"+
				"<table name=\"10822_1\" raw=\"1\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1082_2_xiafeng').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__mujing').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__shuangleng').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__L1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__L2').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10822_2\" raw=\"2\" column=\"4\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1082_2__dzuo1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__dyou1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__dzuo2').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__dyou2').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1082_2__xzuo1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__xyou1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__xzuo2').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2__xyou2').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10822_3\" raw=\"4\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1082_2_x1').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x2').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x3').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x4').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x5').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1082_2_x6').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x7').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x8').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x9').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x10').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"3\">\n"+
				"<td>"+document.getElementById('1082_2_x11').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x12').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x13').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x14').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x15').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"4\">\n"+
				"<td>"+document.getElementById('1082_2_x16').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x17').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x18').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x19').value+"</td>\n"+
				"<td>"+document.getElementById('1082_2_x20').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;
		case "10911":
			str += "<lab id=\"1090114\">\n"+
				"<table name=\"10911_1\" raw=\"1\" column=\"10\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1091_1_d0').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d100').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d200').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d300').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d400').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d500').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d600').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d700').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d800').value+"</td>\n"+
				"<td>"+document.getElementById('1091_1_d900').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;
		case "10912":
			str += "<lab id=\"1090212\">\n"+
				"<table name=\"10912_1\" raw=\"2\" column=\"10\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1091_2_z11').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z12').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z13').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z14').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z15').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z16').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z17').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z18').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z19').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_z20').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1091_2_y11').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y12').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y13').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y14').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y15').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y16').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y17').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y18').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y19').value+"</td>\n"+
				"<td>"+document.getElementById('1091_2_y20').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;
		case "10913":
			str += "<lab id=\"1090312\">\n"+
				"<table name=\"10913_1\" raw=\"2\" column=\"5\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1091_3_z1').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_z2').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_z3').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_z4').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_z5').value+"</td>\n"+
				"</tr>\n"+
				"<tr index=\"2\">\n"+
				"<td>"+document.getElementById('1091_3_y1').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_y2').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_y3').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_y4').value+"</td>\n"+
				"<td>"+document.getElementById('1091_3_y5').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"<table name=\"10913_2\" raw=\"1\" column=\"11\">\n"+
				"<tr index=\"1\">\n"+
				"<td>"+document.getElementById('1091_4_x1').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x5').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x10').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x15').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x20').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x25').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x30').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x35').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x40').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x45').value+"</td>\n"+
				"<td>"+document.getElementById('1091_4_x50').value+"</td>\n"+
				"</tr>\n"+
				"</table>\n"+
				"</lab>";
			return str;

		default:
		return
	}
}
