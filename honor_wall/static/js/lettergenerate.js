var id=parseInt(document.getElementById("id").value);
var name=document.getElementById("nickname").value;
var grade_obj=document.getElementById("grade");
var grade_index=grade_obj.selectedIndex;
var grade=grade_obj.options[grade_index].value;
var field_obj=document.getElementById("field");
var field_index=field_obj.selectedIndex;
var field=field_obj.options[field_index].value;
var classroom_obj=document.getElementById("classroom");
var classroom_index=classroom_obj.selectedIndex;
var classroom=classroom_obj.options[classroom_index].value;
var all=new Array();
var table=document.getElementById("table");
$(document).ready(function(){

    document.getElementById("search").onclick=function () {
        id=parseInt(document.getElementById("id").value);
        name=document.getElementById("nickname").value;
        grade_obj=document.getElementById("grade");
        grade_index=grade_obj.selectedIndex;
        grade=grade_obj.options[grade_index].value;
        field_obj=document.getElementById("field");
        field_index=field_obj.selectedIndex;
        field=field_obj.options[field_index].value;
        classroom_obj=document.getElementById("classroom");
        classroom_index=classroom_obj.selectedIndex;
        classroom=classroom_obj.options[classroom_index].value;
        if (isNaN(id)){
            id=null;
        }
        if(grade=="null"){
            grade=null;
        }
        if(field=="null"){
            field=null;
        }
        if(classroom=="null"){
            classroom=null;
        }
        $.ajax({
            async:true,
            timeout:8000,
            type:"POST",
            dataType:"json",
            url:'./search',
            data:{
                "id":id,
                "name":name,
                "grade":grade,
                "field":field,
                "classroom":classroom,
            },
            success:function(data){
                all=new Array();
                for (i in data){
                    console.log(data[i].id+" "+data[i].name+" "+data[i].grade+"  "+data[i].field+"  "+data[i].classroom)
                    all.push(data[i]);
                    // alert(data[i]);
                }
                // alert(data["name"]);
                show(1);
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                console.log(XMLHttpRequest);
                console.log(textStatus);
                console.log(errorThrown);
                document.getElementById("table").innerHTML='<h4 style="color:red">无相匹配的学生的存在<small>请您进行信息的审核</small></h4>';
            }

        })

    }
})
function show(page) {
    var page_per=10;
    var item=all.length;
    // alert(item);
    var page_max=Math.floor(item/page_per)+1;
    html_head='<table class=\"table table-striped table-bordered table-condensed\"><thead><tr class=\"info\"><th>序号</th><th>学号</th><th>姓名</th><th>年级</th><th>专业</th><th>班级</th><th>操作</th></tr></thead><tbody>';
    html_middle="";
    html_end="</tbody></table>";
    html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">';
    var count=0;
    var begin=0;
    var end=0;
    if (page==page_max){
        begin=(page-1)*page_per+1;
        end=item;
    }
    else {
        begin=(page-1)*page_per+1;
        end=begin+page_per;
    }
    for(var j=begin;j<=end;j++) {
        count++;
        var mess="";
        if(count==1) {
                mess = '<tr class="success"><th>' + j + '</th><th>' + all[j-1]["id"] + '</th><th>' + all[j-1]["name"] + '</th><th>' + all[j-1]["grade"] + '</th><th>' + all[j-1]["field"] +'</th><th>' + all[j-1]["classroom"] + '</th><th><a href="#" class="btn btn-xs btn-warning" style="margin-right:20px;">简历生成</a><a href="#" class="btn btn-xs btn-warning" >推荐信生成</a></th>';
        }
        else {
            mess = '<tr><th>' + j + '</th><th>' + all[j-1]["id"] + '</th><th>' + all[j-1]["name"] + '</th><th>' + all[j-1]["grade"] + '</th><th>' + all[j-1]["field"] +'</th><th>' + all[j-1]["classroom"] + '</th><th><a href="#" class="btn btn-xs btn-warning" style="margin-right:20px;">简历生成</a><a href="#" class="btn btn-xs btn-warning" >推荐信生成</a></th>';
        }
        html_middle += mess;
    }
    if (page<=7){
        if (page != 1){
            html_end += '<li id="page_up" onclick=show('+(page-1)+')><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'}
        for (i=1;i<=page_max;i++){
            if (i == page) {
                html_end += '<li onclick="show(' +i+ ')" id="active" class="active"><a >' + i + '</a></li>'
            }
            else {
                html_end += '<li onclick="show('+i+')"><a >' + i + '</a></li>'
            }
            }

        if (!(page == page_max)) {
            html_end += '<li id="page_down" onclick="show(' +(page+1)+ ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        }
        html_end += '</ul></div>'
    }
    else if(page_max-3<page){
        html_end += '<li onclick="show('+(page-1)+')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
    for (i=page_max-6;i<=page_max;i++) {
        if (i == page) {
            html_end += '<li onclick="show(' +i+ ')" id="active" class="active"><a >' + i + '</a></li>'
        }
        else {
            html_end += '<li onclick="show(' + i+ ')"><a >' + i + '</a></li>'
        }
    }
    if (!(page == p_length)) {
        html_end += '<li id="page_down" onclick="show('+i+')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
    }
    html_end += '</ul></div>'
    }
    else {
            if (!(page == 1)) {
                html_end += '<li id="page_up" onclick="show(' + i + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            }
            if (page - 3 <= 0) {
                min = 1
                max = 8
            }
            else{
                min = page - 3
                max = page + 3 + 1
            }
            for (i=min;i<max;i++ )
                if (i == page) {
                    html_end += '<li onclick="show(' + i + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                }
                else {
                    html_end += '<li onclick="show(' + i+ ')"><a >' + i + '</a></li>'
                }
            if (!(page == p_length)) {
                html_end += '<li id="page_down" onclick="show(' + (page+1)+ ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            }
    }

    table.innerHTML=html_head+html_middle+html_end;
    // alert(table.innerHTML)
}