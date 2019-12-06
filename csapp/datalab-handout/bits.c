/*
 * CS:APP Data Lab
 *
 * 2017302580290  毛云麟
 *
 * bits.c - Source file with your solutions to the Lab.
 *          This is the file you will hand in to your instructor.
 *
 * WARNING: Do not include the <stdio.h> header; it confuses the dlc
 * compiler. You can still use printf for debugging without including
 * <stdio.h>, although you might get a compiler warning. In general,
 * it's not good practice to ignore compiler warnings, but in this
 * case it's OK.
 */

#if 0
 /*
  * Instructions to Students:
  *
  * STEP 1: Read the following instructions carefully.
  */

You will provide your solution to the Data Lab by
editing the collection of functions in this source file.

INTEGER CODING RULES :

Replace the "return" statement in each function with one
or more lines of C code that implements the function.Your code
must conform to the following style :

int Funct(arg1, arg2, ...) {
	/* brief description of how your implementation works */
	int var1 = Expr1;
	...
		int varM = ExprM;

	varJ = ExprJ;
	...
		varN = ExprN;
	return ExprR;
}

Each "Expr" is an expression using ONLY the following :
1. Integer constants 0 through 255 (0xFF), inclusive.You are
not allowed to use big constants such as 0xffffffff.
2. Function arguments and local variables(no global variables).
3. Unary integer operations !~
4. Binary integer operations & ^| +<< >>

Some of the problems restrict the set of allowed operators even further.
Each "Expr" may consist of multiple operators.You are not restricted to
one operator per line.

You are expressly forbidden to :
1. Use any control constructs such as if, do, while, for, switch, etc.
2. Define or use any macros.
3. Define any additional functions in this file.
4. Call any functions.
5. Use any other operations, such as&&, || , -, or ? :
	6. Use any form of casting.
	7. Use any data type other than int.This implies that you
	cannot use arrays, structs, or unions.


	You may assume that your machine :
1. Uses 2s complement, 32 - bit representations of integers.
2. Performs right shifts arithmetically.
3. Has unpredictable behavior when shifting an integer by more
than the word size.

EXAMPLES OF ACCEPTABLE CODING STYLE :
/*
 * pow2plus1 - returns 2^x + 1, where 0 <= x <= 31
 */
int pow2plus1(int x) {
	/* exploit ability of shifts to compute powers of 2 */
	return (1 << x) + 1;
}

/*
 * pow2plus4 - returns 2^x + 4, where 0 <= x <= 31
 */
int pow2plus4(int x) {
	/* exploit ability of shifts to compute powers of 2 */
	int result = (1 << x);
	result += 4;
	return result;
}

FLOATING POINT CODING RULES

For the problems that require you to implent floating - point operations,
the coding rules are less strict.You are allowed to use loopingand
conditional control.You are allowed to use both intsand unsigneds.
You can use arbitrary integerand unsigned constants.

You are expressly forbidden to :
1. Define or use any macros.
2. Define any additional functions in this file.
3. Call any functions.
4. Use any form of casting.
5. Use any data type other than int or unsigned.This means that you
cannot use arrays, structs, or unions.
6. Use any floating point data types, operations, or constants.


NOTES:
1. Use the dlc(data lab checker) compiler(described in the handout) to
check the legality of your solutions.
2. Each function has a maximum number of operators(!~&^| +<< >>)
that you are allowed to use for your implementation of the function.
The max operator count is checked by dlc.Note that '=' is not
counted; you may use as many of these as you want without penalty.
3. Use the btest test harness to check your functions for correctness.
4. Use the BDD checker to formally verify your functions
5. The maximum number of ops for each function is given in the
header comment for each function.If there are any inconsistencies
between the maximum ops in the writeupand in this file, consider
this file the authoritative source.

/*
 * STEP 2: Modify the following functions according the coding rules.
 *
 *   IMPORTANT. TO AVOID GRADING SURPRISES:
 *   1. Use the dlc compiler to check that your solutions conform
 *      to the coding rules.
 *   2. Use the BDD checker to formally verify that your solutions produce
 *      the correct answers.
 */


#endif
 /* Copyright (C) 1991-2018 Free Software Foundation, Inc.
	This file is part of the GNU C Library.

	The GNU C Library is free software; you can redistribute it and/or
	modify it under the terms of the GNU Lesser General Public
	License as published by the Free Software Foundation; either
	version 2.1 of the License, or (at your option) any later version.

	The GNU C Library is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
	Lesser General Public License for more details.

	You should have received a copy of the GNU Lesser General Public
	License along with the GNU C Library; if not, see
	<http://www.gnu.org/licenses/>.  */
	/* This header is separate from features.h so that the compiler can
	   include it implicitly at the start of every compilation.  It must
	   not itself include <features.h> or any other header that includes
	   <features.h> because the implicit include comes before any feature
	   test macros that may be defined in a source file before it first
	   explicitly includes a system header.  GCC knows the name of this
	   header in order to preinclude it.  */
	   /* glibc's intent is to support the IEC 559 math functionality, real
		  and complex.  If the GCC (4.9 and later) predefined macros
		  specifying compiler intent are available, use them to determine
		  whether the overall intent is to support these features; otherwise,
		  presume an older compiler has intent to support these features and
		  define these macros by default.  */
		  /* wchar_t uses Unicode 10.0.0.  Version 10.0 of the Unicode Standard is
			 synchronized with ISO/IEC 10646:2017, fifth edition, plus
			 the following additions from Amendment 1 to the fifth edition:
			 - 56 emoji characters
			 - 285 hentaigana
			 - 3 additional Zanabazar Square characters */
			 /* We do not support C11 <threads.h>.  */
			 /*
			  * bitAnd - x&y using only ~ and |
			  *   Example: bitAnd(6, 5) = 4
			  *   Legal ops: ~ |
			  *   Max ops: 8
			  *   Rating: 1
			  */
	int bitAnd(int x, int y) {
	return ~(~x | ~y);
}
/*
 * getByte - Extract byte n from word x
 *   Bytes numbered from 0 (LSB) to 3 (MSB)
 *   Examples: getByte(0x12345678,1) = 0x56
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 6
 *   Rating: 2
 */
int getByte(int x, int n) {
	return 0xFF & (x >> (n << 3));
}
/*
 * logicalShift - shift x to the right by n, using a logical shift
 *   Can assume that 0 <= n <= 31
 *   Examples: logicalShift(0x87654321,4) = 0x08765432
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 20
 *   Rating: 3
 */
int logicalShift(int x, int n) {
	int mask = 1 << 31;//10000000...
	int high = !!(x & mask) << (32 + ~n);//用! 转化为0 1中的一个, 将减法转换成取反加一(31+(~n+1))
	int no_high = (x & ~mask) >> n;
	return high | no_high;
}
/*
 * bitCount - returns count of number of 1's in word
 *   Examples: bitCount(5) = 2, bitCount(7) = 3
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 40
 *   Rating: 4
 */
int bitCount(int x) {
	/*
	*将所有位分成32组，一组中只有1位
	*将相邻两组合为一组，组中的数值为原来两组中的数值相加
	*重复第2步，直到合成只有1组，组中的数值即为结果
	*/

	//----------注意运算顺序--------------
	//先算术运算，后移位运算，最后位运算
	//--------------------------------------
	int mask1 = 0x55;//01010101 
	int mask2 = 0x33;//00110011
	int mask3 = 0x0F;//00001111
	int mask4 = 0xFF;//11111111
	int result = 0;

	mask1 = mask1 | (mask1 << 8);
	mask1 = mask1 | (mask1 << 16);
	mask2 = mask2 | (mask2 << 8);
	mask2 = mask2 | (mask2 << 16);
	mask3 = mask3 | (mask3 << 8);
	mask3 = mask3 | (mask3 << 16);
	mask4 = mask4 | (mask4 << 8);
	mask4 = mask4 | (mask4 << 16);

	result = (x & mask1) + ((x >> 1)& mask1);//2 2 2 2...
	result = (result & mask2) + ((result >> 2)& mask2);//4 4 4 4 4 4 4 4
	result = (result & mask3) + ((result >> 4)& mask3);//8 8 8 8
	result = (result & mask4) + ((result >> 8)& mask4);//16 16

	return (result + (result >> 16)) & 0xFF;
}
/*
 * bang - Compute !x without using !
 *   Examples: bang(3) = 0, bang(0) = 1
 *   Legal ops: ~ & ^ | + << >>
 *   Max ops: 12
 *   Rating: 4
 */
int bang(int x) {
	//-0=0

	//return 1 & (1 ^ ((x | (~x + 1)) >> 31));
	return ((x | (~x + 1)) >> 31) + 1;
}
/*
 * tmin - return minimum two's complement integer
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 4
 *   Rating: 1
 */
int tmin(void) {
	return 1 << 31;
}
/*
 * fitsBits - return 1 if x can be represented as an
 *  n-bit, two's complement integer.
 *   1 <= n <= 32
 *   Examples: fitsBits(5,3) = 0, fitsBits(-4,3) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 15
 *   Rating: 2
 */
int fitsBits(int x, int n) {
	int shift = 33 + ~n;// 32 + (~n + 1)
	return !(x ^ ((x << shift) >> shift));
}
/*
 * divpwr2 - Compute x/(2^n), for 0 <= n <= 30
 *  Round toward zero
 *   Examples: divpwr2(15,1) = 7, divpwr2(-33,4) = -2
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 15
 *   Rating: 2
 */
int divpwr2(int x, int n) {
	int a = 1 << 31;//10000000
	int isNeg = !!(x & a);//是否为负数
	int totalDiv = (!!(~(a >> (32 + ~n))& x));//是否能被整除
	return (x >> n) + (totalDiv & isNeg);
}
/*
 * negate - return -x
 *   Example: negate(1) = -1.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int negate(int x) {
	return (~x + 1);
}
/*
 * isPositive - return 1 if x > 0, return 0 otherwise
 *   Example: isPositive(-1) = 0.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 8
 *   Rating: 3
 */
int isPositive(int x) {
	return !((x >> 31) | (!x));
}
/*
 * isLessOrEqual - if x <= y  then return 1, else return 0
 *   Example: isLessOrEqual(4,5) = 1.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 24
 *   Rating: 3
 */
int isLessOrEqual(int x, int y) {
	int singx = (x >> 31) & 1;
	int singy = (y >> 31) & 1;    //取得符号位
	int sing = (singx ^ singy) & singx; //singx和singy异号，取得x符号位
	int tmp = x + ((~y) + 1); // x - y, 异号情况下会越界
	tmp = ((tmp >> 31) & 1)& (!(singx ^ singy));// 保证singx 和 singy 同号
	return (sing | tmp | (!(x ^ y)));//判断相等
}
/*
 * ilog2 - return floor(log base 2 of x), where x > 0
 *   Example: ilog2(16) = 4
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 90
 *   Rating: 4
 */
int ilog2(int x) {
	//二分查找
	//找到最高位的1
	/**
	1. 如果x >> 16的结果大于0，那么可以说明最高位的位置至少是16，
	那么我们可以将结果的第4位置1（序号编号规则同上），
	因为2 ^ 4 = 16，反之置0说明结果小于16.
	2. 下面考虑两种情况
		如果第1步中x >> 16 大于0，
	说明我们需要在16位之后的第8位（第24位，相当于再二分）再进行二分查找，
		如果x >> 16小于0，那我们需要在16位之前的第8位（第8位，相当于再二分）进行查找，
	那么我们可以得出，下次查找时的范围为x >> (8 + result) (result表示上一步得到的结果（0或16）)，
	这个+result的意义可以认为是重新确定开始进一步二分查找的位置。
		如果x >> (8 + result) 的结果大于0，
	那么说明结果（result)的第3位必为1，
	相当于在结果上加上了查找到的新位置，
	反之第3位应该仍为0.
	3. 按照上面的思路继续查找到不能再二分（偏移为x >> (1 + reuslt)），
	此时result中得到最终的最高位的位置。
	*/
	int res = 0;
	int x1 = !!(x >> 16);
	int x2 = 0;
	int x3 = 0;
	int x4 = 0;
	int x5 = 0;

	res = x1 << 4;
	x2 = !!(x >> (8 + res));
	res = res | (x2 << 3);
	x3 = !!(x >> (4 + res));
	res = res | (x3 << 2);
	x4 = !!(x >> (2 + res));
	res = res | (x4 << 1);
	x5 = !!(x >> (1 + res));
	res = res | x5;
	return res;
}
/*
 * float_neg - Return bit-level equivalent of expression -f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representations of
 *   single-precision floating point values.
 *   When argument is NaN, return argument.
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 10
 *   Rating: 2
 */
unsigned float_neg(unsigned uf) {
	unsigned result;
	unsigned tmp;
	result = uf ^ 0x80000000; //将符号位取反
	tmp = uf & (0x7fffffff);
	if (tmp > 0x7f800000)//此时是NaN
		result = uf;
	return result;
}
/*
 * float_i2f - Return bit-level equivalent of expression (float) x
 *   Result is returned as unsigned int, but
 *   it is to be interpreted as the bit-level representation of a
 *   single-precision floating point values.
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 30
 *   Rating: 4
 */
unsigned float_i2f(int x) {
	unsigned s = 0;
	unsigned high = 0;
	unsigned temp = 0;
	unsigned afterShift = 0;
	unsigned flag = 0;
	if (x == 0) {
		return 0;
	}
	if (x < 0) {//x为负
		s = 0x80000000;
		x = -x;
	}
	afterShift = x;
	while (1) {
		temp = afterShift;
		afterShift <<= 1;
		high++;
		if (temp & 0x80000000)
			break;
	}
	/*
	如果舍弃的这九位的最高位为0，那么说明舍去的数值小于保留下来的最低位
	表示的值的二分之一，那么我们不需要舍入。

	如果舍弃的这九位的最高位为1，并且后面的位有数值，那么说明舍去的数值
	大于第9位表示的值的二分之一，这个时候我们需要舍入，也就是把最终结果加一。

	如果舍弃的这九位的最高位为1，并且后面的位都是0，这个时候正好
	就是第9位表示的值的二分之一。那么这个时候我们就要看第9位，如果第9位为0，
	那么不舍入。如果第9位为1，那么进行舍入，也就是把最终结果加一。
*/
	if ((afterShift & 0x01ff) > 0x0100)//最后9位大于1/2
		flag = 1;
	else if ((afterShift & 0x03ff) == 0x0300)//恰好相等是要看第10位是否为1
		flag = 1;
	else
		flag = 0;

	return s + (afterShift >> 9) + ((159 - high) << 23) + flag;
}
/*
 * float_twice - Return bit-level equivalent of expression 2*f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representation of
 *   single-precision floating point values.
 *   When argument is NaN, return argument
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 30
 *   Rating: 4
 */
unsigned float_twice(unsigned uf) {
	unsigned f = uf;
	if ((f & 0x7F800000) == 0) //非规格化
	{
		//有效位数部分左移一位
		f = ((f & 0x007FFFFF) << 1) | (0x80000000 & f);
	}
	else if ((f & 0x7F800000) != 0x7F800000) //规格化
	{
		f = f + 0x00800000;// 指数部分加1
	}
	return f;//超出
}
