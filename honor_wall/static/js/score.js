
$(document).ready(function() {

    $('#score_table').DataTable({
        "scrollY": 300,
        "scrollCollapse": true,
        "language": {
            'lengthMenu': '每页显示 _MENU_ 记录',
            'zeroRecords': '没有数据 - 抱歉',
            'info': ' 第_PAGE_ 页/共 _PAGES_页',
            'infoEmpty': '没有符合条件的记录',
            'search': '查找',
            'infoFiltered': '(从  _MAX_ 条记录中过滤)',
            'paginate': { "first":  "首页 ", "last": "末页", "next": "下一页","previous": "上一页"}
        },
        }
    );
 });
