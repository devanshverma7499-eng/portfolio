#include <stdio.h>

int main() {
    int choice;
    float balance = 1000.0;
    float amount;

    while (1) {
        printf("\n===== ATM MACHINE =====\n");
        printf("1. Check Balance\n");
        printf("2. Deposit Money\n");
        printf("3. Withdraw Money\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
        case 1:
            printf("\nYour Current Balance: %.2f\n", balance);
            break;

        case 2:
            printf("\nEnter amount to deposit: ");
            scanf("%f", &amount);
            if (amount > 0) {
                balance += amount;
                printf("Amount deposited successfully!\n");
            } else {
                printf("Invalid amount!\n");
            }
            break;

        case 3:
            printf("\nEnter amount to withdraw: ");
            scanf("%f", &amount);
            if (amount > balance) {
                printf("Insufficient Balance!\n");
            } else if (amount <= 0) {
                printf("Invalid amount!\n");
            } else {
                balance -= amount;
                printf("Please collect your cash.\n");
            }
            break;

        case 4:
            printf("\nThank you for using ATM.\n");
            return 0;  

        default:
            printf("\nInvalid Choice! Please try again.\n");
        }
    }

    return 0;
}
