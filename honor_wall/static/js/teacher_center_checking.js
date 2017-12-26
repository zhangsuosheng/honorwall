var competition;
var competition_index;
var competition_name;
var competition_value;
var competition_2;
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
    if(id=='my_table'){
        pyhttp.open("GET","checking/mytable_"+url+"/select="+competition_value+"page="+(page-1),true)
    }
    else{
        pyhttp.open("GET","checking/mytable_"+url+"/page="+(page-1),true)
    }
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
    if(id=='my_table'){
        pyhttp.open("GET","checking/mytable_"+url+"/select="+competition_value+"page="+(page+1),true)
    }
    else{
        pyhttp.open("GET","checking/mytable_"+url+"/page="+(page+1),true)
    }    pyhttp.send();
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
    if(id=='my_table'){
        pyhttp.open("GET","checking/mytable_"+url+"/select="+competition_value+"page="+(page),true)
    }
    else{
        pyhttp.open("GET","checking/mytable_"+url+"/page="+(page),true)
    }    pyhttp.send();
}
$(document).ready(function(){
    //竞赛的
    document.getElementById("confirm-button").onclick=function(){
        //获取选项条元素
        competition=document.getElementById("stu_honorname_contest");
        //获取选中元素的索引号
        competition_index=competition.selectedIndex;
        //获取索引号所对应的文本内容
        competition_name=competition.options[competition_index].text;
        //获取其索引号所对应的值
        competition_value=competition.options[competition_index].value;
        //如果选择的是第一项提示并返回
        if(competition_value==null||competition_value=="null")
        {
            alert("请对竞赛分类进行选择")
            return;
        }
        //下面的是数据筛选环节然后将table内容填充,设置为可见(未完成)
        var pyhttp=new XMLHttpRequest();//创建请求
        //状态变化的时候更新表格
        pyhttp.onreadystatechange=function()
        {
            if(pyhttp.readyState==4&&pyhttp.status==200)//检查是否存在且正确
            {
                console.log("访问"+"checking/mytable_competition/select="+competition_value+"page=1");
                document.getElementById("my_table").innerHTML=pyhttp.responseText;
            }
        }
        pyhttp.open("GET","checking/mytable_competition/select="+competition_value+"page=1",true);
        pyhttp.send();
    }
    //期刊论文的
    document.getElementById("Bb").onclick=function(){
        //下面的是数据筛选环节然后将table内容填充,设置为可见(未完成)
        var pyhttp=new XMLHttpRequest();//创建请求
        //状态变化的时候更新表格
        pyhttp.onreadystatechange=function()
        {
            if(pyhttp.readyState==4&&pyhttp.status==200)//检查是否存在且正确
            {
                console.log("访问"+"checking/mytable_magazinepaper/page=1");
                document.getElementById("my_table_2").innerHTML=pyhttp.responseText;
            }
        }
        pyhttp.open("GET","checking/mytable_magazinepaper/"+"page=1",true);
        pyhttp.send();
    }
    //重要会议论文
    document.getElementById("Cc").onclick=function(){
        //下面的是数据筛选环节然后将table内容填充,设置为可见(未完成)
        var pyhttp=new XMLHttpRequest();//创建请求
        //状态变化的时候更新表格
        pyhttp.onreadystatechange=function()
        {
            if(pyhttp.readyState==4&&pyhttp.status==200)//检查是否存在且正确
            {
                console.log("访问"+"checking/mytable_meetingpaper/page=1");
                document.getElementById("my_table_3").innerHTML=pyhttp.responseText;
            }
        }
        pyhttp.open("GET","checking/mytable_meetingpaper/"+"page=1",true);
        pyhttp.send();
    }
    //专利的
    document.getElementById("Dd").onclick=function(){
        //下面的是数据筛选环节然后将table内容填充,设置为可见(未完成)
        var pyhttp=new XMLHttpRequest();//创建请求
        //状态变化的时候更新表格
        pyhttp.onreadystatechange=function()
        {
            if(pyhttp.readyState==4&&pyhttp.status==200)//检查是否存在且正确
            {
                console.log("访问"+"checking/mytable_patent/page=1");
                document.getElementById("my_table_4").innerHTML=pyhttp.responseText;
            }
        }
        pyhttp.open("GET","checking/mytable_patent/"+"page=1",true);
        pyhttp.send();
    }
    //奖学金的
    document.getElementById("Ee").onclick=function(){
        //下面的是数据筛选环节然后将table内容填充,设置为可见(未完成)
        var pyhttp=new XMLHttpRequest();//创建请求
        //状态变化的时候更新表格
        pyhttp.onreadystatechange=function()
        {
            if(pyhttp.readyState==4&&pyhttp.status==200)//检查是否存在且正确
            {
                console.log("访问"+"checking/mytable_prize/page=1");
                document.getElementById("my_table_5").innerHTML=pyhttp.responseText;
            }
        }
        pyhttp.open("GET","checking/mytable_prize/"+"page=1",true);
        pyhttp.send();
    }
    //社会经历的
    document.getElementById("Ff").onclick=function(){
        //下面的是数据筛选环节然后将table内容填充,设置为可见(未完成)
        var pyhttp=new XMLHttpRequest();//创建请求
        //状态变化的时候更新表格
        pyhttp.onreadystatechange=function()
        {
            if(pyhttp.readyState==4&&pyhttp.status==200)//检查是否存在且正确
            {
                console.log("访问"+"checking/mytable_experience/page=1");
                document.getElementById("my_table_6").innerHTML=pyhttp.responseText;
            }
        }
        pyhttp.open("GET","checking/mytable_experience/"+"page=1",true);
        pyhttp.send();
    }
    function begin() {
        id=document.getElementsByClassName("tab-pane fade in active")[0].id;
        if(id=="A"){

        }
        else if(id=="B")
        {
            document.getElementById("Bb").onclick();
        }
        else if(id=="C")
        {
            document.getElementById("Cc").onclick();
        }
        else if(id=="D")
        {
            document.getElementById("Dd").onclick();
        }
        else if(id=="E")
        {
            document.getElementById("Ee").onclick();
        }
        else if(id=="F")
        {
            document.getElementById("Ff").onclick();
        }
    }
    begin()
  });

