//在选中下拉菜单中的“其他”一项时弹出文本框让填内容
function showothers(tagid,value) {
    if(value=="others"){
        tagid.style.display="block";
    }
    else{
        tagid.style.display="none";
    }
}