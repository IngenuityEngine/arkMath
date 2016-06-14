MATH README
By Mike Ravella

Edits:
@mravella - 8.21.14

Files:
- Mat44
- Vec4

Module initially created for use with weaver.  Not meant to run standalone.

Contains a vec4 and a 4x4 matrix class.

Vec4 has elements that can be accessed with <.x, .y, .z, .t.>, <.r, .g, .b, .a>, or <.h, .s, .v, .a>.  There is functionality for length, angle between two vectors, dot product, cross product, linear combination, normalization, addition, subtraction, scalar multiplication, negation, min, and max.

Operators are overriden such that * refers to dot product / scalar multiplication, + is addition, - is subtraction, and print will print a list representation. Box notation can be used to get elements. (i.e. vec[1] = vec.y)

To initialize, you can feed a list of size 3 or 4, 4 values as separate arguments, or specify x y z and t with keywords.  Any values that are unspecified will default to zero, regardless of how the values were specified.

Mat44 is essentially just 4 Vec4s that represent the ROWS of the matrix.
To access values in the Mat44, you can access the row with <.row0, .row1, .row2, .row3>,
and then accessing the column with the <.x, .y, .z, .t> as you would a vec4.  So to get the element that refers to the 2nd row and 1st column, you could write mat.row1.x.  You can also get a row by indexing in box notation, so mat[1] = mat.row1, or you can index directly with a tuple.  So mat[1,0] = mat.row1.x.

Functionality exists for transposition, vector matrix multiplication, matrix vector multiplication, matrix matrix multiplication, scalar multiplication, addition, subtraction, determinant, inverse, and svd.

The multiply, add, subtract, getitem, setitem and print operators are overriden.

To initialize a matrix, you can feed it a list of 16 values, 4 row vectors, or use the 16 keywords to fill in the matrix.  Any values that are left unspecified will default to their value in a standard 4x4 identity matrix.