#include <stdio.h>
int main() {
    float a, b, product;
    printf("Enter two numbers: ");
    scanf("%lf  %lf", &a,         &b);  
 
    // Calculating product
    product = a * b;
    
    printf("Product = %.2lf", product);
    
    return 0;
}