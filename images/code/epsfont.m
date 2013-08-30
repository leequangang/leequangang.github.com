function epsfont(epsfilename)
%输入eps文件名，输出嵌入字体后的eps文件，用到用GhostScript的gswin32c.exe
%新文件名字添加后缀_NEW.eps

% netname=textread(list,'%s');
% [N,m]=size(netname);
 dir_path = 'C:\CTEX\Ghostscript\gs9.00\bin';%gswin32c.exe的路径
 file_path=pwd;
 eps2pdf = 'gswin32c -dNOPAUSE -dBATCH -dEPSCrop -q -sDEVICE=pdfwrite -dCompatibilityLevel#1.3 -dPDFSETTINGS=/prepress -dSubsetFonts=true -dEmbedAllFonts=true -sOutputFile=temp.pdf';
 eps2pdf = [dir_path,'\',eps2pdf,' ',file_path,'\',epsfilename];

 
 pdf2eps = 'gswin32c -q -dNOPAUSE -dBATCH -dNOCACHE -sDEVICE=epswrite -sOutputFile=';
 pdf2eps = [dir_path,'\', pdf2eps,file_path,'\',epsfilename,'_NEW.eps temp.pdf'];

   % tic;
    system(eps2pdf);
    system(pdf2eps);
   % toc;
delete 'temp.pdf';

end