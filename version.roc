#define VER_FILEVERSION             3,10,349,0
#define VER_FILEVERSION_STR         "3.10.349.0\0"

#define VER_PRODUCTVERSION          3,10,0,0
#define VER_PRODUCTVERSION_STR      "3.10\0"

#ifndef DEBUG
#define VER_DEBUG                   0
#else
#define VER_DEBUG                   VS_FF_DEBUG
#endif

VS_VERSION_INFO, VERSIONINFO
FILEVERSION     1.0
PRODUCTVERSION  1.0
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "040904E4"
        BEGIN
            VALUE "CompanyName",      "iam-py-test"
            VALUE "FileDescription",  "Check your passwords"
            VALUE "FileVersion",      "1.0"
            VALUE "InternalName",     "passwd.exe"
            VALUE "LegalCopyright",   "Copyleft 2021 iam-py-test"
            VALUE "OriginalFilename", "password.exe"
            VALUE "ProductName",      "Password check"
            VALUE "ProductVersion",   "1.0"
        END
    END

    BLOCK "VarFileInfo"
    BEGIN
        /* The following line should only be modified for localized versions.     */
        /* It consists of any number of WORD,WORD pairs, with each pair           */
        /* describing a language,codepage combination supported by the file.      */
        /*                                                                        */
        /* For example, a file might have values "0x409,1252" indicating that it  */
        /* supports English language (0x409) in the Windows ANSI codepage (1252). */

        VALUE "Translation", 0x409, 1252

    END
END