$(document).ready(function(){
//     $.ajax({
//         async:true,
//         timeout:8000,
//         type:"POST",
//         dataType:"json",
//         url:'./studentmessagechange_2',
//         data:{
//             "id":id,
//             "name":name,
//             "grade":grade,
//             "field":field,
//             "classroom":classroom,
//         },
//         success:function(data){
//             alert(data)
//         },
//         error:function(XMLHttpRequest, textStatus, errorThrown){
//             console.log(XMLHttpRequest);
//             console.log(textStatus);
//             console.log(errorThrown);
//             document.getElementById("table").innerHTML='<h4 style="color:red">信息错误<small>请联系管理员进行查看</small></h4>';
//         }
// })

    var name_obj=document.getElementById("name");
    var id_obj=document.getElementById("id");
    var sex_obj=document.getElementById("sex");
    var field_obj=document.getElementById("field");
    var grade_obj=document.getElementById("grade");
    var classroom_obj=document.getElementById("classroom");
    var faculty_obj=document.getElementById("faculty");
    var state_id=document.getElementById("state_id").innerHTML;
    var nickname_obj=document.getElementById("nickname");
    var political_obj=document.getElementById("political");
    var people_obj=document.getElementById("people");
    if (state_id){
        var state_obj=document.getElementsByClassName("switch-animate switch-off")[0];
        state_obj.className="switch-animate switch-on"
    }
    if (document.getElementsByClassName("switch-animate switch-off")[0]!=undefined)
    {
        var state_obj=document.getElementsByClassName("switch-animate switch-off")[0];
    }
    else {
        var state_obj=document.getElementsByClassName("switch-animate switch-on")[0];
    }
    var sex_index=sex_obj.selectedIndex;
    var field_index=field_obj.selectedIndex;
    var grade_index=grade_obj.selectedIndex;
    var classroom_index=classroom_obj.selectedIndex;


    var name=name_obj.value;
    var id=id_obj.value;
    var sex=sex_obj.options[sex_index].value;
    var field=field_obj.options[field_index].value;
    var grade=grade_obj.options[grade_index].value;
    var classroom=classroom_obj.options[classroom_index].value;
    var faculty=faculty_obj.value;
    var state_obj;
    var nickname=nickname_obj.value;
    var political=political_obj.value;
    var people=people_obj.value;
    if (document.getElementsByClassName("switch-animate switch-on")[0]!=undefined)
    {
        state_obj=document.getElementsByClassName("switch-animate switch-on")[0];
    }
    else {
        state_obj=document.getElementsByClassName("switch-animate switch-off")[0];
    }
    document.getElementById("delete-button").onclick=function () {
        name_obj.value=name;
        id_obj.value=id;
        sex_obj.selectedIndex=sex_index;
        field_obj.selectedIndex=field_index;
        grade_obj.selectedIndex=grade_index;
        classroom_obj.selectedIndex=classroom_index;
        faculty_obj.value=faculty;
        if (state_id){
            state_obj.className="switch-on switch-animate";
        }
        else {
            state_obj.className="switch-off switch-animate";
        }
        nickname_obj.value=nickname;
        political_obj.value=political;
        people_obj.value=people;
    }

     document.getElementById("confirm-button").onclick=function () {
    // var srcElement=event.sreElement;
    // alert(event.srcElement.className)
        sex_index=sex_obj.selectedIndex;
        field_index=field_obj.selectedIndex;
        grade_index=grade_obj.selectedIndex;
        classroom_index=classroom_obj.selectedIndex;


        name=name_obj.value;
        id=id_obj.value;
        sex=sex_obj.options[sex_index].value;
        field=field_obj.options[field_index].value;
        grade=grade_obj.options[grade_index].value;
        classroom=classroom_obj.options[classroom_index].value;
        faculty=faculty_obj.value;
        nickname=nickname_obj.value;
        political=political_obj.value;
        people=people_obj.value;
        var a;
        if(sex=="男")
        {
            a=1;
        }
        else {
            a=0;
        }
        var state;
        if (document.getElementsByClassName("switch-animate switch-on")[0]!=undefined)
        {
            // alert("yes")
            state=1;
        }
        else {
            state=0;
        }
        $.ajax({
        async:true,
        timeout:8000,
        type:"POST",
        dataType:"json",
        url:'../save',
        data:{
            "id":id,
            "name":name,
            "sex":a,
            "grade":grade,
            "field":field,
            "classroom":classroom,
            "faculty":faculty,
            "nickname":nickname,
            "political":political,
            "people":people,
            "state":state,
        },
        success:function(data){
            // alert(state)
        },
        error:function(XMLHttpRequest, textStatus, errorThrown){
            // alert(state)
            // console.log(XMLHttpRequest);
            // console.log(textStatus);
            // console.log(errorThrown);
        }
        })
}
})
