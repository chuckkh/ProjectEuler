#include <iostream>
#include <set>
#include <numeric>
#include <string>

int strToIntHomemade(std::string);

int main(int argc, char **argv)
{
    if (argc != 5){
        std::cout << "WRONG!" << '\n';
        return -1;
    }
    int div1 = strToIntHomemade(argv[1]);
    int div2 = strToIntHomemade(argv[2]);
    int limit1 = strToIntHomemade(argv[3]);
    int limit2 = strToIntHomemade(argv[4]);
    std::set<int> included;
    int stepper1 = limit1, stepper2 = limit1;
    while (stepper1 % div1) {stepper1 += 1;}
    while (stepper2 % div2) {stepper2 += 1;}
    while (stepper1 <= limit2) {
        included.insert(stepper1);
        stepper1 += div1;
    }
    while (stepper2 <= limit2) {
        included.insert(stepper2);
        stepper2 += div2;
    }
    int output = std::accumulate(included.begin(), included.end(), 0);
    std::cout << div1 << " " << div2 << " " << limit1 << " " << limit2 << '\n';
    std::cout << output << '\n';
    return output;
}

int strToIntHomemade(std::string inp){
    int result = 0;
    int sign = 1;
    for (int ind = 0; ind < inp.size(); ind++) {
        char c = inp[ind];
        if (c == 45){
            sign = -1;
        }
        else if (c>=48 && c<=57){
            result *= 10;
            result += (c-48);
        }
    }
    return result * sign;
}


// 0..3.56..90.2..5.......1005
//1005/2/15*7*1005

//..3.56..90.2..5
//..8.01..45.7..0
//..3.56..90.2..5



