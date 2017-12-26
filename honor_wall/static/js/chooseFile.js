
//在student_center中实现上传照片、检查照片大小、检查照片文件类型、预览照片
function upload_stu_idphoto(obj,thefile,divtagstr,imgtagstr,filenamelabel) {
    if(typeof (thefile)=="undefined"){
        alert("请选择要上传的照片！");
        imgtagstr.src="";
        filenamelabel.innerHTML="未上传文件";
    }else if(limitFileSize(thefile)){
        if(setImagePreview(obj,divtagstr,imgtagstr))
            loadFile(thefile,filenamelabel);
        else{
            imgtagstr.src="";
            filenamelabel.innerHTML="未上传文件";
        }
    }
}

//在student_center_checking中实现上传文件大小检查
function upload_stu_provefile(file,labelidstr){
    if(file.size/1024/1024>10){
        alert("证明材料请勿超过10M");
    }else{
        loadFile(file,labelidstr);
    }
}

////////////////////////////////////以下是上面两个函数所用的工具函数////////////////////////////////////////////
//函数1：上传文件
function loadFile(file,labelidstr){
    labelidstr.innerHTML=file.name;
}



//函数2：检查图片的格式是否正确,同时实现预览
function setImagePreview(obj, localImagId, imgObjPreview) {
    alert("hello");
    var array = new Array('jpeg', 'png', 'jpg', 'bmp'); //可以上传的文件类型
    if (obj.value =="") {
        alert("请选择要上传的图片!");
        return false;
    }
    else {
        var fileContentType = obj.value.match(/^(.*)(\.)(.{1,8})$/)[3]; //这个文件类型正则很有用
        ////布尔型变量
        var isExists = false;
        //循环判断图片的格式是否正确
        for (var i in array) {
            if (fileContentType.toLowerCase() == array[i].toLowerCase()) {
                //图片格式正确之后，根据浏览器的不同设置图片的大小

                if (obj.files && obj.files[0]) {
                    //火狐下，直接设img属性
                   imgObjPreview.style.display = 'block';
                   imgObjPreview.style.width = '150px';
                   imgObjPreview.style.height = '210px';
                    //火狐7以上版本不能用上面的getAsDataURL()方式获取，需要一下方式
                    imgObjPreview.src = window.URL.createObjectURL(obj.files[0]);
                }else{
                    alert("预览图片加载失败，请使用其他浏览器");
                    obj.value=""
                    return false;
                }
                isExists = true;
                return true;
            }
        }
        if (isExists == false) {
            alert("上传图片类型不正确!");
            obj.value="";
            return false;
        }
        return false;
    }
    //alert("此时图片框中图片为："+imgObjPreview.src);
}
//3、限制文件存储空间大小
function limitFileSize(thefile) {
    if(thefile.size/1024/1024>3){
        alert("图片过大，请选择小于3M的图片");
        return false;
    }
    return true;
}
