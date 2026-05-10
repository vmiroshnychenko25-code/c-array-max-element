#include <stdio.h>

int main() {
    int n, i;

    // Введення розміру масиву
    printf("Введіть кількість елементів (N): ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Помилка: N має бути додатним числом.\n");
        return 1;
    }

    double array[n]; // Масив для N чисел
    double max;

    // Введення елементів масиву
    printf("Введіть %d чисел:\n", n);
    for (i = 0; i < n; i++) {
        printf("Елемент [%d]: ", i + 1);
        scanf("%lf", &array[i]);
    }

    // Алгоритм пошуку максимуму
    max = array[0]; // Припускаємо, що перший елемент — максимальний
    for (i = 1; i < n; i++) {
        if (array[i] > max) {
            max = array[i];
        }
    }

    // Виведення результату
    printf("\nМаксимальний елемент у масиві: %.2f\n", max);

    return 0;
}
