function Editor() {

}

Editor.prototype.init = function () {
    window.ue = UE.getEditor('editor', {
        'initialFrameHeight': 400,
        'serverUrl': '/ueditor/upload/',
        toolbars : [
            ['fullscreen','paragraph','fontfamily','fontsize','|',
            'inserttable','deletetable','insertrow','insertcol','deleterow','deletecol','mergeright','mergedown','splittorows','splittocols','splittocells','deletecaption','inserttitle',],
            ['searchreplace','|','undo', 'redo', '|','justifyleft','justifyright','justifycenter','justifyjustify','bold','italic','underline','fontborder','strikethrough','superscript','subscript',
            '|','touppercase','tolowercase','|','attachment','map','simpleupload','emotion','spechars','imagenone','imagecenter','imageleft','imageright',]
        ]
    });
};

Editor.prototype.run = function () {
    var self = this;
    self.init();
};

$(function () {
    var editor = new Editor();
    editor.run();
});
