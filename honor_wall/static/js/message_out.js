$(document).ready(function () {
    var id=document.getElementById("id_here").innerHTML;
    console.log(id)
    $.ajax({
        async:true,
        timeout:8000,
        dataType:"json",
        type:"POST",
        url:'./article_get',
        data:{
            "id":id,
        },
        success:function(data){
            console.log(data.title);
            document.getElementById("title").value=data["title"];
            document.getElementById("class").selectedIndex=data["type"];
            document.getElementsByClassName("note-editable panel-body")[0].innerHTML=data["content"];
            // if(data=="1")
            // {
            //     alert("信息删除成功");
            // }
            // else {
            //     alert("信息删除失败,请联系管理员");
            // }
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            // alert(state)
            // console.log(XMLHttpRequest);
            // console.log(textStatus);
            // console.log(errorThrown);
        }
    });
    document.getElementById("delete").onclick=function () {
        var con=confirm("确定要删除此文章吗？");
        if (con){
            $.ajax({
            async:true,
            timeout:8000,
            dataType:"json",
            type:"POST",
            url:'./article_delete',
            data:{
                "id":id,
            },
            success:function(data){
                if(data=="1")
                {
                    alert("信息删除成功");
                }
                else {
                    alert("信息删除失败,请联系管理员");
                }
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                // alert(state)
                // console.log(XMLHttpRequest);
                // console.log(textStatus);
                // console.log(errorThrown);
            }
        })
        }

    }
    document.getElementById("change").onclick=function () {
        var con=confirm("是否要将文章修改");
        if (con){
            $.ajax({
            async:true,
            timeout:8000,
            dataType:"json",
            type:"POST",
            url:'./article_change',
            data:{
                "id":id,
                "title":document.getElementById("title").value,
                "type":document.getElementById("class").options[document.getElementById("class").selectedIndex].value,
                "content":document.getElementsByClassName("note-editable panel-body")[0].innerHTML,
            },
            success:function(data){
                if(data=="1")
                {
                    alert("信息修改成功");
                }
                else {
                    alert("信息修改失败,请联系管理员");
                }
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                // alert(state)
                // console.log(XMLHttpRequest);
                // console.log(textStatus);
                // console.log(errorThrown);
            }
        })
        }
    }
})