#include <stdio.h>

int main() {
	int a;

	scanf_s("%d", &a);
	for (int i = 1; i < 9 + 1; i++) {
		printf("%d * %d = %d\n", (int)a, (int)i, (int)a * i);
	}
}
