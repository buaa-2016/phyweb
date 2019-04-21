
var globalLabDataMap = {};
 
function lab(index){
	this.index = index;
	this.dbId = getDbId(index);
	this.xmlTxt;
	this.inputkind;
	this.flush = function(){
		this.inputkind = $("#report-data-input-modal div.tab-pane.active").data('lab-kind');
		console.log("flush, experiment-id=" + this.index);
		console.log("flush, lab-kind=" + this.inputkind);
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

function getDbId(experiment_id){
	let db_id = $('#experiment-data-' + experiment_id).data('db-id');
	console.log("getDbId() " + experiment_id + ": " + db_id);
	return db_id;
}

$(".btn-view-pdf").click(function() {
	console.log(".btn-view-pdf clicked!");
	let pdf = $(this).parent().data("prepare-pdf");
	PDFObject.embed("./prepare_pdf/" + pdf, "#pdf-object");
})

$('table>tbody button.btn-input-data').click(function() {
	$("#report-data-input-modal").modal('show');
	let experiment_id = $(this).parent().data("experiment-id");
	let remote_form = './lab_data_forms/' + experiment_id + '.html';
	$("#report-data-input-modal .modal-content").load(remote_form, function( response, status, xhr ) {
		if (status === 'error') {
			alert("加载失败，请检查网络连接");
			return;
		}
		$('button.btn-Save').click(btnSaveClicked);
	});
})

$('table>tbody button.btn-gen-report').click(function() {
	console.log("btn-gen-report clicked!");
	let experiment_id = $(this).parent().data("experiment-id");
	Post_lab(experiment_id);
})

function checkInput() {
	let activeTab = $("#report-data-input-modal div.tab-pane.active");
	if (activeTab.length != 1) {
		alert("出错啦，请查看控制台输出");
		console.log("expected 1 active tab, but we got " + activeTab.length);
	}
	let invalid_count = 0;
	let count = 0;
    let pattern = new RegExp('^\\d+(.\\d+)?$');
	activeTab.find("input").each(function() {
		count++;
		if (!pattern.test($(this).val())) {
			invalid_count++;
		}
	});
	if (invalid_count > 0) {
		alert("共" + count + "项输入, 您有" + invalid_count + "项输入不合法");
		return false;
	}
	return true;
}

function btnSaveClicked() {
	console.log("btn-Save clicked");
	if (!checkInput()) {
		return;
	}
	let experiment_id = $(this).data('experiment-id');
	console.log(experiment_id);
	globalLabDataMap[experiment_id] = new lab(experiment_id);
	globalLabDataMap[experiment_id].flush();
	$(`table>tbody div[data-experiment-id="${experiment_id}"] button.btn-gen-report`).removeClass('disabled');
	// close modal
	$('#report-data-input-modal').modal('hide');
}

function Post_lab(experiment_id){
	let curLab = globalLabDataMap[experiment_id];
	var xmlString = curLab.getXML();
	var dbId = curLab.getDbId();
	var kind = curLab.getKind();
	PostXMLDoc("/report",xmlString,dbId,kind,function(){
		if (this.readyState==4 && this.status==200){
			var jsonText = eval("(" + this.responseText + ")");
			if(jsonText["status"]=='success'){
				PDFObject.embed("./" + jsonText['link'], "#pdf-object");
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