/**
 * 
 * Create a C program that says how many feet are in 3.5 yards, 
 * and how many inches are in 3.5 yards. (Note: 1 yard = 3 feet, 1 foot = 12 inches). 
 *
 *  Make sure to print out the results to the terminal.
 *
 */ 


#include <stdio.h>
int main() {
    /*
    This function will perform some arbitrary arithmetic on a static value
    */

    // Static value of yards to perform arithmetic on
    double yards = 3.5;
    
    // Declare conversions
    double inches_in_foot = 12.0;
    double feet_in_yard = 3.0;

    // First calculation
    double answer = yards * feet_in_yard * inches_in_foot;
    
    // Print first answer to console
    printf("There are %.1f inches in %.1f yards.\n", answer, yards);    

    // Second calculation
    answer = yards * feet_in_yard;

    // Print second answer to console
    printf("There are %.1f feet in %.1f yards.\n", answer, yards);

    // Terminate
    return 0;
}