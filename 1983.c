//1983. 조교의 성적 매기기 D2

#include <stdio.h>
#include <stdlib.h>
char alpha[20][20] = {"A+","A0","A-","B+","B0","B-","C+","C0","C-","D-"};
typedef struct {
	int student[101];
}element;

void init(element* student) {
	for (int i = 0; i < 101; i++) {
		student->student[i] = 0;
	}
}
int insert(int mid, int last, int work) {
	int result = 0;
	result = result + (mid * 0.35 + last * 0.45 + work * 0.2);
	return result;
}
void sort(element *student,int num) {
	int temp = 0;
	for (int i = 1; i <= num; i++) {
		for (int j = 1; j <= num ; j++) {
			if (student->student[i] > student->student[j]) {
				temp = student->student[j];
				student->student[j] = student->student[i];
				student->student[i] = temp;
			}
		}
	}
}
int main(void) {
	int test_case, K, num,loc_point=0, loc = 0;
	int mid, last, work;
	char point = {""};

	element student;
	printf("몇 번 테스트?(1~10) = ");
	scanf_s("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		init(&student);
		printf("학생 수 / 알고 싶은 학생 번호 =  ");
		scanf_s("%d", &num);
		scanf_s("%d", &K);
		int x = num / 10;
		for (int j = 1; j <= num; j++) {
			scanf_s("%d", &mid);
			scanf_s("%d", &last);
			scanf_s("%d", &work);
			student.student[j] = insert(mid, last, work);
			if (j == K) {
				loc_point = student.student[j];
			}
		}
		sort(&student, num);
		for (int n = 1; n <= num; n++) {
			if (student.student[n] == loc_point) {
				loc = n;
			}
		}
		printf("#%s\n", alpha[(loc / x)-1]);
	}
	return 0;
}
