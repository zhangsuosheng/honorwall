var competition_index_2;
var competition_name_2;
var competition_value_2;
function onclick1(page,id,url) {
    var pyhttp=new XMLHttpRequest();
    pyhttp.onreadystatechange=function () {
        if(pyhttp.readyState==4&&pyhttp.status==200){
            document.getElementById(id).innerHTML=pyhttp.responseText;
        }
    }
    // var page=document.getElementById("active").innerHTML
    // alert(page)
        pyhttp.open("GET","checking/mytable_"+url+"/select="+competition_value_2+"page="+(page-1),true)
    pyhttp.send();
}
 function onclick2(page,id,url){
    var pyhttp=new XMLHttpRequest();
    pyhttp.onreadystatechange=function () {
        if(pyhttp.readyState==4&&pyhttp.status==200){
            document.getElementById(id).innerHTML=pyhttp.responseText;
        }
    }
    // var page=document.getElementById("active").innerHTML
    //  alert(page)
        pyhttp.open("GET","checking/mytable_"+url+"/select="+competition_value_2+"page="+(page+1),true)
        pyhttp.send();
}
 function onclick3(page,id,url){
    var pyhttp=new XMLHttpRequest();
    pyhttp.onreadystatechange=function () {
        if(pyhttp.readyState==4&&pyhttp.status==200){
            document.getElementById(id).innerHTML=pyhttp.responseText;
        }
    }
    // var page=document.getElementById("active").innerHTML
    //  alert(page)
        pyhttp.open("GET","checking/mytable_"+url+"/select="+competition_value_2+"page="+(page),true)
    pyhttp.send();
}
$(document).ready(function() {
    //已审核
    document.getElementById("sha").onclick = function () {
        competition_2 = document.getElementById("stu_honorprice_contest_2");
        //获取选中元素的索引号
        competition_index_2 = competition_2.selectedIndex;
        //获取索引号所对应的文本内容
        competition_name = competition_2.options[competition_index_2].text;
        //获取其索引号所对应的值
        competition_value_2 = competition_2.options[competition_index_2].value;
        //如果选择的是第一项提示并返回
        if (competition_value_2 == null || competition_value_2 == "null") {
            alert("请对竞赛分类进行选择");
            return false;
        }
        var pyhttp = new XMLHttpRequest();//创建请求
        //状态变化的时候更新表格
        pyhttp.onreadystatechange = function () {
            if (pyhttp.readyState == 4 && pyhttp.status == 200)//检查是否存在且正确
            {
                console.log("访问" + "checking/mytable_already/select=" + competition_value_2 + "page=1");
                document.getElementById("my_table_7").innerHTML = pyhttp.responseText;
            }
        }
        pyhttp.open("GET", "checking/mytable_already/select=" + competition_value_2 + "page=1", true);
        pyhttp.send();
    }
})