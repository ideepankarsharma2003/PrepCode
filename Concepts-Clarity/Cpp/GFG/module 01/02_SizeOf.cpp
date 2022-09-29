#include <bits/stdc++.h>
using namespace std;

int main()
{
    cout << "Size of bool : " << sizeof(bool) << endl;

    cout << "Size of char : " << sizeof(char) << endl;
    cout << "Size of int : " << sizeof(int) << endl;

    cout << "Size of long : " << sizeof(long) << endl;
    cout << "Size of float : " << sizeof(float) << endl;

    cout << "Size of double : " << sizeof(double) << endl;



    /**
     * @brief MACRO CONSTANTS ----> <limits.h>
     *
        CHAR_MIN      -----> Minimum value for an object of type char
        CHAR_MAX      -----> Maximum value for an object of type char
        SCHAR_MIN     -----> Minimum value for an object of type Signed char
        SCHAR_MAX     -----> Maximum value for an object of type Signed char
        UCHAR_MAX     -----> Maximum value for an object of type Unsigned char
        CHAR_BIT      -----> Number of bits in a char object
        MB_LEN_MAX    -----> Maximum number of bytes in a multi-byte character
        SHRT_MIN      -----> Minimum value for an object of type short int
        SHRT_MAX      -----> Maximum value for an object of type short int
        USHRT_MAX     -----> Maximum value for an object of type Unsigned short int
        INT_MIN       -----> Minimum value for an object of type int
        INT_MAX       -----> Maximum value for an object of type int
        UINT_MAX      -----> Maximum value for an object of type Unsigned int
        LONG_MIN      -----> Minimum value for an object of type long int
        LONG_MAX      -----> Maximum value for an object of type long int
        ULONG_MAX     -----> Maximum value for an object of type Unsigned long int
        LLONG_MIN     -----> Minimum value for an object of type long long int
        LLONG_MAX     -----> Maximum value for an object of type long long int
        ULLONG_MAX    -----> Maximum value for an object of type Unsigned long long int
     */
    
    cout << "Size of char : " << sizeof(char) << " byte" << endl;

    cout << "char minimum value: " << CHAR_MIN << endl;

    cout << "char maximum value: " << CHAR_MAX << endl;

    cout << "Size of int : " << sizeof(int) << " bytes"<< endl;

    cout << "Size of short int : " << sizeof(short int)<< " bytes" << endl;

    cout << "Size of long int : " << sizeof(long int)<< " bytes" << endl;

    cout << "Size of signed long int : "<< sizeof(signed long int) << " bytes" << endl;

    cout << "Size of unsigned long int : "<< sizeof(unsigned long int) << " bytes" << endl;

    cout << "Size of float : " << sizeof(float) << " bytes"<< endl;

    cout << "Size of double : " << sizeof(double) << " bytes" << endl;

    cout << "Size of wchar_t : " << sizeof(wchar_t)<< " bytes" << endl;
    
    
    
    
    
    
    
    
    return 0;
}