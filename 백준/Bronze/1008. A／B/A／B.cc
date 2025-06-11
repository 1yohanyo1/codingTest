#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    double A, B;
    cin >> A >> B;
    double result = A / B;

    cout << fixed << setprecision(10) << result << endl;

    return 0;
}
