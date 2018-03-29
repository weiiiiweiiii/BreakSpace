# BreakSpace
BreakSpace is a light-weighted text editor, built on Python tkinter. This is a team project.

SpaceBreaker Introduction

+-----------------------------------------------------------+
|                       Files Relation                      |
+-----------------------------------------------------------+

+---> spacebreakerlib 
|  |
|  +---> __init__.py
|  |     
|  +---> SpaceBreaker.py
|  |  |         
|  |  +---> WindowConfig.py		
|  |  |
|  |  +---> TextArea.py
|  |  |  |
|  |  |  +---> TextBind.py 
|  |  |  |  |
|  |  |  |  +---> ScrollbarXY.py
|  |  |  |  |
|  |  |  |  +---> FilesControls.py
|  |  |  |  |
|  |  |  |  +---> MenuBar.py 
|	
+---> main.py


+-----------------------------------------------------------+
|                  Files Functionality                      |
+-----------------------------------------------------------+

- spacebreakerlib
	- Functionality package of space breaker

- __init__.py
	- Make spacebreakerlib folder become a package

- SpaceBreaker.py
	- Main body of the space breaker
	- Tk frame, root window of space breaker

- WindowConfig.py
	- Utility module
	- Size, location of root window

- TextArea.py
	- Text Area within spacebreaker
	- Contains Text Area Related Object Dictionary {}
		- Functions
		- Files
	- Pack himself in the end

- TextBind.py
	- Bridge between Text Area and its utility modules.
	- Functions, like FilesControls.
	- Organs, like ScrollbarXY and MenuBar.

- ScrollbarXY.py
	- Vertical and horizontal scrollbar related to Text Area.
	- It has to be pack into root window before text area pack
	  itself into root window.

- FilesControls.py
	- Controls all files utility functions and stored in Text
	  Area Related Object Dictionary.
		- New
		- Open
		- Save
		- Exit

- MenuBar.py
	- Need to be constructed after all utility functions within
	  Menu like FilesControl.
	- adopting function objects within Text Area Related Object
	  Dictionary.


//
//              ii.                                        ;91BH,
//             SA391,                                   .r9GG35&G
//             &#ii13Gh;                              i3X31i;:,rB1
//             iMs,:,i5895,                        .5G91:,:;:s1:8A
//              33::::,,;5G5,                    ,58Si,,:::,sHX;iH1
//               Sr.,:;rs13BBX35hh11511h5Shhh5S3GAXS:.,,::,,1AG3iGG
//               .G51S511sr;;iiiishS8G89Shsrrsh595;.,,,,,..5A85Si,h8
//               :SB9s:,............................,,,.,,,SASh53h,1G.
//            .r18S;..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,....,,.1H315199,rX,
//          ;S89s,..,,,,,,,,,,,,,,,,,,,,,,,....,,.......,,,;r1ShS8,;Xi
//        i55s:.........,,,,,,,,,,,,,,,,.,,,......,.....,,....r9&5.:X1
//       59;.....,.     .,,,,,,,,,,,...        .............,..:1;.:&s
//      s8,..;53S5S3s.   .,,,,,,,.,..      i15S5h1:.........,,,..,,:99
//      93.:39s:rSGB@A   ..,,,,.....    .SG3hhh9G&BGi..,,,,,,,,,,,,.,83
//      G5.G8  9#@@@@@X. .,,,,,,.....  iA9,.S&B###@@Mr...,,,,,,,,..,.;Xh
//      Gs.X8 S@@@@@@@B:..,,,,,,,,,,. rA1 ,A@@@@@@@@@H:........,,,,,,.iX:
//     ;9. ,8A#@@@@@@#5,.,,,,,,,,,... 9A. 8@@@@@@@@@@M;    ....,,,,,,,,S8
//     X3    iS8XAHH8s.,,,,,,,,,,...,..58hH@@@@@@@@@Hs       ...,,,,,,,:Gs
//    r8,        ,,,...,,,,,,,,,,.....  ,h8XABMMHX3r.          .,,,,,,,.rX:
//   :9, .    .:,..,:;;;::,.,,,,,..          .,,.               ..,,,,,,.59
//  .Si      ,:.i8HBMMMMMB&5,....                    .            .,,,,,.sMr
//  SS       :: h@@@@@@@@@@#; .                     ... .          ..,,,,iM5
//  91  .    ;:.,1&@@@@@@Mxs.                           .           .,,:,:&S
//  hS ....  .:;,,,i3MMS1;..,..... .  .     ...                     ..,:,.99
//  ,8; ..... .,:,..,8Ms:;,,,...                                     .,::.83
//   s&: ....  .sS553B@@HX3s;,.    .,;13h.                            .:::&1
//    SXr  .  ...;s3G99XA&X88Shss11155hi.                             ,;:h&,
//     iH8:  . ..   ,;iiii;,::,,,,,.                                 .;irHA
//      ,8X5;   .     .......                                       ,;iihS8Gi
//         1831,                                                 .,;irrrrrs&@
//           ;5A8r                                             .:;iiiiirrss1H
//             :X@H3s.......                                .,:;iii;iiiiirsrh
//              r#h:;,...,,.. .,,:;;;;;:::,...              .:;;;;;;iiiirrss1
//             ,M8 ..,....,.....,,::::::,,...         .     .,;;;iiiiiirss11h
//             8B;.,,,,,,,.,.....          .           ..   .:;;;;iirrsss111h
//            i@5,:::,,,,,,,,.... .                   . .:::;;;;;irrrss111111
//            9Bi,:,,,,......                        ..r91;;;;;iirrsss1ss1111
//
