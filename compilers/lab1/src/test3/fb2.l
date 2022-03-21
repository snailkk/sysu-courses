%option noyywrap
%x IFILE

%{
    struct bufstack{
        struct bufstack *prev;/* 上一个文件信息*/
        YY_BUFFER_STATE bs;/* 保存的缓冲区 */
        
    }
}