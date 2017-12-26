function a(self) {
    document.getElementById("name").value=self.innerHTML;
}
$(document).ready(function () {
    var message;
    $.typeahead({
            input:".js-typeahead",
            order:"asc",
            source: {
                groupName: {
                    // Ajax Request
                    ajax: {
                        async:true,
                        timeout:8000,
                        type:"POST",
                        dataType:"json",
                        url:'./getcompetition',
                        success:function(data){
                            message=data;
                            console.log(message);
                        },
                    }
                }
            },
            callback: {
                onClickBefore:function() {

                }
            }
        });
    // $.ajax({
    //     async:true,
    //     timeout:8000,
    //     type:"POST",
    //     dataType:"json",
    //     url:'./getcompetition',
    //     success:function(data){
    //         message=data;
    //         // console.log(message);
    //     },
    //     error:function(XMLHttpRequest, textStatus, errorThrown){
    //         // alert(state)
    //         // console.log(XMLHttpRequest);
    //         // console.log(textStatus);
    //         // console.log(errorThrown);
    //     }
    // })
    var name_obj=document.getElementById("name");
    var competition_level_obj=document.getElementById("competition_level");
    var level_obj=document.getElementById("level");
    var points_obj=document.getElementById("points");
    var message_obj=document.getElementById("competition_message");
    var name=name_obj.value;
    var competition_level_index=competition_level_obj.selectedIndex;
    var competition_level=competition_level_obj.options[competition_level_index].value;
    if(competition_level==""){

    }
    var level_index=level_obj.selectedIndex;
    var level=level_obj.options[level_index].value;
    var points=points_obj.value;
    var message2=message_obj.value;
    var time;
    var ss;
    // document.getElementById("name").onfocus=function () {
    //     ss=document.getElementById("name").value;
    //     time=setInterval(function(){
    //         var m=[];
    //         var s=document.getElementById("name").value;
    //         for(i in message){
    //             if(message[i].indexOf(s)!=-1){
    //                 m.push(message[i])
    //             }
    //         }
    //         var inner="";
    //         for (i in m){
    //             inner+="<tr ><th onmouseover=document.getElementById('name').value=this.innerHTML onmouseout=document.getElementById('name').value>"+m[i]+"</th></tr>";
    //         }
    //
    //         document.getElementById("table").innerHTML=inner;
    //         // console.log(inner);
    //     },500);
    // }
    //
    //
    // document.getElementById("name").onblur=function () {
    //     document.getElementById("table").innerHTML="";
    //     clearInterval(time);
    // }
    // // document.getElementById("t").onmouseover=function () {
    // //     alert(event.srcElement.innerHTML)
    // // }
    // // document.getElementById("t").onclick=function () {
    // //     alert(event.srcElement.innerHTML)
    // // }
    // // document.body.onmouseover=function () {
    // //     alert(event.srcElement.id)
    // // }
    document.getElementById("submit").onclick=function () {
        var name_2=name_obj.value;
        var is=1;
        var is_true=1;
        for (i in message){
            console.log(message[i]);
            if(message[i].display==name_2){
                is=0;
                is_true=0;
                break;
            }
        }
        if (is==0){
            var con=confirm("已存在此条信息,您是否选择将其覆盖");
            if(con==true){
                is=1;
            }
        }
        if (is==1){
            var competition_level_index_2=competition_level_obj.selectedIndex;
        var competition_level_2=competition_level_obj.options[competition_level_index_2].value;
        // alert(competition_level_2)
        var level_index_2=level_obj.selectedIndex;
        var level_2=level_obj.options[level_index_2].value;
        var points_2=points_obj.value;
        var message_2=message_obj.value;
        $.ajax({
            async:true,
            timeout:8000,
            type:"POST",
            dataType:"json",
            url:'./submit',
            data:{
                "name":name_2,
                "competition_level":competition_level_2,
                "level":level_2,
                "points":points_2,
                "message":message_2,
                "is":is_true,
            },
            success:function(data){
                if(data=="1")
                {
                    var group={display:name_2,group:"groupName"};
                    message.push(group);
                    alert("信息存储成功");
                }
                else {
                    alert("信息存储失败,请联系管理员");
                }
            },
            error:function(XMLHttpRequest, textStatus, errorThrown){
                // alert(state)
                // console.log(XMLHttpRequest);
                // console.log(textStatus);
                // console.log(errorThrown);
            }
        });
        }

    }
    document.getElementById("cancel").onclick=function () {
        name_obj.value=name;
        competition_level_obj.selectedIndex=competition_level_index;
        level_obj.selectedIndex=level_index;
        points_obj.value=points;
        message_obj.value=message2;
    }
    document.getElementById("delete").onclick=function () {
        var name_now=document.getElementById("name").value;
        var is_2=0;
        for(i in message){
            if (name_now==message[i].display){
                is_2=1;
            }
        }
        if(is_2==1){
                var con2=confirm("确定将此信息删除吗?");
                if (con2==true){
                    $.ajax({
                        async:true,
                        timeout:8000,
                        type:"POST",
                        dataType:"json",
                        url:'./delete',
                        data:{
                            "name":name_now,
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
            else {
                alert("该条信息不存在！");
            }
    }
    document.getElementById("cop2").onclick=function () {
        location.reload(true);
    }
})