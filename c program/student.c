#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    int rollNumber;
    char name[50];
    int marks[6];
    float percentage;
}

int main() {
    int numStudents;

    printf("Enter the number of students: ");
    scanf("%d", &numStudents);

    struct Student *students = (struct Student *)malloc(numStudents * sizeof(struct Student));

    for (int i = 0; i < numStudents; i++) {
        printf("\nEnter information for Student %d:\n", i + 1);

        printf("Enter roll number: ");
        scanf("%d", &students[i].rollNumber);

        printf("Enter name: ");
        scanf(" %[^\n]s", students[i].name);

        printf("Enter marks (sub1 sub2 sub3 sub4 sub5 sub6): ");
        for (int j = 0; j < 6; j++) {
            scanf("%d", &students[i].marks[j]);
        }

        int totalMarks = 0;
        for (int j = 0; j < 6; j++) {
            totalMarks += students[i].marks[j];
        }
        students[i].percentage = (float)totalMarks / 6;
    }

    for (int i = 0; i < numStudents; i++) {
        printf("\nStudent %d \n Roll Number: %d\n", i + 1, students[i].rollNumber);
        printf("Student %d Name: %s\n", i + 1, students[i].name);
        printf("Student %d Marks: ", i + 1);
        for (int j = 0; j < 6; j++) {
            printf("%d ", students[i].marks[j]);
        }
        printf("\n");
        printf("Student %d Percentage: %.2f%%\n", i + 1, students[i].percentage);
    }

    free(students);

    return 0;
}
