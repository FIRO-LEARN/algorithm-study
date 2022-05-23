#include <stdio.h>
#include <math.h>

int main() {
	float a, b, c, d, e;
	float addresult;
	int result;

	scanf_s("%f %f %f %f %f", &a, &b, &c, &d, &e);
	a = powf(a, 2);
	b = powf(b, 2);
	c = powf(c, 2);
	d = powf(d, 2);
	e = powf(e, 2);

	addresult = a + b + c + d + e;
	result = (int)addresult % 10;
	printf("%d", (int)result);
}
