function addauthor(thisbutton,fillindiv) {
    if(fillindiv.style.display=="none"){
        fillindiv.style.display="block";
        thisbutton.innerHTML="取消";
    }else{
        fillindiv.style.display="none";
        thisbutton.innerHTML="添加";
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//添加的其他作者的数量
var num=0;

function createlabel(nametag,ordertag) {

    var name=nametag.value;
    var order=ordertag.value;
    if(trim(name)!=""&&trim(order)!=""){
       num++;

        var myElement = document.createElement('span');
        myElement.innerHTML ="    姓名："+trim(name)+"    "+"位次："+trim(order);
        myElement.id = "stu_otherauthor"+num+"_magazinepaper";

        
        var deletebutton=document.createElement('button');

        deletebutton.innerHTML="删除";
        deletebutton.id="stu_deletethisauthor"+num+"_magazinepaper";
        deletebutton.onclick=function () {
            javascript:deletethisauthor(myElement.id,deletebutton.id)
        };
        alert(deletebutton.onclick);
        document.getElementById("stu_otherauthors_magazinepaper").appendChild(myElement);
        document.getElementById("stu_otherauthors_magazinepaper").appendChild(deletebutton);
        nametag.value="";
        ordertag.value="";

    }else{
        alert("信息不完整！");
    }
}

function trim(str)
{
    return str.replace("/(^\s*)|(\s*$)/g,");
}

function deletethisauthor(authorid,buttonid) {
    alert(authorid+"  "+buttonid);
    document.getElementById(authorid).remove();
    document.getElementById(buttonid).remove();
    num--;
}




///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////






//添加的其他作者的数量
var numformeeting=0;

function createlabelformeeting(nametag,ordertag) {

    var name=nametag.value;
    var order=ordertag.value;
    if(trim(name)!=""&&trim(order)!=""){
        numformeeting++;

        var myElement = document.createElement('span');
        myElement.innerHTML ="    姓名："+trim(name)+"    "+"位次："+trim(order);
        myElement.id = "stu_otherauthor"+numformeeting+"_meeting";


        var deletebutton=document.createElement('button');

        deletebutton.innerHTML="删除";
        deletebutton.id="stu_deletethisauthor"+numformeeting+"_meeting";
        deletebutton.onclick=function () {
            javascript:deletethisauthorformeeting(myElement.id,deletebutton.id)
        };
        alert(deletebutton.onclick);
        document.getElementById("stu_otherauthors_meeting").appendChild(myElement);
        document.getElementById("stu_otherauthors_meeting").appendChild(deletebutton);
        nametag.value="";
        ordertag.value="";

    }else{
        alert("信息不完整！");
    }
}

function deletethisauthorformeeting(authorid,buttonid) {
    alert(authorid+"  "+buttonid);
    document.getElementById(authorid).remove();
    document.getElementById(buttonid).remove();
    numformeeting--;
}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//添加的其他作者的数量
var numforpatent=0;

function createlabelforpatent(nametag,ordertag) {

    var name=nametag.value;
    var order=ordertag.value;
    if(trim(name)!=""&&trim(order)!=""){
        numforpatent++;

        var myElement = document.createElement('span');
        myElement.innerHTML ="    姓名："+trim(name)+"    "+"位次："+trim(order);
        myElement.id = "stu_otherauthor"+numforpatent+"_patent";


        var deletebutton=document.createElement('button');

        deletebutton.innerHTML="删除";
        deletebutton.id="stu_deletethisauthor"+numforpatent+"_patent";
        deletebutton.onclick=function () {
            javascript:deletethisauthorforpatent(myElement.id,deletebutton.id)
        };
        alert(deletebutton.onclick);
        document.getElementById("stu_otherauthors_patent").appendChild(myElement);
        document.getElementById("stu_otherauthors_patent").appendChild(deletebutton);
        nametag.value="";
        ordertag.value="";

    }else{
        alert("信息不完整！");
    }
}

function deletethisauthorforpatent(authorid,buttonid) {
    alert(authorid+"  "+buttonid);
    document.getElementById(authorid).remove();
    document.getElementById(buttonid).remove();
    numforpatent--;
}