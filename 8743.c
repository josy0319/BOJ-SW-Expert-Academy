//8673. 코딩 토너먼트1 D3

#include <stdio.h>
#include <stdlib.h>
typedef struct {
	int key;
}element;
typedef struct {
	int heap_size;
	element heap[1024];
}Heap;
int visted[100];
void init(Heap* heap) {
	heap->heap_size = 0;
}
void insert(Heap* heap,int point) {
	++(heap->heap_size);
	heap->heap[heap->heap_size].key = point;
}

int power(int a) {
	int final = 1;
	for (int i = 0; i < a; i++) {
		final *= 2;
	}
	return final;
}

int calculator(Heap* heap,int K) {
	int result = 0;
	while (K) {
		int KK = power(K);
		for (int i = 1; i <= KK; i+=2) {
			if (heap->heap[i].key > heap->heap[i + 1].key) {
				result = result + (heap->heap[i].key - heap->heap[i + 1].key);
				heap->heap[(i / 2) +1] = heap->heap[i]; 
				//printf("승자 %d\n",heap->heap[i].key);
			}
			if (heap->heap[i].key <= heap->heap[i + 1].key) {
				result = result + (heap->heap[i+1].key - heap->heap[i].key);
				heap->heap[(i / 2) +1] = heap->heap[i+1];
				//printf("승자 %d\n",heap->heap[i+1].key);
			}
		}
		K--;
	}
	return result;
}


int main(void) {
	int test_case,K,num,KK;
	Heap heap;
	init(&heap);
	//printf("몇 번 테스트?(1~10) = ");
	scanf_s("%d", &test_case);
	for (int i = 1; i <= test_case; i++) {
		//printf("2k승 k = ");
		scanf_s("%d", &K);
		KK = power(K);
		for (int j = 0; j < KK; j++) {
			scanf_s("%d", &num);
			insert(&heap, num);
		}
		int a = calculator(&heap, K);
		printf("#%d %d\n", i, a);
		init(&heap);
	}

	return;
}
